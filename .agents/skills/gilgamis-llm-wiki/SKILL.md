---
name: gilgamis-llm-wiki
description: >-
  Interactive dashboard and knowledge base management skill for the Gilgamis LLM Wiki.
  Use when the user asks to launch, serve, rebuild, search, navigate, or manage the Gilgamis LLM Wiki dashboard,
  or when they want to query and explore ingested books, authors, genres, and themes through an interactive visual interface.
---

# Gilgamis LLM Wiki Skill

This skill provides an interactive web-based dashboard (`index.html`) and management tooling for the **Gilgamis LLM Wiki** knowledge base, following Andrej Karpathy's LLM Wiki pattern.

---

## Capabilities & Architecture

1. **Visual Interactive Dashboard (`index.html`)**:
   * **Collapsible Sidebar & Mobile Drawer**: Collapsible left banner with header toggle button (`☰`), `Ctrl+B` hotkey, and automatic mobile overlay drawer with blurred backdrop.
   * **Sidebar with Dual Sort Modes**: Sort books dynamically by **Newest First** (publication year) or **Newest Added** (wiki ingestion date/batch), with reversible sort directions and match counter.
   * **Header Filters**: Live multi-criteria filtering by **Genres** and **Themes**.
   * **Universal Search**: Real-time fuzzy search across book titles, authors, executive summaries, chapter breakdowns, and quotes. Hotkey: `/`.
   * **Main Pane**: Full detailed view of the currently selected book (Executive Summary, Chapter Breakdown, Citations, Quotes, Thematic Connections).
   * **Entity Modals**: Interactive popups for author biographies and cross-cutting thematic syntheses.
   * **Theme Switcher**: Dark/Light mode support.

2. **Standalone & Server Modes**:
   * Can be served via a lightweight local HTTP server with automatic browser launch.
   * Also available as a self-contained offline `index.html` in the repository root.

---

## Workflow & Procedures

### 1. Launching the Interactive Dashboard
To start the local server and automatically open the dashboard in the default browser:
```powershell
python .agents/skills/gilgamis-llm-wiki/scripts/serve_dashboard.py
```
*Port*: `http://localhost:8080/index.html` (or `http://localhost:8080/`)

### 2. Rebuilding Dashboard Data After Ingesting New Books
Whenever new markdown pages are added or updated in `wiki/books/`, `wiki/authors/`, `wiki/genres/`, or `wiki/themes/`, run the rebuild script:
```powershell
python .agents/skills/gilgamis-llm-wiki/scripts/build_dashboard.py
```
This updates:
- `wiki/dashboard_data.json`
- `index.html`
- `wiki/index.html`
- `.agents/skills/gilgamis-llm-wiki/resources/index.html`

### 3. Ingestion Sources
Books can be ingested from two immutable sources (both excluded from GitHub sync via `.gitignore`):
1. **Primary Mounted Library**: `C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\` (organized by 42+ domain folders: `Art/`, `AI/`, `Philosophy Psychology Sociology/`, etc.)
2. **Local Staging**: `raw/` (workspace-local ad-hoc additions)

### 4. Querying the Wiki Knowledge Base
When answering cross-comparative questions or literature queries:
1. Refer to the Master Index at `wiki/index.md`.
2. Inspect specific book notes in `wiki/books/`, author profiles in `wiki/authors/`, or thematic syntheses in `wiki/themes/`.
3. Provide page-level citations referencing the source PDF files in `BOOKS/<Category>/` or `raw/`.

---

## Related References & Resources

- [Dashboard Guide](./references/dashboard_guide.md) — UI architecture, shortcuts, and feature guide.
- [Dashboard App (`index.html`)](./resources/index.html) — Standalone HTML dashboard application.
- [Dashboard Template](./resources/dashboard_template.html) — Clean template file.
- [Rebuild Script](./scripts/build_dashboard.py) — Parsing and data generation script.
- [Server Script](./scripts/serve_dashboard.py) — Local server with auto-launch.
