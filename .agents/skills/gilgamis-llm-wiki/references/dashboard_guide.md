# Gilgamis LLM Wiki Dashboard Guide

## Overview

The **Gilgamis LLM Wiki Dashboard** (`index.html`) is a standalone, browser-based user interface for navigating, searching, and analyzing the personal book library and strategic knowledge base.

---

## Layout & Architecture

### 1. Header Controls
- **Brand & Version**: Displays the repository title and version indicator.
- **Universal Search Bar**:
  - Hotkey: Press `/` from anywhere on the page to focus the search bar.
  - Live filtering across book titles, authors, executive summaries, chapter notes, and key quotes.
- **Genre Filter Dropdown**: Dynamically populated with all genres from `wiki/genres/`. Filters sidebar listings on change.
- **Theme Filter Dropdown**: Dynamically populated with all core themes from `wiki/themes/`. Filters sidebar listings on change.
- **Dark/Light Theme Toggle**: Instant transition between dark mode and light mode.

### 2. Sidebar (Newest on Top)
- Book list sorted descending by publication year and ingestion freshness.
- Each book card displays:
  - Publication year badge (gold monospace).
  - Full title.
  - Formatted author list.
  - Genre chips.
- Active card highlighting and automatic selection synchronization.

### 3. Main Pane (Selected Book View)
- **Hero Metadata Card**: Title, publication year badge, source file path, last updated timestamp, clickable author links, and genre/theme filter pills.
- **Executive Summary**: Core thesis and narrative/conceptual arc with wiki link resolution.
- **Key Arguments & Chapter Breakdown**: Comprehensive chapter-by-chapter notes, sub-arguments, and strategic models.
- **Key Quotes & Citations**: Distinct callout quote cards with source file and page-level references.
- **Thematic Connections**: Cross-comparative analysis detailing how the selected book dialogues with other library works.

### 4. Interactive Entity Drawers (Modals)
- Clicking any author or theme link anywhere in the dashboard opens an instant preview modal displaying author bios, movements, or cross-cutting thematic syntheses without leaving the book view.
- Press `ESC` or click outside to dismiss the modal.

---

## Rebuilding & Serving

1. **Rebuild Data**:
   ```bash
   python .agents/skills/gilgamis-llm-wiki/scripts/build_dashboard.py
   ```

2. **Serve with Auto-Launch**:
   ```bash
   python .agents/skills/gilgamis-llm-wiki/scripts/serve_dashboard.py
   ```
   Opens `http://localhost:8080/index.html` (or `http://localhost:8080/`) in the default web browser.

3. **Direct File Access**:
   You can also double-click `index.html` in the workspace root to view the dashboard directly in any browser with zero dependencies.
