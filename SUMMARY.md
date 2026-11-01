# Gilgamis LLM Wiki — Ingestion & Library Summary

**Generated**: 2026-11-01  
**Knowledge Base Specification**: [GilgamisLLMWiki.md](GilgamisLLMWiki.md)  
**Interactive Dashboard**: [index.html](index.html) | [http://127.0.0.1:8080/index.html](http://127.0.0.1:8080/index.html)  
**Master Index**: [wiki/index.md](wiki/index.md)  
**Operations Log**: [wiki/log.md](wiki/log.md)  
**Local Ollama (`qwen3.8`) CLI**: [.agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py](.agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py)  

---

## 1. Executive Overview

The **Gilgamis LLM Wiki** is a structured, interlinked personal knowledge base built following Andrej Karpathy's LLM Wiki pattern and integrated with a local **Ollama (`qwen3.8:latest` / `qwen3.8:27b`)** agentic execution and multimodal Vision OCR pipeline. This document summarizes the complete ingestion of foundational literature from both the primary mounted library (`C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\`) and local staging (`raw/`), establishing an expansive, cross-referenced corpus spanning game theory, topological social choice, comparative democratic history (from third-millennium BC Mesopotamia to post-1945 monitory democracy), strategic studies, semiconductor geopolitics, military human performance enhancement, executive leadership, organizational psychology, evolutionary biology and memetics, Anatolian minstrel literature, classical archaeology, paleoclimatology, archaeoastronomy, and alternative prehistory.

### Library Metrics at a Glance
- **Total Ingested Works**: 29 distinct intellectual works (across 33 volumes and ~11,200 pages)
- **Total Generated Wiki Pages**: 170 interlinked markdown files (168 entity pages + `index.md` & `log.md`)
- **Interactive Web App**: [index.html](index.html) (with embedded data, fuzzy search, and modal inspectors)
- **Book Summary & Analysis Pages**: 29 ([books/](wiki/books/))
- **Author Profile Pages**: 64 ([authors/](wiki/authors/))
- **Genre Classification Pages**: 34 ([genres/](wiki/genres/))
- **Core Thematic Concept Pages**: 41 ([themes/](wiki/themes/))
- **Bidirectional Link Integrity**: 100% (0 broken links, 0 orphaned pages, 0 unindexed pages)
- **Source Compliance**: Complete textual citations referencing exact source files and page numbers; source repositories remain immutable and unmodified.

---

## 2. Ingested Books Summary by Category

### Category A: Strategic Studies, Semiconductor Geopolitics, Military Science, Game Theory & Evolutionary Biology
1. **[[the-evolution-of-cooperation]]** ([[robert-axelrod]] & [[william-d-hamilton]], 1984, 243 pp.)  
   Iterated Prisoner's Dilemma, TIT FOR TAT reciprocity, nice/provocable/forgiving/clear heuristics, and the shadow of the future ($w$).
2. **[[the-selfish-gene]]** ([[richard-dawkins]], 1976 / 2006 30th Anniversary Ed., 385 pp.)  
   Gene-centric evolution (immortal replicators vs. organismal survival machines), Maynard Smith's Evolutionarily Stable Strategies (ESS), Hamilton's kin selection ($rB > C$), coining cultural **memes** (Ch. 11), *"Nice Guys Finish First"* (Ch. 12 on Axelrod's TIT FOR TAT), and the Extended Phenotype (Ch. 13).
3. **[[developing-the-super-soldier-enhancing-military-performance]]** (eds. [[william-g-braun-iii]], [[stefanie-von-hlatky]], & [[kim-richard-nossal]], 2017, 132 pp.)  
   U.S. Army Research Laboratory **"Quantified Soldier"** brain-network telemetry, the capability–cohesion paradox across bonding/bridging social capital, special-operations stress resilience, Aristotelian martial courage, and *"People First, Mission Always."*
4. **[[deterrence-in-the-21st-century]]** (eds. [[frans-osinga]] & [[tim-sweijs]], 2021, 538 pp.)  
   Cross-domain deterrence, nuclear stability, Russian *sderzhivanie*, Chinese *weishe*, hybrid conflict, cyber deterrence, and emotion-centric strategy.
5. **[[chip-war-the-fight-for-the-worlds-most-critical-technology]]** ([[chris-miller]] & [[morris-chang]], 2022, 473 pp.)  
   54-chapter geopolitical history of the integrated circuit from Bell Labs, Fairchild, Texas Instruments, and the Pentagon's **Offset Strategies** to [[morris-chang]]'s pure-play foundry at **TSMC**, **ASML**'s extreme ultraviolet (EUV) lithography monopoly, weaponized interdependence, and the Taiwan Strait Dilemma.

### Category B: Comparative Democratic History, Constitutional Neutrality & Topological Social Choice
6. **[[democracy-in-america]]** ([[alexis-de-tocqueville]], 1835/1840, Vols. I & II, 836 pp. / 454 pp.)  
   The 700-year march of the "equality of conditions," New England township self-government, judicial review, the **tyranny of the majority**, **individualism**, the **art of civil association**, *self-interest rightly understood*, and the prophecy of administrative **soft despotism**.
7. **[[kalven-committee-report-on-the-universitys-role-in-political-and-social-action]]** ([[harry-kalven-jr]], 1967, 3 pp.)  
   University of Chicago foundational statement on institutional neutrality: *"The university is the home and sponsor of critics; it is not itself the critic"*—explaining why scholarly communities cannot resort to majority vote on public issues without censoring minority inquiry.
8. **[[the-first-democracies-early-popular-government-outside-athens]]** ([[eric-w-robinson]], reviewed by [[richard-j-evans]], 1997/1998, 3 pp. — **transcribed via `qwen3.8:latest` Vision OCR**)  
   Dethrones Athenocentrism inside Classical Greek history by documenting seventeen archaic Greek popular governments (*demokratiai*) outside Athens prior to 480 BC (including Chios, Argos, Ambracia, Cyrene, Mantineia, Naxos, Samos, and Syracuse).
9. **[[the-life-and-death-of-democracy-and-monitory-democracy]]** ([[john-keane]], 2009, 4 pp.)  
   Three-epoch global history of democracy: **Assembly Democracy** (from c. 2500 BC Mesopotamia), **Representative Democracy**, and post-1945 **Monitory Democracy** (continuous extra-parliamentary power-scrutiny via 100+ watchdog mechanisms).
10. **[[the-secret-history-of-democracy-primitive-democracy]]** (eds. [[benjamin-isakhan]] & [[stephen-stockwell]], and [[thorkild-jacobsen]], 1943/2011, 30 pp.)  
    Proves that third-millennium BC Mesopotamian city-states operated bicameral popular assemblies (*ukkin*/*puhrum*) of elders (*abba*) and free citizens (*guruš*) where **King Gilgamesh of Uruk** required assembly consent before waging war, Kish elected Ipurkish as king, and Urukagina proclaimed *amargi* ("liberty", c. 2350 BC).
11. **[[the-non-orientable-topology-of-condorcets-paradox]]** ([[ori-livson]], [[siddharth-pritam]], & [[mikhail-prokopenko]], 2026, 27 pp., `arXiv:2601.07283v6`)  
    Resolves Chichilnisky's (1980) conjecture by proving that valid (intransitive) preference cycles form orientable surfaces ($S^1 \times [0,1]$ and $S^2$) whereas contradictory (transitive) Condorcet cycles form non-orientable surfaces (Klein bottle $K$ and real projective plane $\mathbb{RP}^2$), reformulating Arrow's Impossibility Theorem via manifold orientability.

### Category C: Executive Leadership, Organizational Psychology & Strategic Communication (2026 Cohort)
12. **[[influencing-leaders]]** ([[james-e-lukaszewski]] & [[helio-fred-garcia]], 2026, 243 pp.)  
    Transitioning from technical "doer" to C-suite trusted advisor; decoding executive anxiety, navigating the "No-Friendship Zone," the "Language of Done," the "Single-Page Rule," and the "Rule of Threes."
13. **[[the-adaptability-advantage]]** ([[john-sanei]], 2026, 189 pp.)  
    Applied neuroscience of **Adaptive Intelligence (AQ)**; clearing **Emotional Debt**, rewiring survival reactivity into a *"Calm, Clear, and Curious"* nervous system, and partnering with exponential AI.
14. **[[rapid-reculturing]]** ([[alex-bailey]] & [[kerri-oneill]], 2026, 302 pp.)  
    **Organizational Rewilding** across Four Pillars (**Human**, **Connect**, **Simplicity**, **Empowerment**), the five-step **HUMAN Model**, the **5-5-5 Coaching Conversation**, and human-centered AI workplace transformation.
15. **[[leading-for-tomorrow]]** (eds. [[scott-barry-kaufman]] & [[chris-shipley]], Foreword by [[rita-mcgrath]], 2026, 355 pp.)  
    26-chapter anthology uniting transient competitive advantage, humanistic self-transcendence, generative AI co-piloting, [[amy-c-edmondson]]'s **intelligent failure** & psychological safety, and [[jonathan-haidt]]'s institutional trust across the "Anxious Generation."
16. **[[valuable-and-visible]]** ([[vanessa-errecarte]], 2026, 273 pp.)  
    **Service-First Personal Branding** and the **EPIC Method** (**E**stablish, **P**ackage, **I**nform, **C**ultivate); **TRUTH** positioning, **ABCs of Framework Creation**, **The FaceTime Effect**, and reframing expert silence as *"unintentional selfishness."*

### Category D: Anatolian Literature, Harappan Geoarchaeology & Republican Historiography
17. **[[oxygen-isotope-in-archaeological-bioapatites-from-india-harappan-civilization]]** ([[anindya-sarkar]] & [[vasant-shinde]] et al., 2016, *Scientific Reports* 6:26555, 9 pp.)  
    Mammalian tooth/bone bioapatite $\delta^{18}\text{O}_w$ paleomonsoon record and OSL/$^{14}\text{C}$ dates from Trench YF-2 at **Bhirrana** (Ghaggar–Hakra / Saraswati valley); proves Pre-Harappan Hakra phase dates to **>9,000–8,000 years BP** and that Mature Harappan urbanism persisted across millennia of monsoon weakening ($7\text{–}2.8\text{ ka BP}$) via adaptive crop-shifting from wheat/barley to drought-hardy millets and rice.
18. **[[asik-borani-soz-insanin-aynasi]]** ([[asik-borani]] & [[ibrahim-gosterir]], 2020, 1,150 pp., 2 Vols.)  
    Complete poetic compendium of Âşık Borani; synthesis of Sufi humanism, pastoral lyricism, social realism, and anti-sectarian egalitarianism.
19. **[[cumhuriyet-donemi-arkeoloji-politikalari-ve-ekrem-akurgal]]** ([[erdal-polat]], 2024, 22 pp.)  
    Atatürk's archaeological mobilization ("Scientific Republic"), Turkish Historical Society (TTK), DTCF, and [[ekrem-akurgal]]'s Anatolian Civilizations Synthesis proving that Greek art derived from Anatolian cultures.

### Category E: Archaeoastronomy, Catastrophism & Lost Civilizations (Graham Hancock et al.)
20. **[[fingerprints-of-the-gods]]** ([[graham-hancock]], 1995, 490 pp.)  
21. **[[keeper-of-genesis]]** ([[graham-hancock]] & [[robert-bauval]], 1996, 331 pp.)  
22. **[[the-mars-mystery]]** ([[graham-hancock]], [[robert-bauval]], [[john-grigsby]], 1998, 252 pp.)  
23. **[[underworld-mysterious-origins-of-civilization]]** ([[graham-hancock]], 2002, 796 pp.)  
24. **[[supernatural-meetings-with-the-ancient-teachers-of-mankind]]** ([[graham-hancock]], 2005, 488 pp.)  
25. **[[lost-knowledge-of-the-ancients]]** (ed. [[glenn-kreisberg]], 2010, 178 pp.)  
26. **[[the-master-game]]** ([[graham-hancock]] & [[robert-bauval]], 2011, 654 pp.)  
27. **[[war-god-nights-of-the-witch]]** ([[graham-hancock]], 2013, 501 pp.)  
28. **[[magicians-of-the-gods]]** ([[graham-hancock]], 2015, 444 pp.)  
29. **[[america-before-the-key-to-earths-lost-civilization]]** ([[graham-hancock]], 2019, 668 pp.)  
