import os
import glob
import re
import json

def get_base_dir():
    cur = os.path.dirname(os.path.abspath(__file__))
    base = os.path.abspath(os.path.join(cur, '..', '..', '..', '..'))
    if os.path.exists(os.path.join(base, 'wiki')):
        return base
    if os.path.exists('wiki'):
        return os.path.abspath('.')
    return base

def parse_log_added_info(wiki_dir):
    log_file = os.path.join(wiki_dir, 'log.md')
    if not os.path.exists(log_file):
        return {}
    with open(log_file, 'r', encoding='utf-8') as f:
        log_txt = f.read()
    sections = re.split(r'\n(?=##\s*\[)', log_txt)
    added_info = {}
    order = 1
    for sec in sections:
        date_m = re.search(r'##\s*\[(\d{4}-\d{2}-\d{2})', sec)
        date_str = date_m.group(1) if date_m else '2026-09-12'
        matches = re.findall(r'(?:wiki/books/([a-zA-Z0-9_\-]+)\.md|\[\[([a-zA-Z0-9_\-]+)\]\])', sec)
        for m in matches:
            slug = m[0] or m[1]
            book_path = os.path.join(wiki_dir, 'books', f'{slug}.md')
            if os.path.exists(book_path):
                if slug not in added_info:
                    added_info[slug] = {
                        "order": order,
                        "date": date_str
                    }
                    order += 1
    return added_info

def parse_markdown_files():
    base_dir = get_base_dir()
    wiki_dir = os.path.join(base_dir, 'wiki')
    added_info = parse_log_added_info(wiki_dir)
    
    books = []
    authors = {}
    genres = {}
    themes = {}
    
    # 1. Parse Authors
    for f in glob.glob(os.path.join(wiki_dir, 'authors', '*.md')):
        slug = os.path.basename(f).replace('.md', '')
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
            
        name_m = re.search(r'^#\s*Author:\s*(.*)', txt, re.MULTILINE)
        name = name_m.group(1).strip() if name_m else slug.replace('-', ' ').title()
        
        eras_m = re.search(r'\*\*Eras / Movements\*\*:\s*(.*)', txt)
        eras = eras_m.group(1).strip() if eras_m else ""
        
        genres_m = re.search(r'\*\*Primary Genres\*\*:\s*(.*)', txt)
        author_genres = genres_m.group(1).strip() if genres_m else ""
        
        bio_m = re.search(r'## Biography & Context\s*\n(.*?)(?=\n##|$)', txt, re.DOTALL)
        bio = bio_m.group(1).strip() if bio_m else ""
        
        themes_m = re.search(r'## Recurring Themes\s*\n(.*)', txt, re.DOTALL)
        rec_themes = themes_m.group(1).strip() if themes_m else ""
        
        authors[slug] = {
            "slug": slug,
            "name": name,
            "eras": eras,
            "genres": author_genres,
            "bio": bio,
            "recurring_themes": rec_themes
        }
        
    # 2. Parse Genres
    for f in glob.glob(os.path.join(wiki_dir, 'genres', '*.md')):
        slug = os.path.basename(f).replace('.md', '')
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
            
        name_m = re.search(r'^#\s*Genre:\s*(.*)', txt, re.MULTILINE)
        name = name_m.group(1).strip() if name_m else slug.replace('-', ' ').title()
        
        desc_m = re.search(r'\*\*Description\*\*:\s*(.*)', txt)
        desc = desc_m.group(1).strip() if desc_m else ""
        
        overview_m = re.search(r'## Overview & Scope\s*\n(.*?)(?=\n##|$)', txt, re.DOTALL)
        overview = overview_m.group(1).strip() if overview_m else ""
        
        genres[slug] = {
            "slug": slug,
            "name": name,
            "description": desc,
            "overview": overview
        }
        
    # 3. Parse Themes
    for f in glob.glob(os.path.join(wiki_dir, 'themes', '*.md')):
        slug = os.path.basename(f).replace('.md', '')
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
            
        name_m = re.search(r'^#\s*Theme:\s*(.*)', txt, re.MULTILINE)
        name = name_m.group(1).strip() if name_m else slug.replace('-', ' ').title()
        
        summary_m = re.search(r'\*\*Summary\*\*:\s*(.*)', txt)
        summary = summary_m.group(1).strip() if summary_m else ""
        
        synthesis_m = re.search(r'## Synthesis\s*\n(.*?)(?=\n##|$)', txt, re.DOTALL)
        synthesis = synthesis_m.group(1).strip() if synthesis_m else ""
        
        themes[slug] = {
            "slug": slug,
            "name": name,
            "summary": summary,
            "synthesis": synthesis
        }
        
    # 4. Parse Books
    for f in glob.glob(os.path.join(wiki_dir, 'books', '*.md')):
        slug = os.path.basename(f).replace('.md', '')
        with open(f, 'r', encoding='utf-8') as fp:
            txt = fp.read()
            
        title_m = re.search(r'^#\s*(.*)', txt, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else slug.replace('-', ' ').title()
        
        authors_m = re.search(r'\*\*Author\(s\)\*\*:\s*(.*)', txt)
        authors_str = authors_m.group(1).strip() if authors_m else ""
        book_author_slugs = re.findall(r'\[\[(.*?)\]\]', authors_str)
        
        genres_m = re.search(r'\*\*Genre\(s\)\*\*:\s*(.*)', txt)
        genres_str = genres_m.group(1).strip() if genres_m else ""
        book_genre_slugs = re.findall(r'\[\[(.*?)\]\]', genres_str)
        
        themes_m = re.search(r'\*\*Key Themes\*\*:\s*(.*)', txt)
        themes_str = themes_m.group(1).strip() if themes_m else ""
        book_theme_slugs = re.findall(r'\[\[(.*?)\]\]', themes_str)
        
        source_m = re.search(r'\*\*Source\*\*:\s*(.*)', txt)
        source = source_m.group(1).strip() if source_m else ""
        
        updated_m = re.search(r'\*\*Last updated\*\*:\s*(.*)', txt)
        last_updated = updated_m.group(1).strip() if updated_m else ""
        
        # Year extraction
        pub_year_m = re.search(r'\*\*Publication(?:\s*Year)?\*\*:[^\n]*?\b(19\d\d|20\d\d)\b', txt)
        if pub_year_m:
            year = int(pub_year_m.group(1))
        elif "21st" in slug or "deterrence" in slug:
            year = 2021
        elif "cooperation" in slug:
            year = 1984
        else:
            year_match = re.search(r'\b(19\d\d|20\d\d)\b', txt)
            year = int(year_match.group(1)) if year_match else 2026
            
        exec_m = re.search(r'## Executive Summary\s*\n(.*?)(?=\n##|$)', txt, re.DOTALL)
        exec_summary = exec_m.group(1).strip() if exec_m else ""
        
        chapters_m = re.search(r'## Key Arguments / Chapter Breakdown\s*\n(.*?)(?=\n##|$)', txt, re.DOTALL)
        chapters_raw = chapters_m.group(1).strip() if chapters_m else ""
        
        quotes_m = re.search(r'## Key Quotes & Citations\s*\n(.*?)(?=\n##|$)', txt, re.DOTALL)
        quotes_raw = quotes_m.group(1).strip() if quotes_m else ""
        
        thematic_m = re.search(r'## Thematic Connections\s*\n(.*?)(?=\n##|$)', txt, re.DOTALL)
        thematic_raw = thematic_m.group(1).strip() if thematic_m else ""
        
        related_m = re.search(r'## Related pages\s*\n(.*)', txt, re.DOTALL)
        related_raw = related_m.group(1).strip() if related_m else ""
        
        book_added = added_info.get(slug, {"order": len(books) + 1, "date": last_updated or "2026-09-12"})
        
        books.append({
            "slug": slug,
            "title": title,
            "year": year,
            "added_order": book_added["order"],
            "added_date": book_added["date"],
            "authors_str": authors_str,
            "author_slugs": book_author_slugs,
            "genres_str": genres_str,
            "genre_slugs": book_genre_slugs,
            "themes_str": themes_str,
            "theme_slugs": book_theme_slugs,
            "source": source,
            "last_updated": last_updated,
            "exec_summary": exec_summary,
            "chapters_raw": chapters_raw,
            "quotes_raw": quotes_raw,
            "thematic_raw": thematic_raw,
            "related_raw": related_raw,
            "full_content": txt
        })
        
    # Sort books newest on top (by publication year descending, then title)
    books.sort(key=lambda b: (b["year"], b["title"]), reverse=True)
    
    wiki_payload = {
        "title": "Gilgamis LLM Wiki",
        "last_updated": "2026-09-12",
        "books": books,
        "authors": authors,
        "genres": genres,
        "themes": themes
    }
    
    return wiki_payload

def build():
    base_dir = get_base_dir()
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(cur_dir, '..', 'resources', 'dashboard_template.html')
    
    payload = parse_markdown_files()
    
    # 1. Write dashboard data JSON
    json_path = os.path.join(base_dir, 'wiki', 'dashboard_data.json')
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"Wrote data JSON to {json_path}")
    
    # 2. Load template and embed JSON
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
        
    embedded_json = json.dumps(payload, ensure_ascii=False, indent=2)
    html_content = template_content.replace('/*__WIKI_DATA__*/', embedded_json)
    
    output_locations = [
        os.path.join(base_dir, 'index.html'),
        os.path.join(base_dir, 'dashboard.html'),
        os.path.join(base_dir, 'wiki', 'index.html'),
        os.path.join(base_dir, 'wiki', 'dashboard.html'),
        os.path.join(base_dir, '.agents', 'skills', 'gilgamis-llm-wiki', 'resources', 'index.html'),
        os.path.join(base_dir, '.agents', 'skills', 'gilgamis-llm-wiki', 'resources', 'dashboard.html')
    ]
    
    for loc in output_locations:
        os.makedirs(os.path.dirname(loc), exist_ok=True)
        with open(loc, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"Generated HTML dashboard: {loc}")

if __name__ == '__main__':
    build()
