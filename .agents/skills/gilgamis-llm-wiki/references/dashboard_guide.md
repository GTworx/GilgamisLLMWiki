# Gilgamis LLM Wiki Dashboard Guide

## Overview

The **Gilgamis LLM Wiki Dashboard** (`index.html`) is a standalone, browser-based user interface for navigating, searching, and analyzing the personal book library and strategic knowledge base.

---

## Layout & Architecture

### 1. Header Controls
- **Sidebar Toggle Button**: 
  - Hamburger button (`☰`) in the header next to the brand logo.
  - Hotkey: `Ctrl+B` (or `Cmd+B`) toggles the left banner collapsed/expanded state.
  - On desktop: Collapses the sidebar to provide full-width distraction-free reading. State is persisted in `localStorage`.
  - On mobile devices: Opens the left banner as an animated slide-over drawer with a dimmed backdrop.
- **Brand & Version**: Displays the repository title and version indicator.
- **Universal Search Bar**:
  - Hotkey: Press `/` from anywhere on the page to focus the search bar.
  - Live filtering across book titles, authors, executive summaries, chapter notes, and key quotes.
- **Genre Filter Dropdown**: Dynamically populated with all genres from `wiki/genres/`. Filters sidebar listings on change.
- **Theme Filter Dropdown**: Dynamically populated with all core themes from `wiki/themes/`. Filters sidebar listings on change.
- **Dark/Light Theme Toggle**: Instant transition between dark mode and light mode.

### 2. Sidebar & Mobile Drawer (Sortable: Newest First & Newest Added)
- **Dual Sorting Modes**:
  - **Newest First** (Default): Sorts books chronologically by publication year (`2024` down to `1984`). Clicking the active button toggles between *Newest First* (↓) and *Oldest First* (↑).
  - **Newest Added**: Sorts books by their ingestion date and chronological addition order to the wiki, keeping newly ingested batches on top. Clicking toggles between *Newest Added* (↓) and *Oldest Added* (↑).
  - When *Newest Added* is active, each book card displays a green `Added YYYY-MM-DD` timestamp chip.
  - Sorting preferences (mode and direction) persist across sessions in `localStorage`.
- **Title Counter Badge**: Dynamically displays the number of matching books based on active search and dropdown filters.
- **Mobile-Responsive Architecture**:
  - On mobile/tablets (`<=900px`), the sidebar collapses by default and acts as an overlay slide-out drawer with a blurred backdrop (`#sidebarBackdrop`).
  - Tapping outside the drawer, clicking the close button (`×`), or pressing `ESC` smoothly closes the sidebar.
  - Selecting any book on mobile automatically closes the drawer and displays the full book details.
- **Book List**:
  - Each book card displays:
    - Publication year badge (gold monospace) and optional added date chip.
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
