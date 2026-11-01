# Gilgamis LLM Wiki

A structured, interlinked personal knowledge base for cataloging, analyzing, and synthesizing a personal library of books, strategic literature, democracy studies, evolutionary biology, and archaeology, maintained by LLM agents (including local Ollama `qwen3.8:latest`) based on Andrej Karpathy's LLM Wiki pattern.

---

## 📌 Quick Links

- 🖥️ **[Interactive Web Dashboard](http://127.0.0.1:8080/index.html)** — Live visual dashboard app (offline: [index.html](index.html)).
- 📋 **[Library Summary](SUMMARY.md)** — Standalone executive summary document.
- 🗂️ **[Master Wiki Index](wiki/index.md)** — Complete table of contents by Books, Authors, Genres, and Themes.
- 📖 **[System Specification](GilgamisLLMWiki.md)** — Architectural design, citation rules, and operational workflow.
- 📜 **[Operations & Ingestion Log](wiki/log.md)** — Append-only audit trail of ingestions and maintenance operations.
- 🤖 **[Local Ollama (`qwen3.8`) Agent CLI](.agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py)** — Local `qwen3.8:latest` (27.3B, 262k context, Vision OCR) ingestion, query, and audit tool.

---

## 🖥️ Gilgamis LLM Wiki Interactive Dashboard

The repository includes a standalone, browser-based user interface (`index.html`) tailored for browsing, filtering, and cross-analyzing the knowledge base.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│  GW  Gilgamis LLM Wiki [Dashboard]      [🔍 Search... (/)]  [All Genres ▾]  [All Themes ▾]  [🌙]│
├──────────────────────┬─────────────────────────────────────────────────────────────────┤
│ INGESTED TITLES      │ 📖 Chip War: The Fight for the World's Most Critical Technology │
│ (Newest First)       │ Published 2022 · Source: BOOKS/Semiconductors/Chip War...       │
│                      │ By Chris Miller (analyzing Morris Chang)                        │
│ [2026] Influencing   │ Genres: [Strategic Studies] [Security Studies] [Military Sci]   │
│  Leaders             │ Themes: [Semiconductor Geopolitics] [Deterrence & Coercion]     │
│                      ├─────────────────────────────────────────────────────────────────┤
│ [2026] Adaptability  │ ℹ️ Executive Summary                                            │
│  Advantage           │ Chronicles how the integrated circuit replaced oil and steel    │
│                      │ as the master strategic resource of modern economic & AI power..│
│ [2022] Chip War      ├─────────────────────────────────────────────────────────────────┤
│                      │ 📑 Key Arguments & Chapter Breakdown                            │
│ [2017] Developing    │ • Bell Labs, Fairchild, Texas Instruments & Pentagon Offsets... │
│  the Super Soldier   │ • Morris Chang's pure-play foundry at TSMC & ASML EUV...        │
│                      │ • Weaponized interdependence & The Taiwan Dilemma...            │
│ [1840] Democracy     ├─────────────────────────────────────────────────────────────────┤
│  in America          │ 💬 Key Quotes & Page Citations                                  │
│                      │ 🔗 Thematic Connections & Dialogues                             │
└──────────────────────┴─────────────────────────────────────────────────────────────────┘
```

### Dashboard & Local Ollama (`qwen3.8`) Workflow

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

4. **Local Ollama (`qwen3.8:latest`) Agentic Ingestion, Vision OCR & Query CLI**:
   ```powershell
   # Check local Ollama server, qwen3.8 model specs, and wiki metrics
   python .agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py status

   # Extract PDF text (with automatic qwen3.8 Vision OCR fallback for scanned PDFs)
   python .agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py extract "<path-to-pdf>"

   # Ingest a book/article via local qwen3.8 and rebuild dashboard
   python .agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py ingest "<path-to-pdf>" --write --rebuild

   # Run cross-book synthesis queries using local qwen3.8
   python .agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py query "How do our ingested books connect game theory, democracy, and adaptive leadership?"

   # Audit wiki bidirectional link integrity and index completeness
   python .agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py audit
   ```

---

## 📊 Knowledge Base Metrics

- **Total Ingested Works**: 29 distinct intellectual works (across 33 volumes and ~11,200 pages)
- **Total Maintained Wiki Pages**: 170 interlinked markdown documents (168 entity pages + `index.md` & `log.md`)
- **Book Analyses**: 29 ([wiki/books/](wiki/books/))
- **Author Profiles**: 64 ([wiki/authors/](wiki/authors/))
- **Genre Indices**: 34 ([wiki/genres/](wiki/genres/))
- **Thematic Syntheses**: 41 ([wiki/themes/](wiki/themes/))
- **Bidirectional Link Integrity**: 100% (0 broken `[[...]]` links, 0 orphaned pages, 0 unindexed pages)
- **Source Integrity**: Strict textual citations referencing exact source files and page numbers; source libraries (`BOOKS/`, `ARTICLES-REPORTS/`, and `raw/`) remain immutable and are excluded from GitHub synchronization via `.gitignore`.

---

## 📚 Complete Ingested Library Catalog

| Year | Title | Author(s) | Primary Genres | Core Themes |
| :--- | :--- | :--- | :--- | :--- |
| **2026** | [[influencing-leaders]] | [[james-e-lukaszewski]], [[helio-fred-garcia]] | [[strategic-communication]], [[leadership-and-management]], [[strategic-studies]] | [[trusted-strategic-advisors-and-influence]], [[rationality-and-decision-making]], [[cooperation-and-reciprocity]] |
| **2026** | [[the-adaptability-advantage]] | [[john-sanei]] | [[leadership-and-management]], [[organizational-psychology]], [[anthropology-of-consciousness]] | [[adaptive-intelligence-and-organizational-resilience]], [[human-centered-ai-and-augmented-leadership]], [[evolution-of-human-consciousness]] |
| **2026** | [[rapid-reculturing]] | [[alex-bailey]], [[kerri-oneill]] | [[organizational-psychology]], [[leadership-and-management]] | [[organizational-culture-and-rewilding]], [[adaptive-intelligence-and-organizational-resilience]], [[human-centered-ai-and-augmented-leadership]] |
| **2026** | [[leading-for-tomorrow]] | [[scott-barry-kaufman]], [[chris-shipley]] (eds.), [[rita-mcgrath]] | [[leadership-and-management]], [[organizational-psychology]], [[strategic-studies]] | [[human-centered-ai-and-augmented-leadership]], [[adaptive-intelligence-and-organizational-resilience]], [[organizational-culture-and-rewilding]] |
| **2026** | [[valuable-and-visible]] | [[vanessa-errecarte]] | [[strategic-communication]], [[leadership-and-management]] | [[service-first-branding-and-authentic-visibility]], [[trusted-strategic-advisors-and-influence]], [[cooperation-and-reciprocity]] |
| **2026** | [[the-non-orientable-topology-of-condorcets-paradox]] | [[ori-livson]], [[siddharth-pritam]], [[mikhail-prokopenko]] | [[social-choice-theory]], [[algebraic-topology]], [[game-theory]], [[political-science]] | [[topological-social-choice-and-preference-cycles]], [[rationality-and-decision-making]], [[cooperation-and-reciprocity]] |
| **2024** | [[cumhuriyet-donemi-arkeoloji-politikalari-ve-ekrem-akurgal]] | [[erdal-polat]] | [[archaeological-historiography]], [[anatolian-civilizations]] | [[archaeology-and-national-identity]], [[critique-of-academic-orthodoxy]] |
| **2022** | [[chip-war-the-fight-for-the-worlds-most-critical-technology]] | [[chris-miller]], [[morris-chang]] | [[strategic-studies]], [[security-studies]], [[international-relations]], [[military-science]] | [[semiconductor-geopolitics-and-chokepoints]], [[deterrence-and-coercion]], [[cross-domain-conflict]] |
| **2021** | [[deterrence-in-the-21st-century]] | [[frans-osinga]], [[tim-sweijs]] (eds.) | [[strategic-studies]], [[military-science]], [[game-theory]] | [[deterrence-and-coercion]], [[nuclear-strategy-and-strategic-stability]], [[cross-domain-conflict]] |
| **2020** | [[asik-borani-soz-insanin-aynasi]] | [[asik-borani]], [[ibrahim-gosterir]] (ed.) | [[turkish-folk-literature]], [[anatolian-humanism]], [[poetry-and-poetics]] | [[universal-love-and-human-dignity]], [[social-critique-and-moral-conscience]], [[asik-and-minstrel-tradition]] |
| **2019** | [[america-before-the-key-to-earths-lost-civilization]] | [[graham-hancock]] | [[alternative-archaeology]], [[pre-columbian-history]], [[archaeoastronomy]] | [[pre-clovis-and-american-antiquity]], [[lost-civilization-hypothesis]], [[younger-dryas-impact-hypothesis]] |
| **2017** | [[developing-the-super-soldier-enhancing-military-performance]] | [[william-g-braun-iii]], [[stefanie-von-hlatky]], [[kim-richard-nossal]] (eds.) | [[military-science]], [[strategic-studies]], [[security-studies]], [[organizational-psychology]] | [[human-performance-enhancement-and-neuro-warfare]], [[adaptive-intelligence-and-organizational-resilience]], [[human-centered-ai-and-augmented-leadership]] |
| **2016** | [[oxygen-isotope-in-archaeological-bioapatites-from-india-harappan-civilization]] | [[anindya-sarkar]], [[vasant-shinde]] | [[paleoclimatology]], [[archaeological-historiography]], [[alternative-archaeology]] | [[catastrophism-and-earth-history]], [[adaptive-intelligence-and-organizational-resilience]], [[pre-athenian-and-indigenous-democracies]] |
| **2015** | [[magicians-of-the-gods]] | [[graham-hancock]] | [[alternative-archaeology]], [[catastrophism]], [[archaeoastronomy]] | [[younger-dryas-impact-hypothesis]], [[lost-civilization-hypothesis]], [[catastrophism-and-earth-history]] |
| **2013** | [[war-god-nights-of-the-witch]] | [[graham-hancock]] | [[historical-fiction]], [[speculative-fiction]], [[epic-narrative]] | [[altered-states-and-origin-of-art]], [[clash-of-civilizations]], [[fanaticism-and-human-sacrifice]] |
| **2011** | [[the-master-game]] | [[graham-hancock]], [[robert-bauval]] | [[esoteric-history]], [[occult-studies]], [[hermeticism]] | [[hermetic-tradition-and-secret-societies]], [[orion-correlation-and-sacred-astronomy]] |
| **2011** | [[the-secret-history-of-democracy-primitive-democracy]] | [[benjamin-isakhan]], [[stephen-stockwell]] (eds.), [[thorkild-jacobsen]] | [[comparative-democratic-history]], [[political-science]], [[archaeological-historiography]] | [[pre-athenian-and-indigenous-democracies]], [[critique-of-academic-orthodoxy]], [[cooperation-and-reciprocity]] |
| **2010** | [[lost-knowledge-of-the-ancients]] | [[glenn-kreisberg]] (ed.) | [[alternative-archaeology]], [[esoteric-history]], [[archaeoastronomy]] | [[critique-of-academic-orthodoxy]], [[lost-civilization-hypothesis]], [[submerged-ruins-and-sea-level-rise]] |
| **2009** | [[the-life-and-death-of-democracy-and-monitory-democracy]] | [[john-keane]] | [[comparative-democratic-history]], [[political-science]], [[social-choice-theory]] | [[monitory-democracy-and-power-scrutiny]], [[pre-athenian-and-indigenous-democracies]], [[tyranny-of-the-majority-and-civil-associations]] |
| **2006** | [[the-selfish-gene]] | [[richard-dawkins]] | [[evolutionary-biology]], [[game-theory]], [[anthropology-of-consciousness]] | [[gene-centric-evolution-and-memetics]], [[cooperation-and-reciprocity]], [[tit-for-tat]] |
| **2005** | [[supernatural-meetings-with-the-ancient-teachers-of-mankind]] | [[graham-hancock]] | [[anthropology-of-consciousness]], [[alternative-archaeology]], [[shamanism]] | [[altered-states-and-origin-of-art]], [[lost-civilization-hypothesis]], [[critique-of-academic-orthodoxy]] |
| **2002** | [[underworld-mysterious-origins-of-civilization]] | [[graham-hancock]] | [[alternative-archaeology]], [[paleoclimatology]], [[investigative-non-fiction]] | [[submerged-ruins-and-sea-level-rise]], [[catastrophism-and-earth-history]], [[lost-civilization-hypothesis]] |
| **1998** | [[the-mars-mystery]] | [[graham-hancock]], [[robert-bauval]], [[john-grigsby]] | [[planetary-science-speculation]], [[alternative-archaeology]], [[catastrophism]] | [[planetary-cataclysm-and-cosmic-impacts]], [[catastrophism-and-earth-history]], [[lost-civilization-hypothesis]] |
| **1997** | [[the-first-democracies-early-popular-government-outside-athens]] | [[eric-w-robinson]], [[richard-j-evans]] | [[comparative-democratic-history]], [[political-science]], [[archaeological-historiography]] | [[pre-athenian-and-indigenous-democracies]], [[critique-of-academic-orthodoxy]] |
| **1996** | [[keeper-of-genesis]] | [[graham-hancock]], [[robert-bauval]] | [[archaeoastronomy]], [[alternative-archaeology]], [[esoteric-history]] | [[orion-correlation-and-sacred-astronomy]], [[lost-civilization-hypothesis]], [[critique-of-academic-orthodoxy]] |
| **1995** | [[fingerprints-of-the-gods]] | [[graham-hancock]] | [[alternative-archaeology]], [[archaeoastronomy]], [[investigative-non-fiction]] | [[lost-civilization-hypothesis]], [[catastrophism-and-earth-history]], [[orion-correlation-and-sacred-astronomy]] |
| **1984** | [[the-evolution-of-cooperation]] | [[robert-axelrod]], [[william-d-hamilton]] | [[game-theory]], [[political-science]], [[evolutionary-biology]] | [[cooperation-and-reciprocity]], [[shadow-of-the-future]], [[evolution-of-strategies]], [[tit-for-tat]] |
| **1967** | [[kalven-committee-report-on-the-universitys-role-in-political-and-social-action]] | [[harry-kalven-jr]] | [[political-science]], [[republican-intellectual-history]], [[comparative-democratic-history]] | [[institutional-neutrality-and-academic-freedom]], [[critique-of-academic-orthodoxy]], [[tyranny-of-the-majority-and-civil-associations]] |
| **1840** | [[democracy-in-america]] | [[alexis-de-tocqueville]] | [[political-science]], [[comparative-democratic-history]], [[republican-intellectual-history]], [[social-choice-theory]] | [[tyranny-of-the-majority-and-civil-associations]], [[rationality-and-decision-making]], [[cooperation-and-reciprocity]] |

---

## 🗂️ Complete Wiki Directory Map

```
GilgamisLLMWiki/
├── [Mounted External Library]                      # C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\
│   ├── BOOKS/Archeology/                          # Ingested: 11 landmark works (13 PDF volumes, ~5,500 pp.)
│   ├── BOOKS/Art/                                 # Ingested: Âşık Borani: Söz İnsanın Aynasıdır (2 Vols., 1,150 pp.)
│   ├── BOOKS/Leadership_/                         # Ingested: 5 landmark 2026 works (1,362 pp.)
│   ├── BOOKS/Military_/                           # Ingested: Developing the Super Soldier (2017, 132 pp.)
│   ├── BOOKS/Biology Evolution/                   # Ingested: The Selfish Gene (Dawkins, 2006, 385 pp.)
│   ├── BOOKS/Semiconductors/                      # Ingested: Chip War (Chris Miller, 2022, 473 pp.)
│   ├── ARTICLES-REPORTS/Democracy/                # Ingested: All 10 files (7 distinct works: Tocqueville, Jacobsen/Isakhan/Stockwell, Kalven, Robinson/Evans, Keane, Sarkar/Shinde, Livson/Pritam/Prokopenko)
│   └── BOOKS/AI/, History_/, Philosophy..., ...   # 40+ domain libraries (immutable, git-ignored)
├── .gitignore                                     # Excludes raw/, BOOKS/, and PDF binaries from GitHub sync
├── raw/                                           # Immutable local staging documents (git-ignored)
├── wiki/                                          # Maintained knowledge base (170 markdown pages)
│   ├── index.md                                   # Master index & full TOC
│   ├── log.md                                     # Ingestion & audit changelog
│   ├── index.html                                 # Dashboard web application copy
│   ├── dashboard_data.json                        # Structured JSON export
│   ├── books/                                     # Ingested book detail pages (29 pages)
│   ├── authors/                                   # Author profile pages (64 pages)
│   ├── genres/                                    # Genre index pages (34 pages)
│   └── themes/                                    # Core thematic concept pages (41 pages)
├── .agents/skills/gilgamis-llm-wiki/              # Agent skill definition & tooling
│   ├── SKILL.md                                   # Skill runbook & manifest
│   ├── scripts/
│   │   ├── ollama_agent.py                        # Local Ollama (qwen3.8:latest) ingestion, Vision OCR, query & audit CLI
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

- **Source Immutability**: Source files in `raw/` and the mounted `BOOKS/` and `ARTICLES-REPORTS/` libraries must never be altered or overwritten.
- **Git Sync Exclusion**: All raw and incoming book directories and binary formats are excluded from GitHub sync via `.gitignore`.
- **Naming Conventions**: All wiki files are lowercase with hyphens (e.g., `the-evolution-of-cooperation.md`).
- **Bidirectional Wiki Links**: Every page links to relevant concepts using `[[page-name]]` format.
- **Citation Format**: Every factual assertion and direct quote must cite its source and page/chapter (e.g., `(source: BOOKS/Semiconductors/Chip War_ The Fight for the Wor - Chris Miller.pdf, ch. 29, p. 166)`).
- **Index & Log Tracking**: Every addition or modification must update `wiki/index.md` and append an entry to `wiki/log.md`.
