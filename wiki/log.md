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
