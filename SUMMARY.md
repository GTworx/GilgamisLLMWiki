# Gilgamis LLM Wiki — Ingestion & Library Summary

**Generated**: 2026-11-01  
**Knowledge Base Specification**: [GilgamisLLMWiki.md](GilgamisLLMWiki.md)  
**Interactive Dashboard**: [index.html](index.html) | [http://127.0.0.1:8080/index.html](http://127.0.0.1:8080/index.html)  
**Master Index**: [wiki/index.md](wiki/index.md)  
**Operations Log**: [wiki/log.md](wiki/log.md)  

---

## 1. Executive Overview

The **Gilgamis LLM Wiki** is a structured, interlinked personal knowledge base built following Andrej Karpathy's LLM Wiki pattern. This document summarizes the complete ingestion of foundational literature from both the primary mounted library (`C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\`) and local staging (`raw/`), establishing an expansive, cross-referenced literature corpus spanning game theory, topological social choice, strategic studies, executive leadership, organizational psychology, strategic communication, evolutionary biology, Anatolian minstrel literature, classical archaeology, archaeoastronomy, and alternative prehistory. Both source repositories are strictly immutable and excluded from GitHub synchronization via `.gitignore`.

### Library Metrics at a Glance
- **Total Ingested Works**: 20 distinct intellectual works (across 22 volumes and ~8,900 pages)
- **Total Generated Wiki Pages**: 137 interlinked markdown files (135 entity pages + `index.md` & `log.md`)
- **Interactive Web App**: [index.html](index.html) (with embedded data, fuzzy search, and modal inspectors)
- **Book Summary & Analysis Pages**: 20 ([books/](wiki/books/))
- **Author Profile Pages**: 48 ([authors/](wiki/authors/))
- **Genre Classification Pages**: 33 ([genres/](wiki/genres/))
- **Core Thematic Concept Pages**: 34 ([themes/](wiki/themes/))
- **Bidirectional Link Integrity**: 100% (0 broken links, 0 orphaned pages)
- **Source Compliance**: Complete textual citations referencing exact source files and page numbers; source repositories remain immutable and unmodified.

---

## 2. Ingested Books Summary by Category

### Category A: Strategic Studies, Game Theory & Topological Social Choice
1. **[[the-evolution-of-cooperation]]** ([[robert-axelrod]] & [[william-d-hamilton]], 1984, 243 pp.)  
   Iterated Prisoner's Dilemma, TIT FOR TAT reciprocity, nice/provocable/forgiving/clear heuristics, and the shadow of the future ($w$).
2. **[[deterrence-in-the-21st-century]]** (eds. [[frans-osinga]] & [[tim-sweijs]], 2021, 538 pp.)  
   Cross-domain deterrence, nuclear stability, Russian *sderzhivanie*, Chinese *weishe*, hybrid conflict, cyber deterrence, and emotion-centric strategy.
3. **[[the-non-orientable-topology-of-condorcets-paradox]]** ([[ori-livson]], [[siddharth-pritam]], & [[mikhail-prokopenko]], 2026, 27 pp., `arXiv:2601.07283v6`)  
   Resolves Chichilnisky's (1980) conjecture by proving that valid (intransitive) preference cycles form orientable surfaces ($S^1 \times [0,1]$ and $S^2$) whereas contradictory (transitive) Condorcet cycles form non-orientable surfaces (Klein bottle $K$ and real projective plane $\mathbb{RP}^2$), reformulating Arrow's Impossibility Theorem via manifold orientability.

### Category B: Executive Leadership, Organizational Psychology & Strategic Communication (2026 Cohort)
4. **[[influencing-leaders]]** ([[james-e-lukaszewski]] & [[helio-fred-garcia]], 2026, 243 pp.)  
   Transitioning from technical "doer" to C-suite trusted advisor; decoding executive anxiety, navigating the "No-Friendship Zone," the "Language of Done," the "Single-Page Rule," and the "Rule of Threes."
5. **[[the-adaptability-advantage]]** ([[john-sanei]], 2026, 189 pp.)  
   Applied neuroscience of **Adaptive Intelligence (AQ)**; clearing **Emotional Debt**, rewiring survival reactivity into a *"Calm, Clear, and Curious"* nervous system, and partnering with exponential AI.
6. **[[rapid-reculturing]]** ([[alex-bailey]] & [[kerri-oneill]], 2026, 302 pp.)  
   **Organizational Rewilding** across Four Pillars (**Human**, **Connect**, **Simplicity**, **Empowerment**), the five-step **HUMAN Model**, the **5-5-5 Coaching Conversation**, and human-centered AI workplace transformation.
7. **[[leading-for-tomorrow]]** (eds. [[scott-barry-kaufman]] & [[chris-shipley]], Foreword by [[rita-mcgrath]], 2026, 355 pp.)  
   26-chapter anthology uniting transient competitive advantage, humanistic self-transcendence, generative AI co-piloting, [[amy-c-edmondson]]'s **intelligent failure** & psychological safety, and [[jonathan-haidt]]'s institutional trust across the "Anxious Generation."
8. **[[valuable-and-visible]]** ([[vanessa-errecarte]], 2026, 273 pp.)  
   **Service-First Personal Branding** and the **EPIC Method** (**E**stablish, **P**ackage, **I**nform, **C**ultivate); **TRUTH** positioning, **ABCs of Framework Creation**, **The FaceTime Effect**, and reframing expert silence as *"unintentional selfishness."*

### Category C: Anatolian Literature & Republican Historiography
9. **[[asik-borani-soz-insanin-aynasi]]** ([[asik-borani]] & [[ibrahim-gosterir]], 2020, 1,150 pp., 2 Vols.)  
   Complete poetic compendium of Âşık Borani; synthesis of Sufi humanism, pastoral lyricism, social realism, and anti-sectarian egalitarianism.
10. **[[cumhuriyet-donemi-arkeoloji-politikalari-ve-ekrem-akurgal]]** ([[erdal-polat]], 2024, 22 pp.)  
    Atatürk's archaeological mobilization ("Scientific Republic"), Turkish Historical Society (TTK), DTCF, and [[ekrem-akurgal]]'s Anatolian Civilizations Synthesis proving that Greek art derived from Anatolian cultures.

### Category D: Archaeoastronomy, Catastrophism & Lost Civilizations (Graham Hancock et al.)
11. **[[fingerprints-of-the-gods]]** ([[graham-hancock]], 1995, 490 pp.)  
    Antediluvian cartography (Piri Reis map), Tiwanaku, precession of the equinoxes in global myth, Giza mathematics, and earth-crust displacement.
12. **[[keeper-of-genesis]]** ([[graham-hancock]] & [[robert-bauval]], 1996, 331 pp.)  
    Geological pluvial erosion of the Great Sphinx ([[robert-schoch]]), Orion Correlation Theory (OCT), the astronomical epoch of 10,500 BC (*Zep Tepi*), and Giza's star shafts.
13. **[[the-mars-mystery]]** ([[graham-hancock]], [[robert-bauval]], [[john-grigsby]], 1998, 252 pp.)  
    Comparative planetary catastrophism between Earth and Mars, the Taurid meteor complex, and Cydonia landforms.
14. **[[underworld-mysterious-origins-of-civilization]]** ([[graham-hancock]], 2002, 796 pp.)  
    Post-glacial sea-level rise inundating 25 million km² of land; marine archaeological surveys in Dwarka, Gulf of Cambay (Khambhat), Malta, and Yonaguni.
15. **[[supernatural-meetings-with-the-ancient-teachers-of-mankind]]** ([[graham-hancock]], 2005, 488 pp.)  
    The Upper Paleolithic creative explosion (~35,000 BP), David Lewis-Williams's neuropsychological cave art model, Ayahuasca shamanism, and DMT entity encounters.
16. **[[lost-knowledge-of-the-ancients]]** (ed. [[glenn-kreisberg]], 2010, 178 pp.)  
    Anthology featuring Hancock, Bauval, Schoch, and West; acoustic engineering, quantum philosophy, and critique of institutional archaeological dogma.
17. **[[the-master-game]]** ([[graham-hancock]] & [[robert-bauval]], 2011, 654 pp.)  
    The Hermetic-Gnostic underground stream, Templars, Giordano Bruno, Freemasonry, and solar-talismanic city planning in Paris and Washington, D.C.
18. **[[war-god-nights-of-the-witch]]** ([[graham-hancock]], 2013, 501 pp.)  
    Historical novel of the 1519 Spanish invasion of Mexico; Cortés, Moctezuma II, Malinal, and the metaphysical confrontation between Christian zeal and Aztec blood sacrifice.
19. **[[magicians-of-the-gods]]** ([[graham-hancock]], 2015, 444 pp.)  
    The Younger Dryas comet impact hypothesis (~12,800 BP), Göbekli Tepe (Pillar 43 date stamp), deliberate burial of megalithic temples, and Gunung Padang.
20. **[[america-before-the-key-to-earths-lost-civilization]]** ([[graham-hancock]], 2019, 668 pp.)  
    Pre-Clovis antiquity (Cerutti Mastodon 130,000 BP), Amazonian *terra preta* and geoglyphs, Australasian DNA in Brazil, and Serpent Mound archaeoastronomy.

---

## 3. Thematic Synthesis Across Ingested Fields

| Dimension | Strategic Studies, Game Theory & Social Choice | Leadership, Org Psychology & Communication | Anatolian Humanism & Historiography | Archaeoastronomy & Catastrophism |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Authors** | Axelrod, Hamilton, Osinga, Sweijs, Freedman, Livson, Pritam, Prokopenko | Lukaszewski, Garcia, Sanei, Bailey, O'Neill, Kaufman, Shipley, McGrath, Edmondson, Haidt, Errecarte | Âşık Borani, İbrahim Gösterir, Ekrem Akurgal, Erdal Polat | Graham Hancock, Robert Bauval, Robert Schoch, John Anthony West |
| **Systemic Fragility** | Nuclear escalation, cyber attribution dilemmas, non-orientable voting cycles ($K, \mathbb{RP}^2$) | Emotional debt, bureaucratic process debt, AI displacement anxiety, C-suite isolation | Societal corruption, bureaucratic tyranny, loss of moral conscience | Planetary comet impacts, rapid glaciation, catastrophic 120m sea-level rise |
| **Resilience Mechanisms** | TIT FOR TAT reciprocity, shadow of the future ($w$), credible assurances | Adaptive Intelligence (AQ), Organizational Rewilding, psychological safety, Constructive Candor, EPIC service branding | Universal love (*sevgi ilimi*), civic honesty, scientific archaeology | Preserving knowledge across precessional epochs and megalithic archives |
