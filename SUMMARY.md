# Gilgamis LLM Wiki — Ingestion & Library Summary

**Generated**: 2026-09-12  
**Knowledge Base Specification**: [GilgamisLLMWiki.md](GilgamisLLMWiki.md)  
**Interactive Dashboard**: [index.html](index.html) | [http://127.0.0.1:8080/index.html](http://127.0.0.1:8080/index.html)  
**Master Index**: [wiki/index.md](wiki/index.md)  
**Operations Log**: [wiki/log.md](wiki/log.md)  

---

## 1. Executive Overview

The **Gilgamis LLM Wiki** is a structured, interlinked personal knowledge base built following Andrej Karpathy's LLM Wiki pattern. This document summarizes the complete ingestion of foundational literature from both the primary mounted library (`C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS`) and local staging (`raw/`), establishing a multi-layered, cross-referenced literature corpus spanning game theory, strategic studies, evolutionary biology, international relations, military science, behavioral decision theory, and Anatolian minstrel literature. Both source repositories are strictly immutable and excluded from GitHub synchronization via `.gitignore`.

### Library Metrics at a Glance
- **Total Ingested Source Documents**: 3 volumes (1,931 total pages)
- **Total Generated Wiki Pages**: 53 interlinked markdown files
- **Interactive Web App**: [index.html](index.html) (with embedded data, fuzzy search, and modal inspectors)
- **Book Summary & Analysis Pages**: 3 ([books/](wiki/books/))
- **Author Profile Pages**: 26 ([authors/](wiki/authors/))
- **Genre Classification Pages**: 10 ([genres/](wiki/genres/))
- **Core Thematic Concept Pages**: 14 ([themes/](wiki/themes/))
- **Bidirectional Link Integrity**: 100% (0 broken links, 0 orphaned pages)
- **Source Compliance**: Complete textual citations referencing exact source files and page numbers; source repositories remain immutable and unmodified.

---

## 2. Ingested Books Summary

### Book 1: *The Evolution of Cooperation*
- **Author(s)**: Robert Axelrod (Chapter 5 with William D. Hamilton)
- **Publication**: Basic Books, 1984 (243 pp.)
- **Source File**: `raw/Axelrod_Robert_The_Evolution_of_Cooperation.pdf`
- **Wiki Page**: [wiki/books/the-evolution-of-cooperation.md](wiki/books/the-evolution-of-cooperation.md)
- **Primary Genres**: [[game-theory]], [[political-science]], [[evolutionary-biology]], [[strategic-studies]]
- **Core Themes**: [[cooperation-and-reciprocity]], [[shadow-of-the-future]], [[evolution-of-strategies]], [[rationality-and-decision-making]], [[tit-for-tat]]

#### Core Thesis & Findings
Axelrod investigates how cooperation can emerge and stabilize among egoists without central authority. Through two round-robin computer tournaments of the iterated Prisoner's Dilemma, Anatol Rapoport's **TIT FOR TAT** strategy (cooperate on move 1, then replicate the opponent's previous move) emerged victorious across diverse strategic environments.

Axelrod distilled the four fundamental attributes of successful strategic interaction:
1. **Be Nice**: Never defect first, preventing unnecessary conflict.
2. **Be Provocable / Retaliatory**: Punish unprovoked defection immediately to prevent exploitation.
3. **Be Forgiving**: Restore cooperation immediately once the opponent stops defecting to break conflict spirals.
4. **Be Clear**: Be transparent and predictable so counterparts can easily recognize and adapt to reciprocity.

---

### Book 2: *Söz İnsanın Aynasıdır (Cilt I & II)*
- **Author(s)**: [[asik-borani]] (Halil Çimen), [[ibrahim-gosterir]] (ed.)
- **Publication**: T.C. Çorum Valiliği İl Kültür ve Turizm Müdürlüğü, Yayın No: 19, 2020 (1,150 pp., 2 Vols.)
- **Source Files**: `BOOKS/Art/73010,cilt1pdf.pdf`, `BOOKS/Art/73011,cilt2pdf.pdf` (Mount: `C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\Art\`)
- **Wiki Page**: [wiki/books/asik-borani-soz-insanin-aynasi.md](wiki/books/asik-borani-soz-insanin-aynasi.md)
- **Primary Genres**: [[turkish-folk-literature]], [[anatolian-humanism]], [[poetry-and-poetics]]
- **Core Themes**: [[universal-love-and-human-dignity]], [[social-critique-and-moral-conscience]], [[asik-and-minstrel-tradition]], [[rationality-and-decision-making]], [[non-western-strategic-thought]]

#### Core Thesis & Findings
The complete poetic and philosophical works of Âşık Borani (Halil Çimen, 1943–2020), one of Anatolia's greatest contemporary bards (*halk ozanı*). Spanning 10 comprehensive thematic parts across two volumes:
1. **Elinde Gül Olsun Dilinde Türkü** & **İnsana Yolculuk**: The saz as moral healing instrument; the human conscience as the reflection of divine truth (*Natık-ı Kuran*).
2. **Fadime'ye Mektuplar** & **Fadime'ye Son Mektuplar**: Lyrical epistolary cycle to "Fadime," symbolizing the dignity and resilience of rural Anatolian womanhood.
3. **Âdem'in Aynası** & **Söz İnsana Söylenir**: Meditations on communicative ethics (*söz insanın aynasıdır*), universal human rights, and rejection of all sectarian and racial divisions.
4. **Bozkırın Gülleri**, **Sevgiye Davet**, & **Serbest Nazım**: Steppe culture, universal appeals for fraternity, and experiments with modern free-verse poetics.
5. **Toplumcu Gerçekçilik & Taşlama**: Uncompromising satire exposing bureaucratic corruption, greed, and exploitation (*"Kim çalarsa çalsın adı hırsızdır"*).

---

### Book 3: *Deterrence in the 21st Century — Insights from Theory and Practice*
- **Editors**: Frans Osinga, Tim Sweijs (NL ARMS 2020 / T.M.C. Asser Press / Springer, 2021, 538 pp.)
- **Source File**: `raw/Deterrence in 21st Century Nuclear NetherlandsAnnualReviewO.pdf`
- **Wiki Page**: [wiki/books/deterrence-in-the-21st-century.md](wiki/books/deterrence-in-the-21st-century.md)
- **Primary Genres**: [[strategic-studies]], [[military-science]], [[international-relations]], [[security-studies]], [[game-theory]]
- **Core Themes**: [[deterrence-and-coercion]], [[nuclear-strategy-and-strategic-stability]], [[cross-domain-conflict]], [[non-western-strategic-thought]], [[rationality-and-decision-making]], [[hybrid-threats-and-cyber-warfare]], [[violent-non-state-actors]]

#### Core Thesis & Findings
Spanning 26 chapters across six thematic parts, this volume provides a comprehensive analysis of the modern renaissance of deterrence theory and its adaptation from Cold War bipolarity to contemporary multipolar, multi-domain, and technologically diffuse environments.

#### Six Thematic Dimensions
1. **Concepts of Deterrence (Part I)**:
   - Historical progression through four scholarly waves (Freedman).
   - Core fundamentals: Deterrence by Denial vs. Deterrence by Punishment, the 3C framework (Capability, Credibility, Communication), and the vital necessity of **Assurances** (Mazarr).
   - NATO's return to collective territorial defense (Rynning) and tripwire deterrence via enhanced Forward Presence (eFP) (Noll et al.).
   - The enduring role of conventional deterrence (Mueller) and extended nuclear guarantees (van Hooft).
   - Cross-Domain Deterrence (CDD) theoretical modeling and asymmetric trade-offs (Sweijs & Zilincik).
2. **Non-Western Strategic Thought (Part II)**:
   - Russian *Sderzhivanie*: A holistic, continuous process spanning peacetime, crisis, and war, blending non-military coercion, information warfare, deception (*maskirovka*), and nuclear signaling (Adamsky).
   - Chinese *Weishe*: Proactive coercion combining the "Three Warfares" (psychological, media, legal) with space/cyber capabilities to compel submission without kinetic war (Cheng).
   - Regional paradigms: Japanese dynamic defense (Katagiri), India-Pakistan Stability-Instability Paradox (Aarten), and Iran's forward-defense proxy network in Syria (Ahmadian & Mohseni).
3. **Deterrence of Non-State Actors (Part III)**:
   - Refutes the claim that non-state actors are undeterrable; analyzes Israel's cumulative deterrence ("mowing the lawn") against Hamas and Hezbollah (Shamir).
   - Localised counterinsurgency deterrence tailored to tribal/village kinship systems (Kitzen & van Kuijck).
   - Russian deterrence of democratic revolts (Rothman) and coercive diplomacy in peace operations (Jakobsen).
4. **New Instruments and Domains (Part IV)**:
   - Targeted economic sanctions and asset freezes as coercive signaling tools (Giumelli).
   - Institutional and societal resilience (e.g., MH17 Joint Investigation Team, social capital) as deterrence by denial against hybrid warfare (van Doorn & Brinkel).
   - Cyber deterrence dilemmas: attribution latency, exploit perishability, and ambiguous thresholds (Soesanto & Smeets).
   - Artificial intelligence, autonomous swarms, and hyper-coercion compressing decision cycles (Wilner & Babb).
5. **Rationality, Psychology, Emotions & Law (Part V)**:
   - Algorithmic game theory and automated command-and-control stability risks (Lindelauf).
   - Behavioral decision theory: Cognitive heuristics (anchoring, confirmation, availability) and Kahneman & Tversky's Prospect Theory (loss aversion causing risk-seeking behavior in the domain of losses) (Bijlsma).
   - Emotion-centric deterrence model: Fear, anger, pride, and humiliation driving crisis escalation (Zilincik & Duyvesteyn).
   - International legal architecture: Mapping deterrence tools to UN Charter Article 51 self-defence, countermeasures, retorsion, and necessity (Ducheine & Pijpers).
6. **Synthesis (Part VI)**:
   - Integrated framework by Sweijs & Osinga calling for tailored, cross-domain deterrence combining military power with societal resilience and cognitive empathy.

---

## 3. Cross-Comparative Thematic Insights

| Dimension | Axelrod (*Evolution of Cooperation*) | Osinga & Sweijs (*Deterrence in the 21st Century*) | Cross-Wiki Synthesis |
| Dimension | Axelrod (*Evolution of Cooperation*) | Osinga & Sweijs (*Deterrence in the 21st Century*) | Âşık Borani (*Söz İnsanın Aynasıdır*) | Cross-Wiki Synthesis |
| :--- | :--- | :--- | :--- | :--- |
| **Strategic Mechanism** | Reciprocity (TIT FOR TAT): nice, retaliatory, forgiving, clear. | Deterrence by punishment/denial, credible threats, and assurances. | Unconditional love (*sevgi ilimi*), communal empathy, and ethical conscience. | Retaliation without forgiveness produces destructive spirals; strategic deterrence needs positive assurances, while social sustainability requires an ethical baseline of human dignity. |
| **Time Horizon** | Shadow of the future ($w$): large $w$ sustains cooperation under anarchy. | Strategic stability and arms control treaties preserve long-term predictability. | Cultural memory, generational poetry, and existential transience (*ölüm nikâhı*). | Long horizons disincentivize cheating; bards and strategic regimes both serve to preserve collective stability across generational time. |
| **Decision-Making Model** | Critique of zero-sum envy and strategic over-complexity in human play. | Behavioral decision theory, Prospect Theory (loss aversion), and emotion-centric models. | Moral rationality: truthfulness and dignity over opportunism and greed. | Pure instrumental greed produces collective ruin; durable social equilibria require moral constraints and transparent communication. |
| **Conflict Domains** | Trench warfare, biological mutualism, trade, and internal organization. | Multi-domain: land, sea, air, space, cyber, economic sanctions, and information warfare. | Civic life, agrarian labor, oral culture, inter-faith dialogue, and personal conscience. | Security extends beyond military dimensions to ideological, communal, and ethical resilience. |
| **Strategic Culture** | Universal mathematical and ecological properties of population dynamics. | Culturally divergent models: Western binary vs. Russian *sderzhivanie* and Chinese *weishe*. | Anatolian Sufi humanism: radical anti-sectarian inclusivity ("seventy-two nations"). | Conflict resolution requires deep cognitive and cultural empathy rather than imposing monocultural assumptions. |

---

## 4. Complete Wiki Directory & Link Map

### Web Dashboard
- [index.html](index.html) — Standalone single-page application.

### Books (`wiki/books/`)
- [the-evolution-of-cooperation.md](wiki/books/the-evolution-of-cooperation.md)
- [deterrence-in-the-21st-century.md](wiki/books/deterrence-in-the-21st-century.md)
- [asik-borani-soz-insanin-aynasi.md](wiki/books/asik-borani-soz-insanin-aynasi.md)

### Authors (`wiki/authors/`)
- [asik-borani.md](wiki/authors/asik-borani.md) — [ibrahim-gosterir.md](wiki/authors/ibrahim-gosterir.md)
- [robert-axelrod.md](wiki/authors/robert-axelrod.md) — [william-d-hamilton.md](wiki/authors/william-d-hamilton.md)
- [frans-osinga.md](wiki/authors/frans-osinga.md) — [tim-sweijs.md](wiki/authors/tim-sweijs.md)
- [lawrence-freedman.md](wiki/authors/lawrence-freedman.md) — [michael-mazarr.md](wiki/authors/michael-mazarr.md)
- [dmitry-adamsky.md](wiki/authors/dmitry-adamsky.md) — [dean-cheng.md](wiki/authors/dean-cheng.md)
- [karl-mueller.md](wiki/authors/karl-mueller.md) — [alexey-arbatov.md](wiki/authors/alexey-arbatov.md)
- [sten-rynning.md](wiki/authors/sten-rynning.md) — [paul-van-hooft.md](wiki/authors/paul-van-hooft.md)
- [jorg-noll.md](wiki/authors/jorg-noll.md) — [eitan-shamir.md](wiki/authors/eitan-shamir.md)
- [martijn-kitzen.md](wiki/authors/martijn-kitzen.md) — [francesco-giumelli.md](wiki/authors/francesco-giumelli.md)
- [stefan-soesanto.md](wiki/authors/stefan-soesanto.md) — [max-smeets.md](wiki/authors/max-smeets.md)
- [alex-wilner.md](wiki/authors/alex-wilner.md) — [roy-lindelauf.md](wiki/authors/roy-lindelauf.md)
- [tom-bijlsma.md](wiki/authors/tom-bijlsma.md) — [samuel-zilincik.md](wiki/authors/samuel-zilincik.md)
- [isabelle-duyvesteyn.md](wiki/authors/isabelle-duyvesteyn.md) — [paul-ducheine.md](wiki/authors/paul-ducheine.md)

### Genres (`wiki/genres/`)
- [anatolian-humanism.md](wiki/genres/anatolian-humanism.md)
- [turkish-folk-literature.md](wiki/genres/turkish-folk-literature.md)
- [poetry-and-poetics.md](wiki/genres/poetry-and-poetics.md)
- [game-theory.md](wiki/genres/game-theory.md)
- [strategic-studies.md](wiki/genres/strategic-studies.md)
- [international-relations.md](wiki/genres/international-relations.md)
- [military-science.md](wiki/genres/military-science.md)
- [security-studies.md](wiki/genres/security-studies.md)
- [evolutionary-biology.md](wiki/genres/evolutionary-biology.md)
- [political-science.md](wiki/genres/political-science.md)

### Themes (`wiki/themes/`)
- [universal-love-and-human-dignity.md](wiki/themes/universal-love-and-human-dignity.md)
- [social-critique-and-moral-conscience.md](wiki/themes/social-critique-and-moral-conscience.md)
- [asik-and-minstrel-tradition.md](wiki/themes/asik-and-minstrel-tradition.md)
- [cooperation-and-reciprocity.md](wiki/themes/cooperation-and-reciprocity.md)
- [tit-for-tat.md](wiki/themes/tit-for-tat.md)
- [shadow-of-the-future.md](wiki/themes/shadow-of-the-future.md)
- [deterrence-and-coercion.md](wiki/themes/deterrence-and-coercion.md)
- [cross-domain-conflict.md](wiki/themes/cross-domain-conflict.md)
- [nuclear-strategy-and-strategic-stability.md](wiki/themes/nuclear-strategy-and-strategic-stability.md)
- [non-western-strategic-thought.md](wiki/themes/non-western-strategic-thought.md)
- [rationality-and-decision-making.md](wiki/themes/rationality-and-decision-making.md)
- [violent-non-state-actors.md](wiki/themes/violent-non-state-actors.md)
- [hybrid-threats-and-cyber-warfare.md](wiki/themes/hybrid-threats-and-cyber-warfare.md)
- [evolution-of-strategies.md](wiki/themes/evolution-of-strategies.md)

---

## 5. Operations & Audit Log Summary

All ingestion operations, directory scaffolding, link verification, and audit traces are permanently recorded in [wiki/log.md](wiki/log.md).
