# Gilgamis LLM Wiki

A structured, interlinked personal knowledge base for cataloging, analyzing, and synthesizing a personal library of books, strategic literature, democracy studies, evolutionary biology, neuroscience, innovation, cybersecurity, blockchain, law, energy economics, education, ethics, and archaeology, maintained by LLM agents (including local Ollama `qwen3.8:latest`) based on Andrej Karpathy's LLM Wiki pattern.

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

- **Total Ingested Works**: 60 distinct intellectual works (across 67 source files/volumes and ~21,500 pages)
- **Total Maintained Wiki Pages**: 286 interlinked markdown documents (284 entity pages + `index.md` & `log.md`)
- **Book Analyses**: 60 ([wiki/books/](wiki/books/))
- **Author Profiles**: 123 ([wiki/authors/](wiki/authors/))
- **Genre Indices**: 49 ([wiki/genres/](wiki/genres/))
- **Thematic Syntheses**: 52 ([wiki/themes/](wiki/themes/))
- **Bidirectional Link Integrity**: 100% (0 broken `[[...]]` links, 0 orphaned pages, 0 unindexed pages)
- **Source Integrity**: Strict textual citations referencing exact source files and page numbers; source libraries (`BOOKS/`, `ARTICLES-REPORTS/`, and `raw/`) remain immutable and are excluded from GitHub synchronization via `.gitignore`.

---

## 📚 Complete Ingested Library Catalog (60 Works)

| Year | Title | Author(s) | Primary Genres | Core Themes |
| :--- | :--- | :--- | :--- | :--- |
| **2026** | [[advanced-network-forensics-a-cyber-behavioral-science-approach]] | [[marshall-s-rich]] | [[cybersecurity-and-digital-forensics]], [[organizational-psychology]], [[security-studies]] | [[hybrid-threats-and-cyber-warfare]], [[human-centered-ai-and-augmented-leadership]], [[rationality-and-decision-making]] |
| **2025** | [[blockchain-crypto-and-defi-bridging-finance-and-technology]] | [[marco-di-maggio]] | [[blockchain-and-decentralized-finance]], [[game-theory]], [[strategic-studies]] | [[decentralized-trust-and-cryptographic-governance]], [[cooperation-and-reciprocity]], [[human-centered-ai-and-augmented-leadership]] |
| **2023** | [[doppelganger-israel-palestine-and-the-doppelganger-effect]] | [[naomi-klein]] | [[postcolonial-and-diaspora-studies]], [[political-science]], [[investigative-non-fiction]] | [[constrained-vs-unconstrained-visions-and-postcolonial-identity]], [[social-critique-and-moral-conscience]], [[clash-of-civilizations]] |
| **2023** | [[monetizing-energy-storage-a-toolkit-to-assess-future-cost-and-value]] | [[oliver-schmidt]], [[iain-staffell]] | [[energy-policy-and-clean-tech-economics]], [[innovation-and-economic-growth]], [[strategic-studies]] | [[energy-transition-and-storage-economics]], [[rationality-and-decision-making]], [[general-purpose-technologies-and-learning-by-doing]] |
| **2022** | [[burasi-cok-onemli-enerjiden-ekonomiye-tam-bagimsiz-turkiye]] | [[berat-albayrak]] | [[energy-policy-and-clean-tech-economics]], [[political-science]], [[strategic-studies]] | [[energy-transition-and-storage-economics]], [[semiconductor-geopolitics-and-chokepoints]], [[archaeology-and-national-identity]] |
| **2022** | [[electric-vehicles-light-duty-fuel-economy-and-shared-micromobility]] | [[kwo-young]], [[gary-marchant]], [[colin-murphy]], [[alexander-kolpakov]] | [[energy-policy-and-clean-tech-economics]], [[innovation-and-economic-growth]], [[public-policy-and-urban-mobility]] | [[energy-transition-and-storage-economics]], [[rationality-and-decision-making]], [[cooperation-and-reciprocity]] |
| **2021** | [[the-challenger-sale-challenge-yourself-action-book]] | [[matthew-dixon]], [[brent-adamson]] | [[consultative-sales-and-commercial-teaching]], [[strategic-communication]], [[leadership-and-management]] | [[consultative-questioning-and-constructive-tension]], [[trusted-strategic-advisors-and-influence]], [[rationality-and-decision-making]] |
| **2020** | [[gormedigimiz-turkiye-123-yillik-national-geographic-arsivi]] | [[kurt-and-margot-lubinski]], [[bernard-f-rogers-jr]] | [[anatolian-civilizations]], [[republican-intellectual-history]], [[archaeological-historiography]] | [[archaeology-and-national-identity]], [[universal-love-and-human-dignity]] |
| **2019** | [[educational-technology-a-primer-for-the-21st-century]] | [[ronghuai-huang]], [[j-michael-spector]], [[junfeng-yang]] | [[educational-technology-and-disruptive-pedagogy]], [[organizational-psychology]], [[anthropology-of-consciousness]] | [[student-centric-and-blended-learning]], [[human-centered-ai-and-augmented-leadership]], [[rationality-and-decision-making]] |
| **2019** | [[entertainment-science-data-analytics-and-practical-theory]] | [[thorsten-hennig-thurau]], [[mark-b-houston]] | [[media-economics-and-entertainment-science]], [[strategic-communication]], [[leadership-and-management]] | [[attention-economy-and-cultural-analytics]], [[rationality-and-decision-making]], [[service-first-branding-and-authentic-visibility]] |
| **2019** | [[getting-started-with-enterprise-blockchain]] | [[michael-bradley]], [[david-gorman]], [[matt-lucas]], [[matthew-golby-kirk]] | [[blockchain-and-decentralized-finance]], [[strategic-studies]], [[leadership-and-management]] | [[decentralized-trust-and-cryptographic-governance]], [[cooperation-and-reciprocity]], [[semiconductor-geopolitics-and-chokepoints]] |
| **2019** | [[media-and-digital-management]] | [[eli-m-noam]] | [[media-economics-and-entertainment-science]], [[leadership-and-management]], [[innovation-and-economic-growth]] | [[attention-economy-and-cultural-analytics]], [[rationality-and-decision-making]], [[general-purpose-technologies-and-learning-by-doing]] |
| **2017** | [[ethics-in-higher-education-values-driven-leaders-for-the-future]] | [[divya-singh]], [[christoph-stuckelberger]], [[obiora-ike]] | [[ethics-and-value-philosophy]], [[educational-technology-and-disruptive-pedagogy]], [[leadership-and-management]] | [[metaphysics-of-quality-and-global-ethics]], [[institutional-neutrality-and-academic-freedom]], [[student-centric-and-blended-learning]] |
| **2017** | [[introduction-to-law]] | [[jaap-hage]], [[antonia-waltermann]], [[bram-akkermans]] | [[law-and-quantitative-criminology]], [[political-science]], [[republican-intellectual-history]] | [[rule-of-law-and-experimental-justice]], [[tyranny-of-the-majority-and-civil-associations]], [[rationality-and-decision-making]] |
| **2016** | [[global-ethics-for-leadership-values-and-virtues-for-life]] | [[christoph-stuckelberger]], [[walter-fust]], [[obiora-ike]] | [[ethics-and-value-philosophy]], [[leadership-and-management]], [[international-relations]] | [[metaphysics-of-quality-and-global-ethics]], [[universal-love-and-human-dignity]], [[cooperation-and-reciprocity]] |
| **2016** | [[reductionism-in-art-and-brain-science-bridging-the-two-cultures]] | [[eric-r-kandel]] | [[neuroscience-and-philosophy-of-mind]], [[anthropology-of-consciousness]], [[poetry-and-poetics]] | [[neurobiology-of-consciousness-and-non-algorithmic-mind]], [[altered-states-and-origin-of-art]], [[evolution-of-human-consciousness]] |
| **2015** | [[blended-using-disruptive-innovation-to-improve-schools]] | [[michael-b-horn]], [[heather-staker]], [[clayton-m-christensen]] | [[educational-technology-and-disruptive-pedagogy]], [[leadership-and-management]], [[organizational-psychology]] | [[student-centric-and-blended-learning]], [[adaptive-intelligence-and-organizational-resilience]], [[organizational-culture-and-rewilding]] |
| **2015** | [[learning-by-doing-the-real-connection-between-innovation-wages-and-wealth]] | [[james-bessen]] | [[innovation-and-economic-growth]], [[political-science]], [[leadership-and-management]] | [[general-purpose-technologies-and-learning-by-doing]], [[human-centered-ai-and-augmented-leadership]], [[rationality-and-decision-making]] |
| **2012** | [[computer-security-incident-handling-guide-nist-sp-800-61r2]] | [[paul-cichonski]], [[tom-millar]], [[tim-grance]], [[karen-scarfone]] | [[cybersecurity-and-digital-forensics]], [[security-studies]], [[strategic-studies]] | [[hybrid-threats-and-cyber-warfare]], [[adaptive-intelligence-and-organizational-resilience]], [[rationality-and-decision-making]] |
| **2010** | [[handbook-of-quantitative-criminology]] | [[alex-r-piquero]], [[david-weisburd]] | [[law-and-quantitative-criminology]], [[social-choice-theory]], [[political-science]] | [[rule-of-law-and-experimental-justice]], [[rationality-and-decision-making]], [[cooperation-and-reciprocity]] |
| **2008** | [[disrupting-class-how-disruptive-innovation-will-change-the-way-the-world-learns]] | [[clayton-m-christensen]], [[michael-b-horn]], [[curtis-w-johnson]] | [[educational-technology-and-disruptive-pedagogy]], [[innovation-and-economic-growth]], [[organizational-psychology]] | [[student-centric-and-blended-learning]], [[general-purpose-technologies-and-learning-by-doing]], [[adaptive-intelligence-and-organizational-resilience]] |
| **2007** | [[a-conflict-of-visions-ideological-origins-of-political-struggles]] | [[thomas-sowell]] | [[political-science]], [[social-choice-theory]], [[republican-intellectual-history]] | [[constrained-vs-unconstrained-visions-and-postcolonial-identity]], [[rationality-and-decision-making]], [[tyranny-of-the-majority-and-civil-associations]] |
| **2007** | [[mongrel-nation-colonization-in-reverse]] | [[ashley-dawson]], [[louise-bennett]] | [[postcolonial-and-diaspora-studies]], [[political-science]], [[poetry-and-poetics]] | [[constrained-vs-unconstrained-visions-and-postcolonial-identity]], [[social-critique-and-moral-conscience]], [[tyranny-of-the-majority-and-civil-associations]] |
| **2006** | [[the-medici-effect-what-elephants-and-epidemics-can-teach-us-about-innovation]] | [[frans-johansson]] | [[innovation-and-economic-growth]], [[leadership-and-management]], [[organizational-psychology]] | [[general-purpose-technologies-and-learning-by-doing]], [[adaptive-intelligence-and-organizational-resilience]], [[cooperation-and-reciprocity]] |
| **2005** | [[economic-transformations-general-purpose-technologies-and-long-term-economic-growth]] | [[richard-g-lipsey]], [[kenneth-i-carlaw]], [[clifford-t-bekar]] | [[innovation-and-economic-growth]], [[political-science]], [[archaeological-historiography]] | [[general-purpose-technologies-and-learning-by-doing]], [[rationality-and-decision-making]], [[evolution-of-strategies]] |
| **2001** | [[the-end-of-modernism-elias-canettis-auto-da-fe]] | [[william-collins-donahue]], [[elias-canetti]] | [[literary-criticism-and-modernism]], [[philosophical-fiction]], [[republican-intellectual-history]] | [[critique-of-academic-orthodoxy]], [[social-critique-and-moral-conscience]], [[fanaticism-and-human-sacrifice]] |
| **1992** | [[discovering-the-brain]] | [[sandra-ackerman]] | [[neuroscience-and-philosophy-of-mind]], [[evolutionary-biology]], [[organizational-psychology]] | [[neurobiology-of-consciousness-and-non-algorithmic-mind]], [[human-performance-enhancement-and-neuro-warfare]], [[adaptive-intelligence-and-organizational-resilience]] |
| **1989** | [[the-emperors-new-mind-concerning-computers-minds-and-the-laws-of-physics]] | [[roger-penrose]] | [[neuroscience-and-philosophy-of-mind]], [[algebraic-topology]], [[anthropology-of-consciousness]] | [[neurobiology-of-consciousness-and-non-algorithmic-mind]], [[human-centered-ai-and-augmented-leadership]], [[rationality-and-decision-making]] |
| **1988** | [[spin-selling]] | [[neil-rackham]] | [[consultative-sales-and-commercial-teaching]], [[strategic-communication]], [[organizational-psychology]] | [[consultative-questioning-and-constructive-tension]], [[trusted-strategic-advisors-and-influence]], [[rationality-and-decision-making]] |
| **1985** | [[noise-the-political-economy-of-music]] | [[jacques-attali]], [[fredric-jameson]], [[susan-mcclary]] | [[philosophy-and-poetics-of-music]], [[political-science]], [[social-choice-theory]] | [[music-as-prophecy-and-political-economy]], [[critique-of-academic-orthodoxy]], [[social-critique-and-moral-conscience]] |
| **1974** | [[zen-and-the-art-of-motorcycle-maintenance]] | [[robert-m-pirsig]] | [[ethics-and-value-philosophy]], [[philosophical-fiction]], [[anthropology-of-consciousness]] | [[metaphysics-of-quality-and-global-ethics]], [[rationality-and-decision-making]], [[critique-of-academic-orthodoxy]] |

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
│   ├── BOOKS/Türkiye_/                            # Ingested: Görmediğimiz Türkiye: 123 Yıllık National Geographic Arşivi
│   ├── BOOKS/Music/                               # Ingested: Noise: The Political Economy of Music (Attali, 1985)
│   ├── BOOKS/Fiction/                             # Ingested: The End of Modernism: Elias Canetti's Auto-da-Fé (Donahue, 2001)
│   ├── BOOKS/Blockchain_/                         # Ingested: 2 works (Blockchain, Crypto & DeFi; Enterprise Blockchain)
│   ├── BOOKS/Cybersecurity/                       # Ingested: 2 works (NIST SP 800-61r2; Advanced Network Forensics)
│   ├── BOOKS/Energy/                              # Ingested: 3 works across 6 files (Burası Çok Önemli; Monetizing Energy Storage; EVs & Shared Micromobility)
│   ├── BOOKS/Entertainment Media/                 # Ingested: 2 works (Entertainment Science; Media and Digital Management)
│   ├── BOOKS/Law/                                 # Ingested: 2 works (Handbook of Quantitative Criminology; Introduction to Law)
│   ├── BOOKS/Sales/                               # Ingested: 2 works (SPIN Selling; The Challenger Sale Action Book)
│   ├── BOOKS/Education_/                          # Ingested: 3 works (Disrupting Class; Blended; Educational Technology)
│   ├── BOOKS/Ethics/                              # Ingested: 3 works (Zen and the Art of Motorcycle Maintenance; Global Ethics; Ethics in Higher Education)
│   ├── BOOKS/Innovation_/                         # Ingested: 3 works (Economic Transformations GPTs; Learning by Doing; The Medici Effect)
│   ├── BOOKS/Neuroscience_/                       # Ingested: 3 works (The Emperor's New Mind; Discovering the Brain; Reductionism in Art and Brain Science)
│   ├── BOOKS/Society_/                            # Ingested: 3 works across 4 files (A Conflict of Visions; Doppelganger Effect; Mongrel Nation)
│   ├── ARTICLES-REPORTS/Democracy/                # Ingested: All 10 files (7 distinct works: Tocqueville, Jacobsen/Isakhan/Stockwell, Kalven, Robinson/Evans, Keane, Sarkar/Shinde, Livson/Pritam/Prokopenko)
│   └── BOOKS/AI/, History_/, Philosophy..., ...   # Remaining domain libraries (immutable, git-ignored)
├── .gitignore                                     # Excludes raw/, BOOKS/, and PDF binaries from GitHub sync
├── raw/                                           # Immutable local staging documents (git-ignored)
├── wiki/                                          # Maintained knowledge base (286 markdown pages)
│   ├── index.md                                   # Master index & full TOC
│   ├── log.md                                     # Ingestion & audit changelog
│   ├── index.html                                 # Dashboard web application copy
│   ├── dashboard_data.json                        # Structured JSON export
│   ├── books/                                     # Ingested book detail pages (60 pages)
│   ├── authors/                                   # Author profile pages (123 pages)
│   ├── genres/                                    # Genre index pages (49 pages)
│   └── themes/                                    # Core thematic concept pages (52 pages)
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
