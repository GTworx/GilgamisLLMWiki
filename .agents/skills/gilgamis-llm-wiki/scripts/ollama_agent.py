#!/usr/bin/env python3
"""
Gilgamis LLM Wiki — Local Ollama (qwen3.8) Agentic Ingestion & Execution Engine
================================================================================
Provides local LLM execution powered by Ollama (`qwen3.8:latest` / `qwen3.8:27b`)
for the Gilgamis LLM Wiki knowledge base:

Subcommands:
  1. status   — Check Ollama server, qwen3.8 model specs, wiki metrics, & library inventory.
  2. extract  — Extract text from PDF (with automatic qwen3.8 multimodal Vision OCR fallback for scanned pages).
  3. ingest   — Analyze a PDF book/article via qwen3.8 and generate/update interlinked wiki pages + dashboard.
  4. query    — Answer cross-comparative literary/strategic queries over the wiki using qwen3.8.
  5. audit    — Verify 100% wiki link integrity, metadata completeness, and zero orphans.
"""

import argparse
import base64
import datetime
import glob
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

try:
    import pypdf
except ImportError:
    pypdf = None

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

DEFAULT_OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_MODEL = os.environ.get("GILGAMIS_OLLAMA_MODEL", "qwen3.8:latest")
LIBRARY_MOUNT = r"C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary"


def get_base_dir() -> str:
    cur = os.path.dirname(os.path.abspath(__file__))
    base = os.path.abspath(os.path.join(cur, "..", "..", "..", ".."))
    if os.path.exists(os.path.join(base, "wiki")):
        return base
    return os.path.abspath(".")


def slugify(text: str) -> str:
    text = text.lower().strip()
    replacements = {
        "ç": "c", "ğ": "g", "ı": "i", "ö": "o", "ş": "s", "ü": "u",
        "â": "a", "î": "i", "û": "u", "é": "e", "è": "e", "ê": "e",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


# ---------------------------------------------------------------------------
# Ollama REST API Client (Zero External Dependencies)
# ---------------------------------------------------------------------------

def ollama_request(endpoint: str, payload: dict = None, timeout: int = 600, base_url: str = DEFAULT_OLLAMA_URL) -> dict:
    url = f"{base_url.rstrip('/')}/{endpoint.lstrip('/')}"
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"}, method="POST")
    else:
        req = urllib.request.Request(url, method="GET")

    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode("utf-8"))


def ollama_chat(
    messages: list,
    model: str = DEFAULT_MODEL,
    think: bool = False,
    temperature: float = 0.2,
    num_ctx: int = 32768,
    images: list = None,
    json_format: bool = False,
    timeout: int = 900,
) -> dict:
    if images and messages:
        messages[-1]["images"] = images

    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "think": think,
        "options": {
            "temperature": temperature,
            "num_ctx": num_ctx,
            "num_predict": 2800,
        },
    }
    if json_format:
        payload["format"] = "json"

    t0 = time.time()
    res = ollama_request("/api/chat", payload=payload, timeout=timeout)
    elapsed = time.time() - t0
    eval_count = res.get("eval_count", 0)
    eval_dur_s = max(res.get("eval_duration", 1) / 1e9, 0.001)
    res["_metrics"] = {
        "elapsed_s": round(elapsed, 2),
        "load_s": round(res.get("load_duration", 0) / 1e9, 2),
        "prompt_tokens": res.get("prompt_eval_count", 0),
        "Output_tokens": eval_count,
        "tokens_per_sec": round(eval_count / eval_dur_s, 1),
    }
    return res


# ---------------------------------------------------------------------------
# PDF Text + Vision OCR Extraction
# ---------------------------------------------------------------------------

def extract_jpeg_streams_from_page(page) -> list:
    """Extract raw JPEG (/DCTDecode) byte streams from a pypdf PageObject without requiring Pillow."""
    jpegs = []
    try:
        resources = page.get("/Resources")
        if not resources:
            return jpegs
        resources = resources.get_object()
        xobjects = resources.get("/XObject")
        if not xobjects:
            return jpegs
        xobjects = xobjects.get_object()
        for key in xobjects:
            obj = xobjects[key].get_object()
            if obj.get("/Subtype") == "/Image":
                flt = obj.get("/Filter")
                if flt == "/DCTDecode" or (isinstance(flt, list) and "/DCTDecode" in flt):
                    raw_bytes = getattr(obj, "_data", None)
                    if raw_bytes:
                        jpegs.append(base64.b64encode(raw_bytes).decode("ascii"))
    except Exception:
        pass
    return jpegs


def extract_pdf_content(
    pdf_path: str,
    model: str = DEFAULT_MODEL,
    use_vision_ocr: bool = True,
    max_chars: int = 55000,
) -> dict:
    """
    Extracts structured page-indexed text from a PDF file.
    - For short documents (<= 35 pages), extracts all pages in sequence.
    - For book-length documents (> 35 pages), extracts front matter / TOC (first 15 pages),
      evenly spaced strategic samples across the body, and conclusion pages so the entire
      intellectual arc fits inside the prompt with exact page numbers.
    - If a page has no text layer and contains an embedded JPEG scan, uses qwen3.8 Vision OCR.
    """
    if pypdf is None:
        raise RuntimeError("pypdf is required for PDF extraction.")

    reader = pypdf.PdfReader(pdf_path)
    total_pages = len(reader.pages)

    if total_pages <= 35:
        selected_indices = list(range(total_pages))
    else:
        front = list(range(min(14, total_pages)))
        back = list(range(max(14, total_pages - 5), total_pages))
        middle_pool = list(range(14, max(14, total_pages - 5)))
        step = max(1, len(middle_pool) // 26)
        middle = middle_pool[::step][:26]
        selected_indices = sorted(set(front + middle + back))

    pages_data = []
    accumulated_chars = 0
    ocr_pages_used = 0

    for idx in selected_indices:
        page = reader.pages[idx]
        text = (page.extract_text() or "").strip()

        if len(text) < 40 and use_vision_ocr and ocr_pages_used < 6:
            jpegs = extract_jpeg_streams_from_page(page)
            if jpegs:
                print(f"  [Vision OCR] Transcribing scanned page {idx + 1}/{total_pages} with {model}...")
                ocr_res = ollama_chat(
                    messages=[
                        {
                            "role": "user",
                            "content": (
                                f"Transcribe all visible text on page {idx + 1} accurately. "
                                "Preserve headings, paragraphs, author names, and citations."
                            ),
                        }
                    ],
                    model=model,
                    think=False,
                    images=[jpegs[0]],
                    num_ctx=8192,
                )
                ocr_text = ocr_res.get("message", {}).get("content", "").strip()
                if ocr_text:
                    text = f"[Transcribed via {model} Vision OCR]\n{ocr_text}"
                    ocr_pages_used += 1

        if text:
            chunk = f"--- [PAGE {idx + 1} of {total_pages}] ---\n{text}\n"
            pages_data.append({"page": idx + 1, "text": text})
            accumulated_chars += len(chunk)
            if accumulated_chars >= max_chars:
                break

    combined_text = "\n".join(
        f"--- [PAGE {p['page']} of {total_pages}] ---\n{p['text']}" for p in pages_data
    )
    if len(combined_text) > max_chars:
        combined_text = combined_text[:max_chars] + "\n...[Truncated to fit context window]..."

    return {
        "pdf_path": pdf_path,
        "total_pages": total_pages,
        "sampled_pages": len(pages_data),
        "ocr_pages": ocr_pages_used,
        "text": combined_text,
    }


# ---------------------------------------------------------------------------
# Wiki Inventory & Audit Helpers
# ---------------------------------------------------------------------------

def get_wiki_inventory(base_dir: str) -> dict:
    wiki_dir = os.path.join(base_dir, "wiki")
    inv = {"books": {}, "authors": {}, "genres": {}, "themes": {}}
    for cat in inv:
        cat_dir = os.path.join(wiki_dir, cat)
        if not os.path.exists(cat_dir):
            continue
        for f in sorted(glob.glob(os.path.join(cat_dir, "*.md"))):
            slug = os.path.basename(f)[:-3]
            with open(f, "r", encoding="utf-8") as fp:
                txt = fp.read()
            m = re.search(r"^#\s*(?:Author:|Genre:|Theme:)?\s*(.*)", txt, re.MULTILINE)
            title = m.group(1).strip() if m else slug
            inv[cat][slug] = {"slug": slug, "title": title, "path": f}
    return inv


def audit_wiki(base_dir: str) -> dict:
    wiki_dir = os.path.join(base_dir, "wiki")
    all_pages = {}
    for sub in ["books", "authors", "genres", "themes"]:
        for f in glob.glob(os.path.join(wiki_dir, sub, "*.md")):
            slug = os.path.basename(f)[:-3]
            with open(f, "r", encoding="utf-8") as fp:
                all_pages[slug] = {"cat": sub, "path": f, "content": fp.read()}

    index_path = os.path.join(wiki_dir, "index.md")
    index_txt = open(index_path, "r", encoding="utf-8").read() if os.path.exists(index_path) else ""

    broken_links = []
    inbound_counts = {slug: 0 for slug in all_pages}

    for slug, info in all_pages.items():
        links = re.findall(r"\[\[([a-zA-Z0-9_\-]+)\]\]", info["content"])
        for target in links:
            if target not in all_pages:
                broken_links.append((slug, target))
            elif target != slug:
                inbound_counts[target] += 1

    for target in re.findall(r"\[\[([a-zA-Z0-9_\-]+)\]\]", index_txt):
        if target not in all_pages:
            broken_links.append(("index.md", target))

    orphans = [s for s, c in inbound_counts.items() if c == 0]
    unindexed = [s for s in all_pages if f"[[{s}]]" not in index_txt]

    return {
        "counts": {
            "books": sum(1 for v in all_pages.values() if v["cat"] == "books"),
            "authors": sum(1 for v in all_pages.values() if v["cat"] == "authors"),
            "genres": sum(1 for v in all_pages.values() if v["cat"] == "genres"),
            "themes": sum(1 for v in all_pages.values() if v["cat"] == "themes"),
            "total_entities": len(all_pages),
        },
        "broken_links": broken_links,
        "orphans": orphans,
        "unindexed": unindexed,
    }


# ---------------------------------------------------------------------------
# Subcommand: status
# ---------------------------------------------------------------------------

def cmd_status(args):
    base_dir = get_base_dir()
    print("=" * 76)
    print(" GILGAMIS LLM WIKI — OLLAMA (qwen3.8) AGENTIC SESSION STATUS")
    print("=" * 76)

    # 1. Check Ollama Server
    try:
        tags = ollama_request("/api/tags", timeout=10)
        models = tags.get("models", [])
        print(f"[Ollama Server] ONLINE at {DEFAULT_OLLAMA_URL} ({len(models)} local models installed)")
        for m in models:
            det = m.get("details", {})
            caps = ", ".join(m.get("capabilities", []))
            size_gb = round(m.get("size", 0) / (1024 ** 3), 2)
            print(
                f"  • {m['name']} | {det.get('parameter_size', '?')} ({det.get('quantization_level', '?')}) "
                f"| {size_gb} GB | ctx={det.get('context_length', '?')} | capabilities=[{caps}]"
            )
    except Exception as e:
        print(f"[Ollama Server] OFFLINE or unreachable at {DEFAULT_OLLAMA_URL}: {e}")

    # 2. Check Wiki Metrics
    audit = audit_wiki(base_dir)
    c = audit["counts"]
    print("\n[Wiki Knowledge Base Metrics]")
    print(
        f"  • Books: {c['books']} | Authors: {c['authors']} | Genres: {c['genres']} "
        f"| Themes: {c['themes']} | Total Entity Pages: {c['total_entities']}"
    )
    print(
        f"  • Link Integrity: {len(audit['broken_links'])} broken links | "
        f"{len(audit['orphans'])} orphans | {len(audit['unindexed'])} unindexed"
    )

    # 3. Check Mounted Library
    if os.path.exists(LIBRARY_MOUNT):
        print(f"\n[Primary Mounted Library: {LIBRARY_MOUNT}]")
        for root_sub in ["BOOKS", "ARTICLES-REPORTS"]:
            p = os.path.join(LIBRARY_MOUNT, root_sub)
            if os.path.exists(p):
                cats = [d for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))]
                print(f"  • {root_sub}/: {len(cats)} domain folders")
    print("=" * 76)


# ---------------------------------------------------------------------------
# Subcommand: extract
# ---------------------------------------------------------------------------

def cmd_extract(args):
    info = extract_pdf_content(
        args.pdf_path,
        model=args.model,
        use_vision_ocr=not args.no_ocr,
        max_chars=args.max_chars,
    )
    print(
        f"Extracted {info['sampled_pages']}/{info['total_pages']} pages "
        f"(Vision OCR pages: {info['ocr_pages']}, chars: {len(info['text'])})"
    )
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(info["text"])
        print(f"Saved extracted text to {args.out}")
    else:
        print(info["text"][:4000])


# ---------------------------------------------------------------------------
# Subcommand: ingest
# ---------------------------------------------------------------------------

def format_source_display(pdf_path: str, base_dir: str) -> str:
    abs_pdf = os.path.abspath(pdf_path)
    if abs_pdf.lower().startswith(LIBRARY_MOUNT.lower()):
        rel = abs_pdf[len(LIBRARY_MOUNT):].lstrip("\\/").replace("\\", "/")
        parent_dir = os.path.dirname(abs_pdf) + "\\"
        return f"{rel} (Mount: {parent_dir})"
    elif abs_pdf.lower().startswith(base_dir.lower()):
        return abs_pdf[len(base_dir):].lstrip("\\/").replace("\\", "/")
    return abs_pdf.replace("\\", "/")


def format_short_source(pdf_path: str, base_dir: str) -> str:
    abs_pdf = os.path.abspath(pdf_path)
    if abs_pdf.lower().startswith(LIBRARY_MOUNT.lower()):
        return abs_pdf[len(LIBRARY_MOUNT):].lstrip("\\/").replace("\\", "/")
    elif abs_pdf.lower().startswith(base_dir.lower()):
        return abs_pdf[len(base_dir):].lstrip("\\/").replace("\\", "/")
    return os.path.basename(abs_pdf)


def cmd_ingest(args):
    base_dir = get_base_dir()
    inv = get_wiki_inventory(base_dir)
    pdf_path = os.path.abspath(args.pdf_path)
    if not os.path.exists(pdf_path):
        print(f"ERROR: File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    print(f"[1/4] Extracting PDF content from: {pdf_path}")
    extracted = extract_pdf_content(
        pdf_path,
        model=args.model,
        use_vision_ocr=True,
        max_chars=args.max_chars,
    )
    short_src = format_short_source(pdf_path, base_dir)
    full_src = format_source_display(pdf_path, base_dir)
    print(
        f"      Total pages: {extracted['total_pages']} | Sampled pages: {extracted['sampled_pages']} "
        f"| Vision OCR pages: {extracted['ocr_pages']} | Extracted chars: {len(extracted['text'])}"
    )

    existing_books = ", ".join(f"[[{k}]] ({v['title']})" for k, v in list(inv["books"].items())[:25])
    existing_genres = ", ".join(f"[[{k}]]" for k in inv["genres"].keys())
    existing_themes = ", ".join(f"[[{k}]]" for k in inv["themes"].keys())
    existing_authors = ", ".join(f"[[{k}]]" for k in inv["authors"].keys())

    system_prompt = (
        "You are the scholarly archivist and analytical synthesis engine for the Gilgamis LLM Wiki "
        "(following Andrej Karpathy's LLM Wiki pattern). You analyze primary PDF books and academic papers "
        "and return a rich, rigorous, strictly valid JSON object for wiki ingestion.\n"
        "CRITICAL RULES:\n"
        "1. Every factual claim and quote MUST include exact page citations referencing the source file, "
        f"e.g. (source: {short_src}, p. 12).\n"
        "2. Reuse existing wiki slugs where relevant, and propose 1-2 new genre or theme slugs only when "
        "the work introduces genuinely distinct domains.\n"
        "3. Connect the work to at least 3 existing books in `thematic_connections` using [[book-slug]] syntax.\n"
        "4. Output ONLY valid JSON matching the requested schema."
    )

    user_prompt = f"""Analyze the following document and generate a complete Gilgamis LLM Wiki ingestion JSON payload.

SOURCE METADATA:
- Short Source Path: `{short_src}`
- Full Source Header: `{full_src}`
- Total PDF Pages: {extracted['total_pages']}

EXISTING WIKI ENTITIES FOR CROSS-LINKING:
- Existing Books: {existing_books}
- Existing Genres: {existing_genres}
- Existing Themes: {existing_themes}
- Existing Authors: {existing_authors}

REQUIRED JSON SCHEMA:
{{
  "slug": "lowercase-hyphenated-book-title",
  "title": "Full Book or Article Title: Subtitle",
  "year": 2026,
  "authors": [
    {{
      "slug": "author-slug",
      "name": "Full Author Name",
      "eras": "Academic / Historical Era & Movement",
      "bio": "2-paragraph scholarly biography and context citing [[book-slug]] and page numbers.",
      "one_line_index_summary": "Concise 1-sentence authority summary for wiki/index.md."
    }}
  ],
  "genres": [
    {{
      "slug": "genre-slug",
      "name": "Genre Title",
      "description": "1-sentence scholarly definition of the genre.",
      "overview": "2-paragraph overview of how this genre operates in the wiki, referencing [[book-slug]]."
    }}
  ],
  "themes": [
    {{
      "slug": "theme-slug",
      "name": "Theme Title",
      "summary": "1-sentence summary of the theme.",
      "synthesis": "2-paragraph cross-cutting synthesis connecting [[book-slug]] with existing wiki works."
    }}
  ],
  "executive_summary": "2 rich, comprehensive scholarly paragraphs summarizing the core thesis, methodology, and conclusions with page citations (source: {short_src}, pp. X-Y).",
  "chapter_breakdown": [
    "* **Section / Chapter Title (pp. X–Y)**:\\n  * *Key Concept*: Detailed analytical breakdown with citations (source: {short_src}, p. X)."
  ],
  "quotes": [
    "* \\"Exact verbatim quote from the text.\\" (source: {short_src}, p. X)"
  ],
  "thematic_connections": [
    "* **Connection Title**: Deep comparative synthesis linking this work to [[existing-book-slug]] and [[existing-author-slug]] on [[existing-theme-slug]]."
  ]
}}

DOCUMENT TEXT:
{extracted['text']}
"""

    print(f"[2/4] Querying local Ollama model `{args.model}` (think={args.think})...")
    res = ollama_chat(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
        model=args.model,
        think=args.think,
        temperature=0.2,
        num_ctx=args.num_ctx,
        json_format=True,
    )
    metrics = res.get("_metrics", {})
    print(
        f"      Ollama completed in {metrics.get('elapsed_s')}s "
        f"({metrics.get('Output_tokens')} tokens @ {metrics.get('tokens_per_sec')} tok/s)"
    )

    raw_content = res.get("message", {}).get("content", "").strip()
    # Strip markdown code fences if present
    raw_content = re.sub(r"^```(?:json)?\s*", "", raw_content)
    raw_content = re.sub(r"\s*```$", "", raw_content)
    data = json.loads(raw_content)

    if args.out_json:
        with open(args.out_json, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"      Saved structured analysis JSON to {args.out_json}")

    if args.write:
        print("[3/4] Writing & updating interlinked Wiki pages...")
        updated_pages = apply_ingestion_to_wiki(data, full_src, short_src, extracted["total_pages"], base_dir)
        print(f"      Touched {len(updated_pages)} wiki pages:")
        for p in updated_pages:
            print(f"        - {p}")
        if args.rebuild:
            print("[4/4] Rebuilding interactive HTML dashboard...")
            import build_dashboard
            build_dashboard.build()
    else:
        print(json.dumps(data, ensure_ascii=False, indent=2))


def apply_ingestion_to_wiki(data: dict, full_src: str, short_src: str, total_pages: int, base_dir: str) -> list:
    wiki_dir = os.path.join(base_dir, "wiki")
    today = datetime.date.today().isoformat()
    touched = []

    book_slug = slugify(data["slug"])
    book_title = data["title"].strip()
    year = int(data.get("year", 2026))

    authors = data.get("authors", [])
    genres = data.get("genres", [])
    themes = data.get("themes", [])

    author_slugs = [slugify(a["slug"]) for a in authors]
    genre_slugs = [slugify(g["slug"]) for g in genres]
    theme_slugs = [slugify(t["slug"]) for t in themes]

    authors_links = ", ".join(f"[[{s}]]" for s in author_slugs)
    genres_links = ", ".join(f"[[{s}]]" for s in genre_slugs)
    themes_links = ", ".join(f"[[{s}]]" for s in theme_slugs)

    chapters_md = "\n\n".join(data.get("chapter_breakdown", []))
    quotes_md = "\n".join(data.get("quotes", []))
    connections_md = "\n".join(data.get("thematic_connections", []))

    related_slugs = []
    for s in author_slugs + genre_slugs + theme_slugs:
        if s not in related_slugs:
            related_slugs.append(s)
    for m in re.findall(r"\[\[([a-zA-Z0-9_\-]+)\]\]", connections_md):
        if m not in related_slugs and m != book_slug:
            related_slugs.append(m)

    related_md = "\n".join(f"- [[{s}]]" for s in related_slugs)

    book_md = f"""# {book_title}

**Author(s)**: {authors_links}  
**Genre(s)**: {genres_links}  
**Key Themes**: {themes_links}  
**Publication Year**: {year}  
**Source**: {full_src}  
**Last updated**: {today}  

---

## Executive Summary

{data.get('executive_summary', '').strip()}

---

## Key Arguments / Chapter Breakdown

{chapters_md}

---

## Key Quotes & Citations

{quotes_md}

---

## Thematic Connections

{connections_md}

---

## Related pages

{related_md}
"""
    book_path = os.path.join(wiki_dir, "books", f"{book_slug}.md")
    with open(book_path, "w", encoding="utf-8") as f:
        f.write(book_md)
    touched.append(f"wiki/books/{book_slug}.md")

    # 2. Create or Update Authors
    for a in authors:
        a_slug = slugify(a["slug"])
        a_path = os.path.join(wiki_dir, "authors", f"{a_slug}.md")
        if os.path.exists(a_path):
            with open(a_path, "r", encoding="utf-8") as f:
                txt = f.read()
            if f"[[{book_slug}]]" not in txt:
                txt = re.sub(
                    r"(## Books in Wiki\s*\n)",
                    f"\\1- [[{book_slug}]] ({year})\n",
                    txt,
                )
                if f"- [[{book_slug}]]" not in txt:
                    txt += f"\n- [[{book_slug}]] ({year})\n"
                with open(a_path, "w", encoding="utf-8") as f:
                    f.write(txt)
                touched.append(f"wiki/authors/{a_slug}.md")
        else:
            rec_themes = "\n".join(f"- [[{t}]]" for t in theme_slugs)
            rel_items = "\n".join(f"- [[{x}]]" for x in ([book_slug] + genre_slugs + theme_slugs))
            a_md = f"""# Author: {a['name']}

**Eras / Movements**: {a.get('eras', 'Contemporary Scholarship')}
**Primary Genres**: {genres_links}
**Last updated**: {today}

---

## Biography & Context
{a.get('bio', '').strip()}

---

## Books in Wiki
- [[{book_slug}]] ({year})

---

## Recurring Themes
{rec_themes}

---

## Related pages
{rel_items}
"""
            with open(a_path, "w", encoding="utf-8") as f:
                f.write(a_md)
            touched.append(f"wiki/authors/{a_slug}.md")

    # 3. Create or Update Genres
    for g in genres:
        g_slug = slugify(g["slug"])
        g_path = os.path.join(wiki_dir, "genres", f"{g_slug}.md")
        if os.path.exists(g_path):
            with open(g_path, "r", encoding="utf-8") as f:
                txt = f.read()
            if f"[[{book_slug}]]" not in txt:
                entry = f"- [[{book_slug}]] ({year}) — {authors_links}\n"
                if "## Books in Wiki" in txt:
                    txt = re.sub(r"(## Books in Wiki\s*\n)", f"\\1{entry}", txt)
                elif "## Featured Works" in txt:
                    txt = re.sub(r"(## Featured Works\s*\n)", f"\\1{entry}", txt)
                else:
                    txt += f"\n## Books in Wiki\n{entry}"
                with open(g_path, "w", encoding="utf-8") as f:
                    f.write(txt)
                touched.append(f"wiki/genres/{g_slug}.md")
        else:
            auth_bullets = "\n".join(f"- [[{s}]]" for s in author_slugs)
            rel_bullets = "\n".join(f"- [[{s}]]" for s in theme_slugs)
            g_md = f"""# Genre: {g['name']}

**Description**: {g.get('description', '').strip()}
**Key Themes**: {themes_links}
**Last updated**: {today}

---

## Overview & Scope
{g.get('overview', '').strip()}

---

## Books in Wiki
- [[{book_slug}]] ({year}) — {authors_links}

---

## Key Authors & Theorists
{auth_bullets}

---

## Related Genres & Themes
{rel_bullets}
"""
            with open(g_path, "w", encoding="utf-8") as f:
                f.write(g_md)
            touched.append(f"wiki/genres/{g_slug}.md")

    # 4. Create or Update Themes
    for t in themes:
        t_slug = slugify(t["slug"])
        t_path = os.path.join(wiki_dir, "themes", f"{t_slug}.md")
        if os.path.exists(t_path):
            with open(t_path, "r", encoding="utf-8") as f:
                txt = f.read()
            if f"[[{book_slug}]]" not in txt:
                entry = f"- [[{book_slug}]] ({year}) — {authors_links}\n"
                if "## Featured Works" in txt:
                    txt = re.sub(r"(## Featured Works\s*\n)", f"\\1{entry}", txt)
                else:
                    txt += f"\n## Featured Works\n{entry}"
                with open(t_path, "w", encoding="utf-8") as f:
                    f.write(txt)
                touched.append(f"wiki/themes/{t_slug}.md")
        else:
            auth_bullets = "\n".join(f"- [[{s}]]" for s in author_slugs)
            rel_bullets = "\n".join(f"- [[{s}]]" for s in genre_slugs)
            t_md = f"""# Theme: {t['name']}

**Summary**: {t.get('summary', '').strip()}
**Last updated**: {today}

---

## Synthesis
{t.get('synthesis', '').strip()}

---

## Featured Works
- [[{book_slug}]] ({year}) — {authors_links}

---

## Key Authors & Perspectives
{auth_bullets}

---

## Related themes & genres
{rel_bullets}
"""
            with open(t_path, "w", encoding="utf-8") as f:
                f.write(t_md)
            touched.append(f"wiki/themes/{t_slug}.md")

    return touched


# ---------------------------------------------------------------------------
# Subcommand: query
# ---------------------------------------------------------------------------

def cmd_query(args):
    base_dir = get_base_dir()
    wiki_dir = os.path.join(base_dir, "wiki")
    index_path = os.path.join(wiki_dir, "index.md")
    index_txt = open(index_path, "r", encoding="utf-8").read() if os.path.exists(index_path) else ""

    # Rank relevant book & theme files by keyword overlap with the query
    q_words = set(re.findall(r"[a-z0-9]{3,}", args.question.lower()))
    scored_files = []
    for sub in ["books", "themes", "authors", "genres"]:
        for f in glob.glob(os.path.join(wiki_dir, sub, "*.md")):
            txt = open(f, "r", encoding="utf-8").read()
            txt_lower = txt.lower()
            score = sum(txt_lower.count(w) for w in q_words)
            if score > 0:
                scored_files.append((score, os.path.basename(f), txt[:3500]))

    scored_files.sort(key=lambda x: x[0], reverse=True)
    top_contexts = "\n\n".join(
        f"=== WIKI PAGE: {fname} (relevance={sc}) ===\n{snippet}"
        for sc, fname, snippet in scored_files[:8]
    )

    messages = [
        {
            "role": "system",
            "content": (
                "You are the Gilgamis LLM Wiki synthesis engine powered by Qwen 3.8. "
                "Synthesize a scholarly, cross-comparative response citing specific wiki entities "
                "with [[slug]] links and exact source page numbers."
            ),
        },
        {
            "role": "user",
            "content": (
                f"MASTER INDEX OVERVIEW:\n{index_txt[:6000]}\n\n"
                f"RELEVANT WIKI DETAIL PAGES:\n{top_contexts}\n\n"
                f"USER QUESTION:\n{args.question}"
            ),
        },
    ]

    print(f"Querying `{args.model}` across {len(scored_files[:8])} matched wiki pages...")
    res = ollama_chat(messages=messages, model=args.model, think=args.think, num_ctx=args.num_ctx)
    metrics = res.get("_metrics", {})
    print("-" * 76)
    print(res.get("message", {}).get("content", ""))
    print("-" * 76)
    print(
        f"[Ollama {args.model} | {metrics.get('elapsed_s')}s | "
        f"{metrics.get('Output_tokens')} tokens @ {metrics.get('tokens_per_sec')} tok/s]"
    )


# ---------------------------------------------------------------------------
# Subcommand: audit
# ---------------------------------------------------------------------------

def cmd_audit(args):
    base_dir = get_base_dir()
    res = audit_wiki(base_dir)
    c = res["counts"]
    print("=" * 68)
    print(" GILGAMIS LLM WIKI — LINK & METADATA INTEGRITY AUDIT")
    print("=" * 68)
    print(f"  Books   : {c['books']}")
    print(f"  Authors : {c['authors']}")
    print(f"  Genres  : {c['genres']}")
    print(f"  Themes  : {c['themes']}")
    print(f"  Total   : {c['total_entities']} entity pages (+ index.md & log.md)")
    print("-" * 68)
    print(f"  Broken [[links]] : {len(res['broken_links'])}")
    for src, dst in res["broken_links"]:
        print(f"    ! {src} -> [[{dst}]]")
    print(f"  Orphan pages     : {len(res['orphans'])}")
    for o in res["orphans"]:
        print(f"    ! [[{o}]]")
    print(f"  Unindexed pages  : {len(res['unindexed'])}")
    for u in res["unindexed"]:
        print(f"    ! [[{u}]]")
    print("=" * 68)


def main():
    parser = argparse.ArgumentParser(
        description="Gilgamis LLM Wiki — Local Ollama (qwen3.8) Ingestion & Execution CLI"
    )
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Ollama model name (default: {DEFAULT_MODEL})")
    parser.add_argument("--think", action="store_true", help="Enable Qwen 3.8 extended thinking mode")
    parser.add_argument("--num-ctx", type=int, default=32768, help="Ollama context window size (default: 32768)")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="Show Ollama model status and Gilgamis Wiki metrics")

    p_ext = sub.add_parser("extract", help="Extract text (and Vision OCR for scans) from a PDF")
    p_ext.add_argument("pdf_path", help="Path to PDF file")
    p_ext.add_argument("--no-ocr", action="store_true", help="Disable Vision OCR fallback")
    p_ext.add_argument("--max-chars", type=int, default=55000, help="Max characters to extract")
    p_ext.add_argument("--out", help="Output text file path")

    p_ing = sub.add_parser("ingest", help="Analyze and ingest a PDF into the Gilgamis LLM Wiki via qwen3.8")
    p_ing.add_argument("pdf_path", help="Path to PDF file")
    p_ing.add_argument("--max-chars", type=int, default=45000, help="Max extracted characters sent to model")
    p_ing.add_argument("--out-json", help="Save structured LLM JSON output to file")
    p_ing.add_argument("--write", action="store_true", default=True, help="Write markdown pages to wiki/")
    p_ing.add_argument("--no-write", action="store_false", dest="write", help="Dry-run without writing wiki files")
    p_ing.add_argument("--rebuild", action="store_true", default=True, help="Rebuild dashboard HTML after ingestion")

    p_qry = sub.add_parser("query", help="Query the Gilgamis LLM Wiki using local qwen3.8")
    p_qry.add_argument("question", help="Cross-book question to synthesize")

    sub.add_parser("audit", help="Run wiki link integrity and orphan audit")

    args = parser.parse_args()
    if args.command == "status":
        cmd_status(args)
    elif args.command == "extract":
        cmd_extract(args)
    elif args.command == "ingest":
        cmd_ingest(args)
    elif args.command == "query":
        cmd_query(args)
    elif args.command == "audit":
        cmd_audit(args)


if __name__ == "__main__":
    main()
