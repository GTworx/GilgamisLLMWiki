# Gilgamis LLM Wiki — Upcoming Actions & Roadmap

This document records the planned operational, analytical, and interface development tasks scheduled following the 100% completion of the `ARTICLES-REPORTS` library ingestion.

---

## 📌 Status Overview
- **Library Ingestion**: 100.0% Complete (2,901 / 2,901 physical files across 70 collections).
- **Current Canonical Works**: 1,507 works (Works 1–1509).
- **Bidirectional Integrity**: 0 broken links, 0 orphans, 0 unindexed pages.

---

## 🗺️ Roadmapped Action Items

### 1. Interactive Dashboard Updates & UI/UX Enhancements
- [ ] **Visual & Layout Modernization**:
  - Refresh layout and typography for large-screen and mobile readability.
  - Refine dark / light theme palette, accents, and contrast.
- [ ] **Multi-Faceted Search & Filtering**:
  - Add multi-tag filtering (select multiple genres and themes simultaneously).
  - Add faceted filtering by publication year, author, collection source, or canonical work number.
  - Enhance client-side search indexing for instant full-text filtering across 1,500+ works.
- [ ] **Knowledge Graph & Network Exploration**:
  - Integrate an interactive visual graph view (e.g., Force-directed graph / Canvas) showing links between authors, books, genres, and themes.
- [ ] **Reader / Viewer Refinements**:
  - Collapsible panels for executive summaries, chapter breakdowns, key quotes, and thematic dialogues.
  - Quick-copy citation buttons and direct deep links to wiki markdown files.
- [ ] **Build Pipeline & Asset Syncing**:
  - Ensure `build_dashboard.py` cleanly packages and synchronizes `dashboard.html`, `index.html`, and `wiki/dashboard.html` with zero external dependencies.

---

### 2. Deep Semantic Cross-Synthesis & Thematic Research
- [ ] **Cross-Domain Macro Syntheses**:
  - *Frontier AI Scaling vs. Grid Capacity*: Synthesizing works on LLMs, Chinchilla scaling, inference compute, and datacenter energy/nuclear SMR requirements (Works 1487–1509).
  - *Bioelectronic Medicine & Neuroimmunology*: Cross-examining vagus nerve stimulation, bioelectric signaling, temporal interference, and clinical immunotherapy (Works 1475–1486).
  - *Sovereign AI, TSMC Foundries & Geopolitics*: Intersecting semiconductor supply chains, ASML EUV lithography, export controls, and sovereign AI strategies (Works 1417–1422, 1499).
  - *Venture Capital, Private Equity & Automation Productivity*: Correlating PE roll-up strategies, seed-to-scale metrics, and Acemoglu-Restrepo automation labor economics (Works 1465–1474, 1494).
- [ ] **Thematic Briefs & Literature Reviews**:
  - Generate standalone comparative briefs highlighting intellectual debates, consensus, and open problems across ingested works.

---

### 3. Repository Maintenance & Scratch Housekeeping
- [ ] **Scratch Directory Organization**:
  - Review `scratch/` directory and safely archive one-off batch generation scripts (AR-1 through AR-20E2).
  - Retain core recurring maintenance tools:
    - `scratch/survey_complete_status.py` (library audit against physical storage)
    - `scratch/rebuild_index.py` (master index synchronization)
    - `.agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py` (Karpathy LLM agent CLI & link integrity auditor)
    - `.agents/skills/gilgamis-llm-wiki/scripts/build_dashboard.py` (standalone web dashboard compiler)
- [ ] **Git & Documentation Sync**:
  - Ensure `SUMMARY.md`, `wiki/index.md`, and `README.md` continue to reflect all interface and analytical enhancements.
