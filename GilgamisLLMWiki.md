

Markdown  
\# Gilgamis LLM Wiki

A personal book and literary knowledge base maintained by Claude Code / LLM.  
Based on Andrej Karpathy's LLM Wiki pattern.

\#\# Purpose

This wiki is a structured, interlinked knowledge base for cataloging, analyzing, and synthesizing a personal library of books.  
The LLM maintains the wiki, while the user provides raw book files, discusses literary frameworks, asks cross-book questions, and guides thematic analysis.

\#\# Folder structure

raw/ \-- source book files (EPUB, PDF, TXT, MD) (immutable \-- never modify these)  
wiki/ \-- markdown pages maintained by the LLM  
wiki/books/ \-- book summary and detail pages (e.g., epic-of-gilgamesh.md)  
wiki/authors/ \-- author profile pages (e.g., hermann-hesse.md)  
wiki/genres/ \-- genre index pages (e.g., speculative-fiction.md)  
wiki/themes/ \-- core thematic concept pages (e.g., mortality-and-legacy.md)  
wiki/index.md \-- master index and table of contents sorted by Genre, Theme, and Author  
wiki/log.md \-- append-only record of all ingestions and operations

\#\# Ingest workflow

When a new book or document is added to \`raw/\` and requested for ingestion:

1\. Read the full source document or chapter breakdown.  
2\. Discuss key takeaways, core themes, and genre classifications with the user before writing.  
3\. Create a dedicated book page in \`wiki/books/\<book-title\>.md\`.  
4\. Create or update author page(s) in \`wiki/authors/\<author-name\>.md\`.  
5\. Create or update genre page(s) in \`wiki/genres/\<genre-name\>.md\`.  
6\. Create or update theme concept pages in \`wiki/themes/\<theme-name\>.md\`, cross-referencing ideas from other books in the library.  
7\. Add bidirectional wiki-links (\`\[\[page-name\]\]\`) connecting books, authors, genres, and themes.  
8\. Update \`wiki/index.md\` with the new book, linked under its respective authors, genres, and themes.  
9\. Append an entry to \`wiki/log.md\` with the timestamp, book title, author, and all updated pages.

A single book ingestion will touch 8–15 wiki pages across \`books/\`, \`authors/\`, \`genres/\`, and \`themes/\`.

\#\# Page formats

\#\#\# 1\. Book Page (\`wiki/books/\<title\>.md\`)

\`\`\`markdown  
\# Book Title

\*\*Author(s)\*\*: \[\[author-name\]\]  
\*\*Genre(s)\*\*: \[\[genre-1\]\], \[\[genre-2\]\]  
\*\*Key Themes\*\*: \[\[theme-1\]\], \[\[theme-2\]\], \[\[theme-3\]\]  
\*\*Source\*\*: raw/filename.pdf  
\*\*Last updated\*\*: YYYY-MM-DD

\---

\#\# Executive Summary  
One to two paragraphs summarizing the core thesis, narrative arc, or primary subject.

\#\# Key Arguments / Chapter Breakdown  
Detailed notes, chapter takeaways, character arcs, or central arguments.

\#\# Key Quotes & Citations  
\- "Notable quote from the text." (source: filename.pdf, p. 45\)

\#\# Thematic Connections  
How this work dialogues with other books in the wiki (e.g., contrasts with \[\[another-book\]\]).

\#\# Related pages  
\- \[\[author-name\]\]  
\- \[\[theme-1\]\]  
\- \[\[genre-1\]\]

### **2\. Theme Page (wiki/themes/\<theme-name\>.md)**

Markdown  
\# Theme: Mortality and Legacy

**\*\*Summary\*\***: Exploration of how human impermanence shapes societal drive, heroics, and existential philosophy.  
**\*\*Last updated\*\***: YYYY-MM-DD

\---

\#\# Synthesis  
Cross-cutting analysis of how different authors and works treat this theme across eras.

\#\# Featured Works  
\- \[\[epic-of-gilgamesh\]\] — Journey from terror of death to civic legacy.  
\- \[\[meditations\]\] — Stoic acceptance of natural transience.

\#\# Key Authors & Perspectives  
\- \[\[marcus-aurelius\]\]  
\- \[\[unknown-babylonian-scribe\]\]

\#\# Related themes & genres  
\- \[\[existentialism\]\]  
\- \[\[philosophical-fiction\]\]

### **3\. Author Page (wiki/authors/\<author-name\>.md)**

Markdown  
\# Author: Name

**\*\*Eras / Movements\*\***: \[\[literary-movement\]\]  
**\*\*Primary Genres\*\***: \[\[genre-1\]\]  
**\*\*Last updated\*\***: YYYY-MM-DD

\---

\#\# Biography & Context  
Brief context on historical era, philosophy, and literary significance.

\#\# Books in Wiki  
\- \[\[book-1\]\] (Year)  
\- \[\[book-2\]\] (Year)

\#\# Recurring Themes  
\- \[\[theme-1\]\]  
\- \[\[theme-2\]\]

## **Citation rules**

* Every factual claim, summary assertion, or direct quote must reference its source file and page/chapter where possible (format: (source: filename.epub, ch. 4)).  
* If critical analyses or historical accounts disagree on an interpretation or translation, note the distinction explicitly.  
* Mark unverified textual assumptions as \[verification needed\].

## **Question answering & exploration**

When the user asks a question (e.g., *"How do my ingested books define leadership?"* or *"Compare author X and Y on existential dread"*):

> 1. Read wiki/index.md to locate relevant book, theme, and author pages.  
> 2. Read the corresponding detail pages across wiki/themes/, wiki/books/, and wiki/authors/.  
> 3. Synthesize a cross-comparative answer citing specific wiki pages and sources.  
> 4. If a valuable new synthesis or comparison emerges, offer to file it as a new page in wiki/themes/.

## **Lint & maintenance**

When asked to audit or lint the wiki:

* Find orphan books, authors, or themes (pages with zero inbound links).  
* Identify themes or genres mentioned in book notes that lack dedicated pages in wiki/themes/ or wiki/genres/.  
* Check for missing metadata fields (Author, Genre, Themes, Source) across all book entries.  
* Validate that wiki/index.md reflects all entries in subdirectories\[cite: 1\].  
* Report findings as a structured checklist with recommended automated fixes\[cite: 1\].

## **Rules**

* **Never modify anything in the raw/ directory**\[cite: 1\].  
* Always keep filenames lowercase with hyphens (e.g., the-brothers-karamazov.md)\[cite: 1\].  
* Always update wiki/index.md and wiki/log.md whenever pages are added or modified\[cite: 1\].  
* Keep classification flexible: if a book spans multiple genres or novel themes, confirm categorizations with the user during ingestion\[cite: 1\].

\<ElicitationsGroup message="Next steps to set up and run your Gilgamis LLM Wiki:"\>  
  \<Elicitation label="Generate a starting wiki/index.md template for books" query="Generate a complete template for wiki/index.md organizing books by themes, genres, and authors."/\>  
  \<Elicitation label="Create a CLI shell script to scaffold the Gilgamis wiki directory structure" query="Write a bash script to scaffold the raw/, wiki/books/, wiki/authors/, wiki/genres/, and wiki/themes/ directory structure along with empty log.md and index.md files."/\>  
\</ElicitationsGroup\>  
