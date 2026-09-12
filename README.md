# Gilgamis LLM Wiki

A structured, interlinked personal knowledge base for cataloging, analyzing, and synthesizing a personal library of books and strategic literature, maintained by LLM agents based on Andrej Karpathy's LLM Wiki pattern.

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
│ INGESTED TITLES      │ 📖 Deterrence in the 21st Century — Insights from Theory & Practice│
│ (Newest First)       │ Published 2021 · Source: raw/Deterrence in 21st Century...       │
│                      │ By Frans Osinga, Tim Sweijs, Lawrence Freedman, ...             │
│ [2021] Deterrence    │ Genres: [Strategic Studies] [Military Science] [Game Theory]    │
│  in 21st Century     │ Themes: [Deterrence & Coercion] [Cross-Domain] [Non-Western]    │
│                      ├─────────────────────────────────────────────────────────────────┤
│ [1984] The Evolution │ ℹ️ Executive Summary                                            │
│  of Cooperation      │ Cross-disciplinary volume assessing deterrence across nuclear,  │
│                      │ conventional, cyber, space, AI, and non-Western doctrines...   │
│                      ├─────────────────────────────────────────────────────────────────┤
│                      │ 📑 Key Arguments & Chapter Breakdown (Ch. 1–26)                 │
│                      │ • Freedman (Ch. 1): Evolution through 4 scholarship waves...    │
│                      │ • Mazarr (Ch. 2): Denial vs Punishment & Assurances...          │
│                      │ • Adamsky (Ch. 9): Russian holistic 'Sderzhivanie'...           │
│                      ├─────────────────────────────────────────────────────────────────┤
│                      │ 💬 Key Quotes & Page Citations                                  │
│                      │ 🔗 Thematic Connections & Dialogues                             │
└──────────────────────┴─────────────────────────────────────────────────────────────────┘
```

### Dashboard Features
- **Sidebar (Titles Newest on Top)**: Displays books in descending chronological order (`2021` *Deterrence in the 21st Century*, then `1984` *The Evolution of Cooperation*), with year badges, authors, and genre chips.
- **Header Filters**: Live multi-criteria dropdown filtering for **Genres** (7 categories) and **Themes** (11 categories).
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

- **Total Ingested Volumes**: 3 volumes (1,931 total pages across strategic studies, game theory, and Anatolian minstrel literature)
- **Total Maintained Wiki Pages**: 53 interlinked markdown documents
- **Book Analyses**: 3 ([wiki/books/](wiki/books/))
- **Author Profiles**: 26 ([wiki/authors/](wiki/authors/))
- **Genre Indices**: 10 ([wiki/genres/](wiki/genres/))
- **Thematic Syntheses**: 14 ([wiki/themes/](wiki/themes/))
- **Bidirectional Link Integrity**: 100% (0 broken `[[...]]` links, 0 orphaned pages)
- **Source Integrity**: Strict textual citations referencing exact source files and page numbers; source libraries (`BOOKS/` and `raw/`) remain immutable and are excluded from GitHub synchronization via `.gitignore`.

---

## 📚 Ingested Library Summaries

### 1. [The Evolution of Cooperation](wiki/books/the-evolution-of-cooperation.md)
* **Author(s)**: [[robert-axelrod]], [[william-d-hamilton]]
* **Publication**: Basic Books, 1984 (243 pp.)
* **Source**: `raw/Axelrod_Robert_The_Evolution_of_Cooperation.pdf`
* **Primary Genres**: [[game-theory]], [[political-science]], [[evolutionary-biology]], [[strategic-studies]]
* **Core Themes**: [[cooperation-and-reciprocity]], [[shadow-of-the-future]], [[evolution-of-strategies]], [[rationality-and-decision-making]], [[tit-for-tat]]

#### Executive Summary
Axelrod addresses a fundamental question across social science and biology: under what conditions will cooperation emerge in a world of egoists without central authority? Using the iterated Prisoner's Dilemma, Axelrod ran two computer tournaments pitting strategies from game theorists, economists, psychologists, and mathematicians. 

The tournaments demonstrated the decisive success of **TIT FOR TAT**—a simple strategy submitted by Anatol Rapoport that starts by cooperating and thereafter replicates the opponent's previous move. Axelrod extracts four core strategic virtues:
1. **Be Nice**: Never defect first, preventing unnecessary conflict.
2. **Be Provocable / Retaliatory**: Punish unprovoked defection immediately to avoid exploitation.
3. **Be Forgiving**: Restore cooperation immediately once the adversary relents.
4. **Be Clear**: Maintain transparent, predictable rules so counterparts can recognize reciprocity.

Axelrod extends the model to historical case studies—such as the "live-and-let-live" system in WWI trench warfare—and evolutionary biology (co-authored with W.D. Hamilton), offering practical advice for institutional designers to promote cooperation by enlarging the **shadow of the future** ($w$).

---

### 2. [Söz İnsanın Aynasıdır (Cilt I & II)](wiki/books/asik-borani-soz-insanin-aynasi.md)
* **Author(s)**: [[asik-borani]] (Halil Çimen), [[ibrahim-gosterir]] (ed.)
* **Publication**: T.C. Çorum Valiliği İl Kültür ve Turizm Müdürlüğü, Yayın No: 19, 2020 (1,150 pp., 2 Vols.)
* **Source**: `BOOKS/Art/73010,cilt1pdf.pdf`, `BOOKS/Art/73011,cilt2pdf.pdf` (Mount: `C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\Art\`)
* **Primary Genres**: [[turkish-folk-literature]], [[anatolian-humanism]], [[poetry-and-poetics]]
* **Core Themes**: [[universal-love-and-human-dignity]], [[social-critique-and-moral-conscience]], [[asik-and-minstrel-tradition]], [[rationality-and-decision-making]], [[non-western-strategic-thought]]

#### Executive Summary
A comprehensive two-volume, 1,150-page compendium representing the complete lifetime works of Âşık Borani (Halil Çimen, 1943–2020), one of modern Turkey's preeminent folk poets and minstrel-philosophers (*halk ozanı*). Compiled by folklorist İbrahim Gösterir, the work spans ten sections capturing sixty years of poetic creation:
1. **Elinde Gül Olsun Dilinde Türkü** & **İnsana Yolculuk**: Foundational poetry defining the minstrel's saz as moral medicine and the human conscience as the sacred mirror of truth (*Natık-ı Kuran*).
2. **Fadime'ye Mektuplar** & **Fadime'ye Son Mektuplar**: Celebrated epistolary cycles addressed to "Fadime"—muse, confidante, and symbol of rural Anatolian womanhood and enduring love.
3. **Âdem'in Aynası** & **Söz İnsana Söylenir**: Philosophical meditations on human dignity, communicative ethics (*söz insanın aynasıdır*), and universal egalitarianism ("I recognize only one race: Humanity").
4. **Bozkırın Gülleri**, **Sevgiye Davet**, & **Serbest Dizeli Şiirler**: Pastoral hymns to steppe resilience, universal anti-sectarian appeals, and experiments in modern free-verse folk poetics.
5. **Toplumcu Gerçekçilik & Taşlama**: Fearless social satire targeting political corruption, bureaucratic greed, and religious hypocrisy (*"Kim çalarsa çalsın adı hırsızdır"*).

---

### 3. [Deterrence in the 21st Century — Insights from Theory and Practice](wiki/books/deterrence-in-the-21st-century.md)
* **Editors**: [[frans-osinga]], [[tim-sweijs]]
* **Publication**: NL ARMS 2020 / T.M.C. Asser Press / Springer, 2021 (538 pp.)
* **Source**: `raw/Deterrence in 21st Century Nuclear NetherlandsAnnualReviewO.pdf`
* **Primary Genres**: [[strategic-studies]], [[military-science]], [[international-relations]], [[security-studies]], [[game-theory]]
* **Core Themes**: [[deterrence-and-coercion]], [[nuclear-strategy-and-strategic-stability]], [[cross-domain-conflict]], [[non-western-strategic-thought]], [[rationality-and-decision-making]], [[hybrid-threats-and-cyber-warfare]], [[violent-non-state-actors]]

#### Executive Summary
An encyclopedic volume examining the renaissance and re-conceptualization of deterrence in contemporary geopolitics across 26 chapters and six parts:
1. **Concepts of Deterrence (Part I)**: Tracing four waves of deterrence scholarship (Freedman); fundamentals of denial vs. punishment, 3Cs (Capability, Credibility, Communication), and **Assurances** (Mazarr); NATO territorial defense (Rynning); conventional deterrence modes (Mueller); arms control erosion (Arbatov); extended deterrence credibility (van Hooft); NATO eFP tripwires (Noll et al.); and Cross-Domain Deterrence (CDD) modeling (Sweijs & Zilincik).
2. **Non-Western Strategic Thought (Part II)**: Russian holistic *Sderzhivanie* blending non-military coercion, *maskirovka*, and nuclear signaling (Adamsky); Chinese proactive *Weishe* and the Three Warfares (Cheng); Japanese defense (Katagiri); South Asian Stability-Instability Paradox (Aarten); and Iranian forward-deterrence proxy networks in Syria (Ahmadian & Mohseni).
3. **Non-State Actors & Irregular War (Part III)**: Cumulative deterrence ("mowing the lawn") against VNSAs like Hamas/Hezbollah (Shamir); localized counterinsurgency deterrence tailored to village/tribal kinship systems (Kitzen & van Kuijck); Russian deterrence of democratic revolts (Rothman); and coercive diplomacy in peace operations (Jakobsen).
4. **New Instruments & Domains (Part IV)**: Targeted economic sanctions (Giumelli); societal and institutional resilience as deterrence by denial against hybrid threats (van Doorn & Brinkel); cyber deterrence challenges (attribution latency, exploit perishability) (Soesanto & Smeets); and AI hyper-coercion and autonomous swarm saturation (Wilner & Babb).
5. **Rationality, Psychology, Emotions & Law (Part V)**: Algorithmic game theory and automated C2 risks (Lindelauf); behavioral heuristics and Prospect Theory's loss aversion driving risk-seeking in domain of losses (Bijlsma); emotion-centric deterrence modeling fear, anger, and pride (Zilincik & Duyvesteyn); and international legal thresholds under UN Charter Art. 51, countermeasures, and retorsion (Ducheine & Pijpers).
6. **Synthesis (Part VI)**: Cross-cutting roadmap by Sweijs & Osinga calling for multi-domain synergy, cognitive empathy, and whole-of-society resilience.

---

### 🔬 Cross-Comparative Synthesis

| Dimension | Axelrod (*Evolution of Cooperation*) | Osinga & Sweijs (*Deterrence in the 21st Century*) | Âşık Borani (*Söz İnsanın Aynasıdır*) | Integrated Wiki Takeaway |
| :--- | :--- | :--- | :--- | :--- |
| **Strategic & Moral Mechanism** | Reciprocity (TIT FOR TAT): nice, retaliatory, forgiving, clear. | Deterrence by punishment/denial, credible threats, and assurances. | Unconditional love (*sevgi ilimi*), communal empathy, and ethical conscience. | Retaliation without forgiveness produces destructive spirals; strategic deterrence needs positive assurances, while social sustainability requires an ethical baseline of human dignity. |
| **Time Horizon** | Shadow of the future ($w$): large $w$ sustains cooperation under anarchy. | Strategic stability and arms control treaties preserve long-term predictability. | Cultural memory, generational poetry, and existential transience (*ölüm nikâhı*). | Long horizons disincentivize cheating; bards and strategic regimes both serve to preserve collective stability across generational time. |
| **Decision-Making Model** | Critique of zero-sum envy and strategic over-complexity in human play. | Behavioral decision theory, Prospect Theory (loss aversion), and emotion-centric models. | Moral rationality: truthfulness and dignity over opportunism and greed. | Pure instrumental greed produces collective ruin; durable social equilibria require moral constraints and transparent communication. |
| **Conflict Domains** | Trench warfare, biological mutualism, trade, and internal organization. | Multi-domain: land, sea, air, space, cyber, economic sanctions, and information warfare. | Civic life, agrarian labor, oral culture, inter-faith dialogue, and personal conscience. | Security extends beyond military dimensions to ideological, communal, and ethical resilience. |
| **Strategic Culture** | Universal mathematical and ecological properties of population dynamics. | Culturally divergent models: Western binary vs. Russian *sderzhivanie* and Chinese *weishe*. | Anatolian Sufi humanism: radical anti-sectarian inclusivity ("seventy-two nations"). | Conflict resolution requires deep cognitive and cultural empathy rather than imposing monocultural assumptions. |

---

## 🗂️ Complete Wiki Directory Map

```
GilgamisLLMWiki/
├── [Mounted External Library]                      # C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\
│   ├── Art/                                       # Ingested: 73010,cilt1pdf.pdf, 73011,cilt2pdf.pdf
│   └── AI/, History_/, Philosophy..., ...         # 42+ domain libraries (immutable, git-ignored)
├── .gitignore                                     # Excludes raw/, BOOKS/, and PDF binaries from GitHub sync
├── raw/                                           # Immutable local staging documents (git-ignored)
│   ├── Axelrod_Robert_The_Evolution_of_Cooperation.pdf
│   └── Deterrence in 21st Century Nuclear NetherlandsAnnualReviewO.pdf
├── wiki/                                          # Maintained knowledge base
│   ├── index.md                                   # Master index & full TOC
│   ├── log.md                                     # Ingestion & audit changelog
│   ├── index.html                                 # Dashboard web application copy
│   ├── dashboard_data.json                        # Structured JSON export
│   ├── books/                                     # Ingested book detail pages (3 pages)
│   │   ├── the-evolution-of-cooperation.md
│   │   ├── deterrence-in-the-21st-century.md
│   │   └── asik-borani-soz-insanin-aynasi.md
│   ├── authors/                                   # Author profile pages (26 pages)
│   │   ├── asik-borani.md                         ├── ibrahim-gosterir.md
│   │   ├── robert-axelrod.md                      ├── frans-osinga.md
│   │   ├── tim-sweijs.md                          ├── lawrence-freedman.md
│   │   ├── michael-mazarr.md                      ├── dmitry-adamsky.md
│   │   ├── dean-cheng.md                          ├── william-d-hamilton.md
│   │   ├── karl-mueller.md                        ├── alexey-arbatov.md
│   │   ├── sten-rynning.md                        ├── paul-van-hooft.md
│   │   ├── jorg-noll.md                           ├── eitan-shamir.md
│   │   ├── martijn-kitzen.md                      ├── francesco-giumelli.md
│   │   ├── stefan-soesanto.md                     ├── max-smeets.md
│   │   ├── alex-wilner.md                         ├── roy-lindelauf.md
│   │   ├── tom-bijlsma.md                         ├── samuel-zilincik.md
│   │   ├── isabelle-duyvesteyn.md                 └── paul-ducheine.md
│   ├── genres/                                    # Genre index pages (10 pages)
│   │   ├── anatolian-humanism.md                  ├── turkish-folk-literature.md
│   │   ├── poetry-and-poetics.md                  ├── game-theory.md
│   │   ├── strategic-studies.md                   ├── international-relations.md
│   │   ├── military-science.md                    ├── security-studies.md
│   │   ├── evolutionary-biology.md                └── political-science.md
│   └── themes/                                    # Core thematic concept pages (14 pages)
│       ├── universal-love-and-human-dignity.md    ├── social-critique-and-moral-conscience.md
│       ├── asik-and-minstrel-tradition.md         ├── cooperation-and-reciprocity.md
│       ├── tit-for-tat.md                         ├── shadow-of-the-future.md
│       ├── deterrence-and-coercion.md             ├── cross-domain-conflict.md
│       ├── nuclear-strategy-and-strategic-stability.md
│       ├── non-western-strategic-thought.md       ├── rationality-and-decision-making.md
│       ├── violent-non-state-actors.md            ├── hybrid-threats-and-cyber-warfare.md
│       └── evolution-of-strategies.md
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
- **Citation Format**: Every factual assertion and direct quote must cite its source and page/chapter (e.g., `(source: BOOKS/Art/73010,cilt1pdf.pdf, Intro, p. 39)`).
- **Index & Log Tracking**: Every addition or modification must update `wiki/index.md` and append an entry to `wiki/log.md`.
