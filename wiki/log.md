# Gilgamis LLM Wiki — Ingestion & Operations Log

This file provides an append-only historical audit log of all book ingestions, conceptual syntheses, wiki structural updates, and maintenance operations.

---

## [2026-08-23T19:12:00+02:00] Initial Wiki Scaffolding & Ingestion of Library

### 1. Ingestion: *The Evolution of Cooperation*
- **Book Title**: *The Evolution of Cooperation*
- **Author(s)**: Robert Axelrod (Chapter 5 co-authored with William D. Hamilton)
- **Source File**: `raw/Axelrod_Robert_The_Evolution_of_Cooperation.pdf`
- **Pages**: 243
- **Pages Created / Updated**:
  - `wiki/books/the-evolution-of-cooperation.md`
  - `wiki/authors/robert-axelrod.md`
  - `wiki/authors/william-d-hamilton.md`
  - `wiki/genres/game-theory.md`
  - `wiki/genres/political-science.md`
  - `wiki/genres/evolutionary-biology.md`
  - `wiki/themes/cooperation-and-reciprocity.md`
  - `wiki/themes/tit-for-tat.md`
  - `wiki/themes/shadow-of-the-future.md`
  - `wiki/themes/evolution-of-strategies.md`
  - `wiki/themes/rationality-and-decision-making.md`

### 2. Ingestion: *Deterrence in the 21st Century — Insights from Theory and Practice*
- **Book Title**: *Deterrence in the 21st Century — Insights from Theory and Practice* (NL ARMS 2020)
- **Editors**: Frans Osinga, Tim Sweijs
- **Contributors**: Lawrence Freedman, Michael J. Mazarr, Sten Rynning, Karl Mueller, Alexey Arbatov, Paul van Hooft, Jörg Noll, Osman Bojang, Sebastiaan Rietjens, Dmitry Adamsky, Dean Cheng, Nori Katagiri, Sander Ruben Aarten, Hassan Ahmadian, Payam Mohseni, Eitan Shamir, Martijn Kitzen, Christina van Kuijck, Maarten Rothman, Peter Viggo Jakobsen, Francesco Giumelli, Cees van Doorn, Theo Brinkel, Stefan Soesanto, Max Smeets, Alex Wilner, Casey Babb, Roy Lindelauf, Tom Bijlsma, Samuel Zilincik, Isabelle Duyvesteyn, Paul Ducheine, Peter Pijpers
- **Source File**: `raw/Deterrence in 21st Century Nuclear NetherlandsAnnualReviewO.pdf`
- **Pages**: 538 (26 Chapters across 6 Parts)
- **Pages Created / Updated**:
  - `wiki/books/deterrence-in-the-21st-century.md`
  - `wiki/authors/frans-osinga.md`
  - `wiki/authors/tim-sweijs.md`
  - `wiki/authors/lawrence-freedman.md`
  - `wiki/authors/michael-mazarr.md`
  - `wiki/authors/dmitry-adamsky.md`
  - `wiki/authors/dean-cheng.md`
  - `wiki/authors/karl-mueller.md`
  - `wiki/authors/alexey-arbatov.md`
  - `wiki/authors/sten-rynning.md`
  - `wiki/authors/paul-van-hooft.md`
  - `wiki/authors/jorg-noll.md`
  - `wiki/authors/eitan-shamir.md`
  - `wiki/authors/martijn-kitzen.md`
  - `wiki/authors/francesco-giumelli.md`
  - `wiki/authors/stefan-soesanto.md`
  - `wiki/authors/max-smeets.md`
  - `wiki/authors/alex-wilner.md`
  - `wiki/authors/roy-lindelauf.md`
  - `wiki/authors/tom-bijlsma.md`
  - `wiki/authors/samuel-zilincik.md`
  - `wiki/authors/isabelle-duyvesteyn.md`
  - `wiki/authors/paul-ducheine.md`
  - `wiki/genres/strategic-studies.md`
  - `wiki/genres/military-science.md`
  - `wiki/genres/international-relations.md`
  - `wiki/genres/security-studies.md`
  - `wiki/themes/deterrence-and-coercion.md`
  - `wiki/themes/nuclear-strategy-and-strategic-stability.md`
  - `wiki/themes/cross-domain-conflict.md`
  - `wiki/themes/non-western-strategic-thought.md`
  - `wiki/themes/violent-non-state-actors.md`
  - `wiki/themes/hybrid-threats-and-cyber-warfare.md`

### 3. Master Index & System Architecture
- **Master Index**: `wiki/index.md` created with full tables of contents across Books, Authors, Genres, Themes, and Directory Architecture.
- **Verification**: Complete bidirectional link integrity check across all 46 wiki pages (0 broken links, 0 orphans).

---

## [2026-08-23T19:31:00+02:00] Skill Creation: Gilgamis LLM Wiki Interactive Dashboard

- **Skill Name**: `gilgamis-llm-wiki`
- **Location**: `.agents/skills/gilgamis-llm-wiki/`
- **Created Files**:
  - `.agents/skills/gilgamis-llm-wiki/SKILL.md` (Skill manifest & runbook)
  - `.agents/skills/gilgamis-llm-wiki/scripts/build_dashboard.py` (Data parser & HTML generator)
  - `.agents/skills/gilgamis-llm-wiki/scripts/serve_dashboard.py` (Local HTTP server with browser launcher)
  - `.agents/skills/gilgamis-llm-wiki/resources/dashboard.html` (Standalone single-page dashboard application)
  - `.agents/skills/gilgamis-llm-wiki/references/dashboard_guide.md` (UI architecture & shortcut guide)
  - `dashboard.html` (Root-level interactive application for instant browser access)
  - `wiki/dashboard.html` & `wiki/dashboard_data.json`
- **Features Implemented**:
  - Sidebar with titles sorted newest on top (2021 first, then 1984).
  - Header filters for Genres and Themes with dynamic multi-criteria filtering.
  - Universal real-time search bar with keyboard shortcut (`/`).
  - Rich Main Pane rendering of selected book (hero card, executive summary, chapter breakdowns, quotes, thematic connections).
  - Interactive modals for instant preview of author biographies and cross-cutting thematic syntheses.
  - Dark/Light mode toggle.

---

## [2026-08-23T19:46:00+02:00] Dashboard Renaming to index.html & Pure Event Architecture

- **Primary Dashboard Endpoint**: Standardized dashboard filename to `index.html` across root, `wiki/`, and skill resources for standard web serving (while retaining `dashboard.html` aliases).
- **Template Separation**: Created `.agents/skills/gilgamis-llm-wiki/resources/dashboard_template.html` with pure JSON script-island data injection and dataset click handlers to guarantee zero JS syntax escaping anomalies.
- **Updated Files**:
  - `index.html` (Primary root dashboard app)
  - `wiki/index.html`
  - `.agents/skills/gilgamis-llm-wiki/resources/index.html`
  - `.agents/skills/gilgamis-llm-wiki/scripts/build_dashboard.py`
  - `.agents/skills/gilgamis-llm-wiki/scripts/serve_dashboard.py`
  - `README.md`, `SUMMARY.md`, `SKILL.md`, `references/dashboard_guide.md`

---

## [2026-09-12T19:15:00+02:00] Incoming Books Mount Integration, Git Ignore Sync Exclusion, and Test Ingestion of Art Folder

### 1. Ingestion Sources Architecture & Git Sync Exclusion
- **Mounted External Library Configured**: Added primary incoming library mount at `C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\` across system specification (`GilgamisLLMWiki.md`), `README.md`, `SKILL.md`, and master index (`wiki/index.md`).
- **Git Ignore Security**: Created `.gitignore` excluding `raw/`, incoming mounts (`BOOKS/`, `_GilgameshLibrary/`), and binary document formats (`*.pdf`, `*.epub`, etc.) from GitHub synchronization.
- **Git Tracking Cache Cleaned**: Staged exclusion of local raw files (`git rm -r --cached raw/`) while preserving 100% of physical files intact on local disk.

### 2. Test Ingestion: *Âşık Borani: Söz İnsanın Aynasıdır (Cilt I & II)*
- **Source Location**: `C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\Art\`
- **Files Ingested**: `73010,cilt1pdf.pdf` (Vol. 1, 564 pp.) and `73011,cilt2pdf.pdf` (Vol. 2, 586 pp.) — Total: 1,150 pages across 10 sections.
- **Author**: Âşık Borani (Halil Çimen, 1943–2020)
- **Editor & Compiler**: İbrahim Gösterir
- **Publisher**: T.C. Çorum Valiliği İl Kültür ve Turizm Müdürlüğü (Yayın No: 19, 2020)
- **Pages Created / Updated**:
  - `wiki/books/asik-borani-soz-insanin-aynasi.md` (Comprehensive book analysis covering all 10 sections with authentic textual citations)
  - `wiki/authors/asik-borani.md` (Full biography, lineage, poetic creed, cultural honors)
  - `wiki/authors/ibrahim-gosterir.md` (Folklorist, compiler, educator)
  - `wiki/genres/turkish-folk-literature.md`
  - `wiki/genres/anatolian-humanism.md`
  - `wiki/genres/poetry-and-poetics.md`
  - `wiki/themes/universal-love-and-human-dignity.md`
  - `wiki/themes/social-critique-and-moral-conscience.md`
  - `wiki/themes/asik-and-minstrel-tradition.md`
  - `wiki/themes/non-western-strategic-thought.md` (Updated with Anatolian humanist peace paradigm)
  - `wiki/themes/cooperation-and-reciprocity.md` (Updated with humanist moral cooperation dimension)
  - `wiki/themes/rationality-and-decision-making.md` (Updated with moral rationality vs opportunism)
  - `wiki/index.md` (Updated metrics: 3 books, 26 authors, 10 genres, 14 themes)

### 3. Dashboard Rebuild
- Enhanced `build_dashboard.py` year extraction logic.
- Rebuilt `wiki/dashboard_data.json` and generated standalone dashboard files (`index.html`, `dashboard.html`, `wiki/index.html`, `wiki/dashboard.html`).

