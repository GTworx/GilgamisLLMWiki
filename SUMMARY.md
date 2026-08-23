# Gilgamis LLM Wiki — Ingestion & Library Summary

**Generated**: 2026-08-23  
**Knowledge Base Specification**: [GilgamisLLMWiki.md](GilgamisLLMWiki.md)  
**Interactive Dashboard**: [index.html](index.html) | [http://127.0.0.1:8080/index.html](http://127.0.0.1:8080/index.html)  
**Master Index**: [wiki/index.md](wiki/index.md)  
**Operations Log**: [wiki/log.md](wiki/log.md)  

---

## 1. Executive Overview

The **Gilgamis LLM Wiki** is a structured, interlinked personal knowledge base built following Andrej Karpathy's LLM Wiki pattern. This document summarizes the complete ingestion of the foundational volumes located in `raw/`, establishing a multi-layered, cross-referenced literature corpus spanning game theory, strategic studies, evolutionary biology, international relations, military science, and behavioral decision theory.

### Library Metrics at a Glance
- **Total Ingested Source Documents**: 2 volumes (781 total pages)
- **Total Generated Wiki Pages**: 46 interlinked markdown files
- **Interactive Web App**: [index.html](index.html) (with embedded data and offline search)
- **Book Summary & Analysis Pages**: 2 ([books/](wiki/books/))
- **Author Profile Pages**: 24 ([authors/](wiki/authors/))
- **Genre Classification Pages**: 7 ([genres/](wiki/genres/))
- **Core Thematic Concept Pages**: 11 ([themes/](wiki/themes/))
- **Bidirectional Link Integrity**: 100% (0 broken links, 0 orphaned pages)
- **Source Compliance**: Complete textual citations referencing exact source files and page numbers; `raw/` directory remains immutable and unmodified.

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

#### Key Case Studies & Applications
- **WWI Trench Warfare ("Live-and-Let-Live")**: Tacit non-aggression pacts emerged between British and German infantry due to repeated, indefinite interactions ($w$), until central command mandated verifiable raids with casualties.
- **Biological Systems**: Reciprocal altruism evolves naturally without conscious intent or high intelligence (e.g., cleaner fish mutualism, bacteria, fig wasps) when spatial clustering and repeated interactions are present.
- **Advice for Institutional Designers**: Enlarge the shadow of the future ($w$), alter payoffs, teach reciprocity, and improve recognition/reputation tracking.

---

### Book 2: *Deterrence in the 21st Century — Insights from Theory and Practice*
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
| :--- | :--- | :--- | :--- |
| **Strategic Mechanism** | Reciprocity (TIT FOR TAT): nice, retaliatory, forgiving, clear. | Deterrence by punishment/denial, credible threats, and assurances. | Retaliation without forgiveness leads to endless conflict spirals; deterrence stability requires positive reciprocity (assurances). |
| **Time Horizon** | Shadow of the future ($w$): large $w$ sustains cooperation under anarchy. | Strategic stability and arms control treaties preserve long-term predictability. | High-speed technologies (hypersonics, AI decision loops) dangerously compress time horizons, undermining both cooperation and deterrence. |
| **Decision-Making Model** | Critique of zero-sum envy and strategic over-complexity in human play. | Behavioral decision theory, Prospect Theory (loss aversion), and emotion-centric models. | Actors under existential threat become risk-seeking in the domain of losses; hyper-rational models fail to predict real-world crises. |
| **Conflict Domains** | Trench warfare, biological mutualism, trade, and internal organization. | Multi-domain: land, sea, air, space, cyber, economic sanctions, and information warfare. | Cross-domain asymmetric offsetting creates severe calibration hazards and attribution bottlenecks. |
| **Strategic Culture** | Universal mathematical and ecological properties of population dynamics. | Culturally divergent models: Western binary vs. Russian *sderzhivanie* and Chinese *weishe*. | Effective strategic engagement requires cognitive empathy to avoid fatal perceptual misalignment. |

---

## 4. Complete Wiki Directory & Link Map

### Web Dashboard
- [index.html](index.html) — Standalone single-page application.

### Books (`wiki/books/`)
- [the-evolution-of-cooperation.md](wiki/books/the-evolution-of-cooperation.md)
- [deterrence-in-the-21st-century.md](wiki/books/deterrence-in-the-21st-century.md)

### Authors (`wiki/authors/`)
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
- [game-theory.md](wiki/genres/game-theory.md)
- [strategic-studies.md](wiki/genres/strategic-studies.md)
- [international-relations.md](wiki/genres/international-relations.md)
- [military-science.md](wiki/genres/military-science.md)
- [security-studies.md](wiki/genres/security-studies.md)
- [evolutionary-biology.md](wiki/genres/evolutionary-biology.md)
- [political-science.md](wiki/genres/political-science.md)

### Themes (`wiki/themes/`)
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
