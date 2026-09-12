# Gilgamis LLM Wiki

A structured, interlinked personal knowledge base for cataloging, analyzing, and synthesizing a personal library of books, strategic literature, and archaeology, maintained by LLM agents based on Andrej Karpathy's LLM Wiki pattern.

---

## 📌 Quick Links

- 🖥️ **[Interactive Web Dashboard](http://127.0.0.1:8080/index.html)** — Live visual dashboard app (offline: [index.html](index.html)).
- 📋 **[Library Summary](SUMMARY.md)** — Standalone executive summary document.
- 🗂️ **[Master Wiki Index](wiki/index.md)** — Complete table of contents by Books, Authors, Genres, and Themes.
- 📖 **[System Specification](GilgamisLLMWiki.md)** — Architectural design, citation rules, and operational workflow.
- 📜 **[Operations & Ingestion Log](wiki/log.md)** — Append-only audit trail of ingestions and maintenance operations.

---

## 🖥️ Gilgamis LLM Wiki Interactive Dashboard

The repository includes a standalone, browser-based user interface (`index.html`) tailored for browsing, filtering, and cross-analyzing the knowledge base.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  GW  Gilgamis LLM Wiki [Dashboard]      [🔍 Search... (/)]  [All Genres ▾]  [All Themes ▾]  [🌙]│
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│ INGESTED TITLES      │ 📖 Cumhuriyet Dönemi Arkeoloji Politikaları ve Ekrem Akurgal    │
│ (Newest First)       │ Published 2024 · Source: BOOKS/Archeology/2023 CUMHURİYET...     │
│                      │ By Erdal Polat (discussing Ekrem Akurgal)                       │
│ [2024] Arkeoloji     │ Genres: [Archaeological Historiography] [Anatolian Civilizations]│
│  Politikaları        │ Themes: [Archaeology & National Identity] [Critique of Dogma]   │
│                      ├─────────────────────────────────────────────────────────────────┤
│ [2021] Deterrence    │ ℹ️ Executive Summary                                            │
│  in 21st Century     │ Historical investigation into Atatürk's 'Scientific Republic'   │
│                      │ and the founding of the Anatolian Civilizations Synthesis...    │
│ [2020] Söz İnsanın   ├─────────────────────────────────────────────────────────────────┤
│  Aynasıdır           │ 📑 Key Arguments & Chapter Breakdown                            │
│                      │ • TTK, DTCF, and the First National Excavations (Ahlatlıbel)... │
│ [2019] America       │ • Atatürk's "Sparks and Volcanoes" directive to Europe...       │
│  Before              │ • Akurgal's Smyrna excavations overturning Eurocentrism...      │
│                      ├─────────────────────────────────────────────────────────────────┤
│ [2015] Magicians     │ 💬 Key Quotes & Page Citations                                  │
│  of the Gods         │ 🔗 Thematic Connections & Dialogues                             │
└──────────────────────┴─────────────────────────────────────────────────────────────────┘
```

### Dashboard Features
- **Collapsible Sidebar & Mobile Drawer**: Collapsible left banner via header toggle button (`☰`) or hotkey (`Ctrl+B`). On mobile screens, automatically collapses into an overlay slide-out drawer with backdrop blur, auto-closing upon book selection for seamless phone and tablet reading.
- **Sidebar (Sortable: Newest First & Newest Added)**: Toggle between **Newest First** (publication year, 2024 down to 1984) and **Newest Added** (ingestion chronological order, newest batches on top), with reversible ascending/descending directions, matching book counter badge, and persistent preferences in `localStorage`.
- **Header Filters**: Live multi-criteria dropdown filtering for **Genres** (20 categories) and **Themes** (28 categories).
- **Universal Search Bar**: Real-time fuzzy search across titles, authors, executive summaries, chapter notes, and quotes. *(Press `/` anywhere to focus)*.
- **Main Pane (Selected Book View)**: Complete structured book view with hero metadata, executive summaries, chapter breakdowns, quote cards with exact page citations, and thematic connections.
- **Interactive Entity Modals**: Click any author or theme link across the UI to open an instant modal with full biographical context or cross-cutting thematic syntheses without losing your place.
- **Dark / Light Theme Toggle**: Instant transition between dark and light themes.

### Running the Dashboard App

1. **Launch Local Server with Auto-Launch Browser**:
   ```powershell
   python .agents/skills/gilgamis-llm-wiki/scripts/serve_dashboard.py
   ```
   *Serves at `http://127.0.0.1:8080/index.html`.*

2. **Direct Offline Browser Access**:
   Double-click **[index.html](index.html)** in the repository root to run directly in any browser with zero dependencies.

3. **Rebuild Data after Ingesting New Books**:
   ```powershell
   python .agents/skills/gilgamis-llm-wiki/scripts/build_dashboard.py
   ```

---

## 📊 Knowledge Base Metrics

- **Total Ingested Works**: 14 distinct intellectual works (across 16 volumes and ~7,500 pages)
- **Total Maintained Wiki Pages**: 104 interlinked markdown documents
- **Book Analyses**: 14 ([wiki/books/](wiki/books/))
- **Author Profiles**: 34 ([wiki/authors/](wiki/authors/))
- **Genre Indices**: 20 ([wiki/genres/](wiki/genres/))
- **Thematic Syntheses**: 28 ([wiki/themes/](wiki/themes/))
- **Bidirectional Link Integrity**: 100% (0 broken `[[...]]` links, 0 orphaned pages)
- **Source Integrity**: Strict textual citations referencing exact source files and page numbers; source libraries (`BOOKS/` and `raw/`) remain immutable and are excluded from GitHub synchronization via `.gitignore`.

---

## 📚 Complete Ingested Library Catalog

| Year | Title | Author(s) | Primary Genres | Core Themes |
| :--- | :--- | :--- | :--- | :--- |
| **2024** | [[cumhuriyet-donemi-arkeoloji-politikalari-ve-ekrem-akurgal]] | [[erdal-polat]] | [[archaeological-historiography]], [[anatolian-civilizations]] | [[archaeology-and-national-identity]], [[critique-of-academic-orthodoxy]] |
| **2021** | [[deterrence-in-the-21st-century]] | [[frans-osinga]], [[tim-sweijs]] (eds.) | [[strategic-studies]], [[military-science]], [[game-theory]] | [[deterrence-and-coercion]], [[nuclear-strategy-and-strategic-stability]], [[cross-domain-conflict]] |
| **2020** | [[asik-borani-soz-insanin-aynasi]] | [[asik-borani]], [[ibrahim-gosterir]] (ed.) | [[turkish-folk-literature]], [[anatolian-humanism]], [[poetry-and-poetics]] | [[universal-love-and-human-dignity]], [[social-critique-and-moral-conscience]], [[asik-and-minstrel-tradition]] |
| **2019** | [[america-before-the-key-to-earths-lost-civilization]] | [[graham-hancock]] | [[alternative-archaeology]], [[pre-columbian-history]], [[archaeoastronomy]] | [[pre-clovis-and-american-antiquity]], [[lost-civilization-hypothesis]], [[younger-dryas-impact-hypothesis]] |
| **2015** | [[magicians-of-the-gods]] | [[graham-hancock]] | [[alternative-archaeology]], [[catastrophism]], [[archaeoastronomy]] | [[younger-dryas-impact-hypothesis]], [[lost-civilization-hypothesis]], [[catastrophism-and-earth-history]] |
| **2013** | [[war-god-nights-of-the-witch]] | [[graham-hancock]] | [[historical-fiction]], [[speculative-fiction]], [[epic-narrative]] | [[altered-states-and-origin-of-art]], [[clash-of-civilizations]], [[fanaticism-and-human-sacrifice]] |
| **2011** | [[the-master-game]] | [[graham-hancock]], [[robert-bauval]] | [[esoteric-history]], [[occult-studies]], [[hermeticism]] | [[hermetic-tradition-and-secret-societies]], [[orion-correlation-and-sacred-astronomy]] |
| **2010** | [[lost-knowledge-of-the-ancients]] | [[glenn-kreisberg]] (ed.) | [[alternative-archaeology]], [[esoteric-history]], [[archaeoastronomy]] | [[critique-of-academic-orthodoxy]], [[lost-civilization-hypothesis]], [[submerged-ruins-and-sea-level-rise]] |
| **2005** | [[supernatural-meetings-with-the-ancient-teachers-of-mankind]] | [[graham-hancock]] | [[anthropology-of-consciousness]], [[alternative-archaeology]], [[shamanism]] | [[altered-states-and-origin-of-art]], [[lost-civilization-hypothesis]], [[critique-of-academic-orthodoxy]] |
| **2002** | [[underworld-mysterious-origins-of-civilization]] | [[graham-hancock]] | [[alternative-archaeology]], [[paleoclimatology]], [[investigative-non-fiction]] | [[submerged-ruins-and-sea-level-rise]], [[catastrophism-and-earth-history]], [[lost-civilization-hypothesis]] |
| **1998** | [[the-mars-mystery]] | [[graham-hancock]], [[robert-bauval]], [[john-grigsby]] | [[planetary-science-speculation]], [[alternative-archaeology]], [[catastrophism]] | [[planetary-cataclysm-and-cosmic-impacts]], [[catastrophism-and-earth-history]], [[lost-civilization-hypothesis]] |
| **1996** | [[keeper-of-genesis]] | [[graham-hancock]], [[robert-bauval]] | [[archaeoastronomy]], [[alternative-archaeology]], [[esoteric-history]] | [[orion-correlation-and-sacred-astronomy]], [[lost-civilization-hypothesis]], [[critique-of-academic-orthodoxy]] |
| **1995** | [[fingerprints-of-the-gods]] | [[graham-hancock]] | [[alternative-archaeology]], [[archaeoastronomy]], [[investigative-non-fiction]] | [[lost-civilization-hypothesis]], [[catastrophism-and-earth-history]], [[orion-correlation-and-sacred-astronomy]] |
| **1984** | [[the-evolution-of-cooperation]] | [[robert-axelrod]], [[william-d-hamilton]] | [[game-theory]], [[political-science]], [[evolutionary-biology]] | [[cooperation-and-reciprocity]], [[shadow-of-the-future]], [[evolution-of-strategies]], [[tit-for-tat]] |

---

## 🗂️ Complete Wiki Directory Map

```
GilgamisLLMWiki/
├── [Mounted External Library]                      # C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\
│   ├── Archeology/                                # Ingested: 11 landmark works (13 PDF volumes, ~5,500 pp.)
│   ├── Art/                                       # Ingested: Âşık Borani: Söz İnsanın Aynasıdır (2 Vols., 1,150 pp.)
│   └── AI/, History_/, Philosophy..., ...         # 40+ domain libraries (immutable, git-ignored)
├── .gitignore                                     # Excludes raw/, BOOKS/, and PDF binaries from GitHub sync
├── raw/                                           # Immutable local staging documents (git-ignored)
│   ├── Axelrod_Robert_The_Evolution_of_Cooperation.pdf
│   └── Deterrence in 21st Century Nuclear NetherlandsAnnualReviewO.pdf
├── wiki/                                          # Maintained knowledge base (104 markdown pages)
│   ├── index.md                                   # Master index & full TOC
│   ├── log.md                                     # Ingestion & audit changelog
│   ├── index.html                                 # Dashboard web application copy
│   ├── dashboard_data.json                        # Structured JSON export
│   ├── books/                                     # Ingested book detail pages (14 pages)
│   ├── authors/                                   # Author profile pages (34 pages)
│   ├── genres/                                    # Genre index pages (20 pages)
│   └── themes/                                    # Core thematic concept pages (28 pages)
├── .agents/skills/gilgamis-llm-wiki/              # Agent skill definition & tooling
│   ├── SKILL.md                                   # Skill runbook & manifest
│   ├── scripts/
│   │   ├── build_dashboard.py                     # Data parsing & HTML generator
│   │   └── serve_dashboard.py                     # Local web server launcher
│   ├── resources/
│   │   ├── index.html                             # Self-contained dashboard app
│   │   └── dashboard_template.html                # Clean HTML template
│   └── references/
│       └── dashboard_guide.md                     # Feature & shortcut manual
├── index.html                                     # 1-Click offline dashboard
├── SUMMARY.md                                     # Executive summary document
└── GilgamisLLMWiki.md                             # LLM Wiki design specification
```

---

## 📜 Maintenance & Citation Rules

- **Source Immutability**: Source files in `raw/` and the mounted `BOOKS/` library must never be altered or overwritten.
- **Git Sync Exclusion**: All raw and incoming book directories and binary formats are excluded from GitHub sync via `.gitignore`.
- **Naming Conventions**: All wiki files are lowercase with hyphens (e.g., `the-evolution-of-cooperation.md`).
- **Bidirectional Wiki Links**: Every page links to relevant concepts using `[[page-name]]` format.
- **Citation Format**: Every factual assertion and direct quote must cite its source and page/chapter (e.g., `(source: BOOKS/Archeology/Graham Hancock 13 Magicians of the Gods.pdf, ch. 1, p. 11)`).
- **Index & Log Tracking**: Every addition or modification must update `wiki/index.md` and append an entry to `wiki/log.md`.
