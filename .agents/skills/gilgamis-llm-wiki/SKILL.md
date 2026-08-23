---
name: gilgamis-llm-wiki
description: >-
  Interactive dashboard and knowledge base management skill for the Gilgamis LLM Wiki.
  Use when the user asks to launch, serve, rebuild, search, navigate, or manage the Gilgamis LLM Wiki dashboard,
  or when they want to query and explore ingested books, authors, genres, and themes through an interactive visual interface.
---

# Gilgamis LLM Wiki Skill

This skill provides an interactive web-based dashboard and management tooling for the **Gilgamis LLM Wiki** knowledge base, following Andrej Karpathy's LLM Wiki pattern.

---

## Capabilities & Architecture

1. **Visual Interactive Dashboard**:
   * **Sidebar**: Displays all ingested book titles with the newest publications on top, showing publication year, authors, and genre badges.
   * **Header Filters**: Live multi-criteria filtering by **Genres** and **Themes**.
   * **Universal Search**: Real-time fuzzy search across book titles, authors, executive summaries, chapter breakdowns, and quotes. Hotkey: `/`.
   * **Main Pane**: Full detailed view of the currently selected book (Executive Summary, Chapter Breakdown, Citations, Quotes, Thematic Connections).
   * **Entity Modals**: Interactive popups for author biographies and cross-cutting thematic syntheses.
   * **Theme Switcher**: Dark/Light mode support.

2. **Standalone & Server Modes**:
   * Can be served via a lightweight local HTTP server with automatic browser launch.
   * Also available as a self-contained offline `dashboard.html` in the repository root.

---

## Workflow & Procedures

### 1. Launching the Interactive Dashboard
To start the local server and automatically open the dashboard in the default browser:
```powershell
python .agents/skills/gilgamis-llm-wiki/scripts/serve_dashboard.py
```
*Port*: `http://localhost:8765/dashboard.html`

### 2. Rebuilding Dashboard Data After Ingesting New Books
Whenever new markdown pages are added or updated in `wiki/books/`, `wiki/authors/`, `wiki/genres/`, or `wiki/themes/`, run the rebuild script:
```powershell
python .agents/skills/gilgamis-llm-wiki/scripts/build_dashboard.py
```
This updates:
- `wiki/dashboard_data.json`
- `dashboard.html`
- `wiki/dashboard.html`
- `.agents/skills/gilgamis-llm-wiki/resources/dashboard.html`

### 3. Querying the Wiki Knowledge Base
When answering cross-comparative questions or literature queries:
1. Refer to the Master Index at `wiki/index.md`.
2. Inspect specific book notes in `wiki/books/`, author profiles in `wiki/authors/`, or thematic syntheses in `wiki/themes/`.
3. Provide page-level citations referencing the raw PDF files in `raw/`.

---

## Related References & Resources

- [Dashboard Guide](./references/dashboard_guide.md) — UI architecture, shortcuts, and feature guide.
- [Dashboard Template](./resources/dashboard.html) — Standalone HTML dashboard application.
- [Rebuild Script](./scripts/build_dashboard.py) — Parsing and data generation script.
- [Server Script](./scripts/serve_dashboard.py) — Local server with auto-launch.
