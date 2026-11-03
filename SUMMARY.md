# Gilgamis LLM Wiki — Ingestion & Library Summary

**Generated**: 2026-11-03  
**Knowledge Base Specification**: [GilgamisLLMWiki.md](GilgamisLLMWiki.md)  
**Interactive Dashboard**: [index.html](index.html) | [http://127.0.0.1:8080/index.html](http://127.0.0.1:8080/index.html)  
**Master Index**: [wiki/index.md](wiki/index.md)  
**Operations Log**: [wiki/log.md](wiki/log.md)  
**Local Ollama (`qwen3.8`) CLI**: [.agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py](.agents/skills/gilgamis-llm-wiki/scripts/ollama_agent.py)  

---

## 1. Executive Overview

The **Gilgamis LLM Wiki** is a structured, interlinked personal knowledge base built following Andrej Karpathy's LLM Wiki pattern and integrated with a local **Ollama (`qwen3.8:latest` / `qwen3.8:27b`)** agentic execution and multimodal Vision OCR pipeline. This document summarizes the complete ingestion of foundational literature from both the primary mounted library (`C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\`) and local staging (`raw/`), establishing an expansive, cross-referenced corpus spanning game theory, topological social choice, comparative democratic history (from third-millennium BC Mesopotamia to post-1945 monitory democracy), strategic studies, semiconductor geopolitics, military human performance enhancement, executive leadership, organizational psychology, evolutionary biology and memetics, Anatolian minstrel literature, classical archaeology, paleoclimatology, archaeoastronomy, and alternative prehistory.

### Library Metrics at a Glance
- **Total Ingested Works**: 78 distinct intellectual works (across 92 source files/volumes and ~26,800 pages)
- **Total Generated Wiki Pages**: 348 interlinked markdown files (346 entity pages + `index.md` & `log.md`)
- **Interactive Web App**: [index.html](index.html) (with embedded data, fuzzy search, and modal inspectors)
- **Book Summary & Analysis Pages**: 78 ([books/](wiki/books/))
- **Author Profile Pages**: 162 ([authors/](wiki/authors/))
- **Genre Classification Pages**: 51 ([genres/](wiki/genres/))
- **Core Thematic Concept Pages**: 55 ([themes/](wiki/themes/))
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

### Category F: Option 2 Small Domain Batch (14 Folders, 31 Works: Türkiye, Music, Fiction, Blockchain, Cybersecurity, Energy, Entertainment Media, Law, Sales, Education, Ethics, Innovation, Neuroscience & Society)
30. **[[gormedigimiz-turkiye-123-yillik-national-geographic-arsivi]]** ([[kurt-and-margot-lubinski]], [[bernard-f-rogers-jr]], 2020)  
    *Görmediğimiz Türkiye: 123 Yıllık National Geographic Arşivi* is a curated 50-page visual and ethnographic chronicle drawn from over a century of the *National Geographic* photographic archives, documenting everyday social life, urban transformation, maritime commerce, and rural landscapes across early Republican Türkiye between the 1920s and 1950s (source: BOOKS/Türkiye_/Görmediğimiz Türkiye.pdf, pp.
31. **[[noise-the-political-economy-of-music]]** ([[jacques-attali]], [[fredric-jameson]], [[susan-mcclary]], 1985)  
    *Noise: The Political Economy of Music* (originally published in French as *Bruits* in 1977; English translation by Brian Massumi in 1985 with a Foreword by [[fredric-jameson]] and Afterword by [[susan-mcclary]]) is [[jacques-attali]]'s landmark theoretical treatise arguing that music is not a passive superstructure reflecting economic base relations, but a **prophetic herald** that anticipates future social orders and political economies centuries or decades before they materialize in institutions (source: BOOKS/Music/attali noise.pdf, pp.
32. **[[the-end-of-modernism-elias-canettis-auto-da-fe]]** ([[william-collins-donahue]], [[elias-canetti]], 2001)  
    *The End of Modernism: Elias Canetti's Auto-da-Fé* (published by University of North Carolina Press in 2001; reissued with a new Foreword in 2010, UNC Studies in the Germanic Languages and Literatures No.
33. **[[blockchain-crypto-and-defi-bridging-finance-and-technology]]** ([[marco-di-maggio]], 2025)  
    *Blockchain, Crypto and DeFi: Bridging Finance and Technology* (published by John Wiley & Sons, 2025/2026, 749 pp.) is Harvard Business School Professor [[marco-di-maggio]]'s comprehensive 15-chapter treatise on the economic architecture, game-theoretic incentives, and institutional transformation of distributed ledger technology, cryptocurrencies, decentralized finance (DeFi), Web3, and AI-blockchain convergence (source: BOOKS/Blockchain_/2026 Blockchain, Crypto & DeFi.pdf, pp.
34. **[[getting-started-with-enterprise-blockchain]]** ([[michael-bradley]], [[david-gorman]], [[matt-lucas]], [[matthew-golby-kirk]], 2019)  
    *Getting Started with Enterprise Blockchain: A Guide to Design and Development* (published by O'Reilly Media and IBM Corporation, 2019, 86 pp.) by [[michael-bradley]], [[david-gorman]], [[matt-lucas]], and [[matthew-golby-kirk]] (with a Foreword by Clause Inc.
35. **[[computer-security-incident-handling-guide-nist-sp-800-61r2]]** ([[paul-cichonski]], [[tom-millar]], [[tim-grance]], [[karen-scarfone]], 2012)  
    *Computer Security Incident Handling Guide (NIST Special Publication 800-61 Revision 2)* (published by the National Institute of Standards and Technology, August 2012, 79 pp., `DOI: 10.6028/NIST.SP.800-61r2`) by [[paul-cichonski]], [[tom-millar]] (US-CERT / DHS), [[tim-grance]], and [[karen-scarfone]] is the foundational U.S.
36. **[[advanced-network-forensics-a-cyber-behavioral-science-approach]]** ([[marshall-s-rich]], 2026)  
    *Advanced Network Forensics: A Cyber-Behavioral Science Approach* (published by John Wiley & Sons, 2026, 297 pp.) by forensic cyberpsychologist Dr.
37. **[[burasi-cok-onemli-enerjiden-ekonomiye-tam-bagimsiz-turkiye]]** ([[berat-albayrak]], 2022)  
    *Burası Çok Önemli! Enerjiden Ekonomiye Tam Bağımsız Türkiye* (published by Turkuvaz Kitap, March 2022, 273 pp.) is the political-economic memoir and policy manifesto of Dr.
38. **[[monetizing-energy-storage-a-toolkit-to-assess-future-cost-and-value]]** ([[oliver-schmidt]], [[iain-staffell]], 2023)  
    *Monetizing Energy Storage: A Toolkit to Assess Future Cost and Value* (published by Oxford University Press, 2023, 353 pp.) by Dr.
39. **[[electric-vehicles-light-duty-fuel-economy-and-shared-micromobility]]** ([[kwo-young]], [[gary-marchant]], [[colin-murphy]], [[alexander-kolpakov]], 2022)  
    This four-volume synthesis encompasses the complete `BOOKS/Energy/Light Battery Vehicle including eBike/` sub-library (totaling 749 pages across four landmark engineering and National Academies policy studies published between 2013 and 2022): (1) *Electric Vehicle Battery Technologies* (2013, 44 pp., Springer, `DOI: 10.1007/978-1-4614-0134-6_2`) by [[kwo-young]], Caisheng Wang, Le Yi Wang, and Kai Strunz; (2) *Assessment of Technologies for Improving Light-Duty Vehicle Fuel Economy—2025–2035* (2021, 457 pp., National Academies Press) chaired by [[gary-marchant]]; (3) *TCRP Research Report 230: Transit and Micromobility* (2021, 111 pp., Transportation Research Board / NASEM) by [[colin-murphy]] et al.; and (4) *NCHRP Synthesis 597: Micromobility Policies, Permits, and Practices* (2022, 137 pp., TRB / NASEM) by [[alexander-kolpakov]], Austin Marie Sipiora, and Jana E.
40. **[[entertainment-science-data-analytics-and-practical-theory]]** ([[thorsten-hennig-thurau]], [[mark-b-houston]], 2019)  
    *Entertainment Science: Data Analytics and Practical Theory for Movies, Games, Books, and Music* (published by Springer Nature, 2019, 879 pp., `DOI: 10.1007/978-3-319-89292-4`) by Professors [[thorsten-hennig-thurau]] (University of Münster) and [[mark-b-houston]] (Texas Christian University) is an encyclopedic synthesis of over 35 years of empirical econometrics, consumer psychology, and data science across the global motion picture, video game, book publishing, and recorded music industries (source: BOOKS/Entertainment Media/2019_Book_EntertainmentScience.pdf, pp.
41. **[[media-and-digital-management]]** ([[eli-m-noam]], 2019)  
    *Media and Digital Management* (published by Palgrave Macmillan / Springer Nature, 2019, 486 pp., `DOI: 10.1007/978-3-319-72000-5`) by Columbia Business School Professor [[eli-m-noam]] is a comprehensive treatise on the managerial economics, industrial organization, technology engineering, finance, law, and distribution strategy of the global media, communications, and digital information sector (source: BOOKS/Entertainment Media/2019_Book_MediaAndDigitalManagement.pdf, pp.
42. **[[handbook-of-quantitative-criminology]]** ([[alex-r-piquero]], [[david-weisburd]], 2010)  
    *Handbook of Quantitative Criminology* (published by Springer, 2010, 787 pp., `DOI: 10.1007/978-0-387-77650-7`) edited by Professors [[alex-r-piquero]] (Florida State University) and [[david-weisburd]] (Hebrew University of Jerusalem / George Mason University), with a Foreword by Alfred Blumstein, is the landmark 35-chapter reference work codifying the statistical, spatial, longitudinal, and experimental methodologies of modern criminology and criminal justice policy (source: BOOKS/Law/2010_Book_HandbookOfQuantitativeCriminol.pdf, pp.
43. **[[introduction-to-law]]** ([[jaap-hage]], [[antonia-waltermann]], [[bram-akkermans]], 2017)  
    *Introduction to Law (Second Edition)* (published by Springer International Publishing, 2017, 396 pp., `DOI: 10.1007/978-3-319-57252-9`) edited by Maastricht University legal scholars [[jaap-hage]], [[antonia-waltermann]], and [[bram-akkermans]] is a comparative, jurisdiction-transcending treatise on the foundations, concepts, branches, and philosophy of law designed at the Maastricht European Law School (source: BOOKS/Law/2017_Book_IntroductionToLaw.pdf, pp.
44. **[[spin-selling]]** ([[neil-rackham]], 1988)  
    *SPIN Selling* (published by McGraw-Hill, 1988, 210 pp.) by Huthwaite founder and behavioral psychologist [[neil-rackham]] is the foundational empirical study of high-value, complex B2B sales behavior (source: BOOKS/Sales/The Spin Selling.pdf, pp.
45. **[[the-challenger-sale-challenge-yourself-action-book]]** ([[matthew-dixon]], [[brent-adamson]], 2021)  
    *Challenge Yourself: The Challenger Sales Conversation — Developing and Managing Constructive Tension* (published by Challenger Performance Optimization / Corporate Executive Board & Gartner, 2021, 56 pp.) operationalizes the landmark CEB/Gartner research pioneered by [[matthew-dixon]] and [[brent-adamson]] (*The Challenger Sale* and *The Challenger Customer*) into an interactive field workbook for complex B2B commercial conversations (source: BOOKS/Sales/Challenge Yourself Virtual Classroom - Action Book v3.pdf, pp.
46. **[[disrupting-class-how-disruptive-innovation-will-change-the-way-the-world-learns]]** ([[clayton-m-christensen]], [[michael-b-horn]], [[curtis-w-johnson]], 2008)  
    *Disrupting Class: How Disruptive Innovation Will Change the Way the World Learns* (published by McGraw-Hill, 2008, 258 pp.) by Harvard Business School Professor [[clayton-m-christensen]], [[michael-b-horn]], and [[curtis-w-johnson]] applies Christensen's renowned theory of **Disruptive Innovation** to diagnose why public K–12 schools have struggled for decades to improve despite massive funding increases and why student-centric online learning will fundamentally transform education (source: BOOKS/Education_/Disrupting Class_ How Disruptive Innovation Will Change the Way the World Learns ( PDFDrive ).pdf, pp.
47. **[[blended-using-disruptive-innovation-to-improve-schools]]** ([[michael-b-horn]], [[heather-staker]], [[clayton-m-christensen]], 2015)  
    *Blended: Using Disruptive Innovation to Improve Schools* (published by Jossey-Bass / Wiley, 2015, 333 pp., with a Foreword by [[clayton-m-christensen]]) by Clayton Christensen Institute co-founder [[michael-b-horn]] and [[heather-staker]] is the practical design manual translating the disruptive innovation theory of [[disrupting-class-how-disruptive-innovation-will-change-the-way-the-world-learns]] into concrete K–12 school architectures (source: BOOKS/Education_/Blended_ Using Disruptive Innovation to Improve Schools ( PDFDrive ).pdf, pp.
48. **[[educational-technology-a-primer-for-the-21st-century]]** ([[ronghuai-huang]], [[j-michael-spector]], [[junfeng-yang]], 2019)  
    *Educational Technology: A Primer for the 21st Century* (published by Springer Nature Singapore in the *Lecture Notes in Educational Technology* series, 2019, 253 pp., `DOI: 10.1007/978-981-13-6643-7`) by Professors [[ronghuai-huang]] (Beijing Normal University), [[j-michael-spector]] (University of North Texas), and [[junfeng-yang]] (Hangzhou Normal University) is a foundational international textbook synthesizing the theoretical foundations, technological architectures, instructional design models, and research methodologies of 21st-century educational technology (source: BOOKS/Education_/2019_Book_EducationalTechnology.pdf, pp.
49. **[[zen-and-the-art-of-motorcycle-maintenance]]** ([[robert-m-pirsig]], 1974)  
    *Zen and the Art of Motorcycle Maintenance: An Inquiry into Values* (originally published by William Morrow in 1974; 25th Anniversary Edition, HarperPerennial Modern Classics, 429 pp.) by [[robert-m-pirsig]] is one of the most influential philosophical novels of the twentieth century (source: BOOKS/Ethics/Zen and the Art of Motorcycle Maintenance_ An Inquiry into Values ( PDFDrive ).pdf, pp.
50. **[[global-ethics-for-leadership-values-and-virtues-for-life]]** ([[christoph-stuckelberger]], [[walter-fust]], [[obiora-ike]], 2016)  
    *Global Ethics for Leadership: Values and Virtues for Life* (published by Globethics.net in Geneva as *Globethics.net Global No.
51. **[[ethics-in-higher-education-values-driven-leaders-for-the-future]]** ([[divya-singh]], [[christoph-stuckelberger]], [[obiora-ike]], 2017)  
    *Ethics in Higher Education: Values-driven Leaders for the Future* (published by Globethics.net in Geneva as *Globethics.net Education Ethics No.
52. **[[economic-transformations-general-purpose-technologies-and-long-term-economic-growth]]** ([[richard-g-lipsey]], [[kenneth-i-carlaw]], [[clifford-t-bekar]], 2005)  
    *Economic Transformations: General Purpose Technologies and Long-Term Economic Growth* (published by Oxford University Press, 2005, 618 pp.) by economists [[richard-g-lipsey]], [[kenneth-i-carlaw]], and [[clifford-t-bekar]]—growing out of the Canadian Institute for Advanced Research (CIAR) program advised by Nobel laureate Kenneth Arrow—is the definitive theoretical, historical, and formal treatise on **General Purpose Technologies (GPTs)** and **Structuralist-Evolutionary (S-E)** economics (source: BOOKS/Innovation_/Economic transformations- general purpose technologies and long-term economic growth (2005)(595s)lipsey r.g., carlaw k.i., bekar c.t_.pdf, pp.
53. **[[learning-by-doing-the-real-connection-between-innovation-wages-and-wealth]]** ([[james-bessen]], 2015)  
    *Learning by Doing: The Real Connection Between Innovation, Wages, and Wealth* (published by Yale University Press, 2015, 310 pp.) by Boston University economist and former desktop-publishing software pioneer [[james-bessen]] resolves a central paradox of modern capitalism: why major technological revolutions (both during the first 50 years of the 19th-century Industrial Revolution—*'Engels' Pause'*—and during the post-1980 Information Technology revolution) initially produce **stagnant median wages and rising inequality** for decades before eventually generating broad-based prosperity (source: BOOKS/Innovation_/2015 Learning by Doing - the real connection between_innovation, wages, and wealth.pdf, pp.
54. **[[the-medici-effect-what-elephants-and-epidemics-can-teach-us-about-innovation]]** ([[frans-johansson]], 2006)  
    *The Medici Effect: What Elephants and Epidemics Can Teach Us About Innovation* (Harvard Business School Press, 2004/2006; 10-page Introduction monograph *'What is the Medici Effect, and How Can It Help Me Innovate?'*, ISBN 978-1-4221-4609-5) by [[frans-johansson]] introduces one of modern innovation theory's most influential frameworks: **The Intersection** (source: BOOKS/Innovation_/HBR+What+is+the+Medici+Effect.pdf, pp.
55. **[[the-emperors-new-mind-concerning-computers-minds-and-the-laws-of-physics]]** ([[roger-penrose]], 1989)  
    *The Emperor's New Mind: Concerning Computers, Minds, and the Laws of Physics* (originally published by Oxford University Press in 1989; Revised Edition 1999) by Nobel Prize–winning mathematical physicist Sir [[roger-penrose]] is a monumental 10-chapter inquiry into whether human consciousness and mathematical insight can ever be replicated by an algorithmic digital computer—the claim of **'Strong AI'** (source: BOOKS/Neuroscience_/dokumen.pub_the-emperors-new-mind-concerning-computers-minds-and-the-laws-of-physics-revised-impression-second-edition-9780198784920-0198784929-978-0-19-286198-6.epub, ch.
56. **[[discovering-the-brain]]** ([[sandra-ackerman]], 1992)  
    *Discovering the Brain* (published by National Academy Press, Washington, D.C., 1992, 195 pp.) by science writer [[sandra-ackerman]] for the **Institute of Medicine (IOM) and National Academy of Sciences** is the official foundational synthesis launched to inaugurate the U.S.
57. **[[reductionism-in-art-and-brain-science-bridging-the-two-cultures]]** ([[eric-r-kandel]], 2016)  
    *Reductionism in Art and Brain Science: Bridging the Two Cultures* (published by Columbia University Press, 2016, ISBN 978-0-231-17962-1) by Nobel Prize–winning neuroscientist [[eric-r-kandel]] demonstrates how **methodological reductionism**—isolating a complex phenomenon's fundamental components to reveal its underlying mechanisms—serves as the common methodological bridge uniting modern brain science and 20th-century abstract art, thereby healing C.
58. **[[a-conflict-of-visions-ideological-origins-of-political-struggles]]** ([[thomas-sowell]], 2007)  
    *A Conflict of Visions: Ideological Origins of Political Struggles* (originally published in 1987; Revised Edition published by Basic Books, 2006/2007, 323 pp.) by Hoover Institution economist and social theorist [[thomas-sowell]] investigates a profound historical puzzle: why the same individuals consistently line up on the same sides of completely unrelated political, legal, economic, and military controversies across centuries (source: BOOKS/Society_/2006 A Conflict of Visions Ideological Origins of Political Struggles-by Thomas Sowell.pdf, pp.
59. **[[doppelganger-israel-palestine-and-the-doppelganger-effect]]** ([[naomi-klein]], 2023)  
    *Israel, Palestine, and the Doppelganger Effect* (published late 2023, 55 pp.
60. **[[mongrel-nation-colonization-in-reverse]]** ([[ashley-dawson]], [[louise-bennett]], 2007)  
    *Colonization in Reverse: An Introduction* (the foundational 27-page opening chapter of *Mongrel Nation: Diasporic Culture and the Making of Postcolonial Britain*, published by University of Michigan Press, 2007, Stable URL `http://www.jstor.com/stable/j.ctv3znzng.4`) by cultural historian [[ashley-dawson]] chronicles how post-1945 migration from the Caribbean, South Asia, and Africa dismantled insular imperial myths of British identity and forged a hybrid, cosmopolitan postcolonial culture (source: BOOKS/Society_/Dawson-ColonizationReverse-2007.pdf, pp.

### Category G: Artificial Intelligence, Machine Learning, Data Science & AGI Geopolitics (`BOOKS/AI/` — 18 Works across 25 Source Files)
61. **[[infinite-how-visionary-leaders-transform-todays-businesses-into-ai-forward-companies]]** ([[brian-solis]] & [[dave-wright]], 2026, Wiley, 323 pp.)  
    ServiceNow AI transformation manifesto introducing the **AI Maturity Index**, the **AI Control Tower**, **Agentic AI**, and exponential **AI-First** enterprise architectures over legacy digital transformation.
62. **[[ai-2027]]** ([[daniel-kokotajlo]], [[scott-alexander]], [[thomas-larsen]], [[eli-lifland]], & [[romeo-dean]], 2025, AI Futures Project, 71 pp.)  
    Month-by-month scenario wargame charting the 2025–2027 trajectory from **OpenBrain**'s Agent-1 through Agent-4, recursive AI R&D **intelligence explosion**, neuralese **scheming** and misalignment, **China's CDZ** weight theft, and branching **Slowdown vs. Race** endings.
63. **[[empire-of-ai-dreams-and-nightmares-in-sam-altmans-openai]]** ([[karen-hao]], 2025, Penguin Press, 575 pp.)  
    Investigative history of Sam Altman's OpenAI framing frontier AI labs as neo-colonial **computational empires** built on global South data-annotation labor (Kenya, Venezuela, Chile), hyperscale energy/water extraction, and the ideological rift between **Boomers** and **Doomers**.
64. **[[probabilistic-artificial-intelligence]]** ([[andreas-krause]] & [[jonas-hubotter]], 2025, ETH Zürich / arXiv:2502.05244v1, 418 pp. + companion `.txt`)  
    Graduate mathematical textbook unifying **Bayesian inference**, **Gaussian Processes**, **Kalman/particle filtering**, **active learning** (submodular mutual information), **Bayesian optimization** (GP-UCB), **Markov Decision Processes**, and **RLHF / DPO** for foundation models.
65. **[[a-brief-history-of-intelligence-evolution-ai-and-the-five-breakthroughs-that-made-our-brains]]** ([[max-solomon-bennett]], 2025, HarperCollins, 103 pp.)  
    Chronicles the **Five Evolutionary Breakthroughs** of biological brains—**Steering** (bilaterians), **Reinforcing** (vertebrates / TD dopamine), **Simulating** (mammals / neocortex), **Mentalizing** (primates / Theory of Mind), and **Speaking** (humans / language)—as a reverse-engineering blueprint for AGI.
66. **[[situational-awareness-the-decade-ahead]]** ([[leopold-aschenbrenner]], 2024, 165 pp., 2 PDF copies)  
    Projects **Orders of Magnitude (OOMs)** in compute, algorithmic efficiency, and **unhobbling** to argue that AGI arrives by **2027**, triggering an intelligence explosion, trillion-dollar ** industrial mobilization**, **superalignment** challenges, and a national-security **"The Project."**
67. **[[co-intelligence-living-and-working-with-ai]]** ([[ethan-mollick]], 2024, Portfolio / Penguin, 114 pp.)  
    Defines the **Jagged Frontier** of LLM capabilities, the **Four Rules of Co-Intelligence** (*Always invite AI to the table; Be the human in the loop; Treat AI like a person; Assume this is the worst AI you will ever use*), **Centaurs vs. Cyborgs**, and **"**"Best-of-Breed"** augmentation.
68. **[[large-language-models-in-cybersecurity-threats-exposure-and-mitigation]]** (eds. [[andrei-kucharavy]], [[octave-plancherel]], [[valentin-mulder]], [[alain-mermoud]], & [[vincent-lenders]], 2024, Springer Open, 249 pp.)  
    24-chapter technical reference from the Cyber-Defence Campus (armasuisse) analyzing LLM architectures, **prompt injection**, **data poisoning**, **training data extraction**, **SOC automation**, and disinformation warfare.
69. **[[the-coming-wave-ai-power-and-our-future]]** ([[mustafa-suleyman]] & [[michael-bhaskar]], 2023, Crown, 302 pp. + 673 HTML study annotations)  
    Diagnoses the **containment problem** of **omni-use** AI and synthetic biology, the **pessimism aversion trap**, asymmetric nation-state disruption, and the **Ten Concentric Steps Toward Containment**.
70. **[[a-brief-history-of-artificial-intelligence-what-it-is-where-we-are-and-where-we-are-going]]** ([[michael-wooldridge]], 2020, Flatiron Books / Macmillan, 9 chapters `.epub`)  
    Oxford computer scientist's intellectual history from **Turing's 1950 Imitation Game** and the **1956 Dartmouth Workshop** through **GOFAI**, **AI Winters**, behavioral robotics, deep reinforcement learning (**AlphaGo**), and the **Consciousness Fallacy**.
71. **[[achieving-real-business-outcomes-from-artificial-intelligence-and-the-future-of-machine-intelligence]]** ([[atif-kureishy]], [[chad-meley]], [[ben-mackenzie]], & [[david-beyer]], 2016/2019, O'Reilly Media, 2 Vols., 151 pp.)  
    Pairs Teradata's enterprise AI operationalization playbooks (**AI Flywheel**, **MLOps governance**) with O'Reilly's frontier perspectives on deep learning, hardware acceleration, and data strategy.
72. **[[introduction-to-deep-learning-from-logical-calculus-to-artificial-intelligence]]** ([[sandro-skansi]], 2018, Springer, 196 pp.)  
    Traces neural computation from **McCulloch–Pitts (1943)** logical calculus and **Rosenblatt's Perceptron** through **backpropagation**, **CNNs**, **RNNs/LSTMs**, **Word2Vec**, **autoencoders**, and **Searle's Chinese Room**.
73. **[[machine-learning-for-dummies-ibm-limited-edition]]** ([[judith-hurwitz]] & [[daniel-kirsch]], 2018, John Wiley & Sons, 75 pp., 2 identical SHA-256 copies)  
    Executive practitioner guide covering supervised, unsupervised, and reinforcement learning pipelines, feature engineering, neural networks, and enterprise **IBM Watson** deployments.
74. **[[introduction-to-artificial-intelligence]]** ([[wolfgang-ertel]], 2017, Springer 2nd Ed., 365 pp.)  
    Rigorous German-tradition textbook spanning **propositional and first-order predicate logic**, **Resolution Calculus**, **heuristic search ($A^*$)**, **Jaynesian probability & Bayesian networks**, **reinforcement learning**, and deep learning.
75. **[[an-introduction-to-machine-learning]]** ([[miroslav-kubat]], 2017, Springer 2nd Ed., 348 pp.)  
    Comprehensive 16-chapter university textbook covering **Bayesian classifiers**, **Perceptrons/MLPs**, **SVMs**, **Decision Trees ($ID3/C4.5$)**, **Boosting/AdaBoost**, **PAC learning**, **VC-dimension**, and **class imbalance**.
76. **[[introduction-to-data-science-a-python-approach-to-concepts-techniques-and-applications]]** ([[laura-igual]] & [[santi-segui]], 2017, Springer, 227 pp.)  
    Hands-on University of Barcelona textbook teaching statistical inference, regression, clustering, **recommender systems**, **NLP**, **PageRank network analysis**, and **MapReduce/Spark** in Python.
77. **[[machine-learning-in-medicine-a-complete-overview]]** ([[ton-j-cleophas]] & [[aeilko-h-zwinderman]], 2015, Springer, 498 pp.)  
    80-chapter biostatistical compendium covering **hierarchical clustering**, **linear/logistic/Cox regression**, **Monte Carlo & Markov chains**, **neural networks**, **support vector machines**, and **genetic algorithms** in clinical trials.
78. **[[python-and-r-scientific-computing-foundations-for-ai-and-data-science]]** ([[john-hunt]], [[kent-d-lee]], [[alain-f-zuur]], [[elena-n-ieno]], & [[erik-h-w-g-meesters]], 2009–2019, Springer, 4 Vols., 1,404 pp.)  
    Four-volume Springer computing foundation uniting **Python 3 object-oriented/functional software engineering**, **computational complexity ($O(n)$) & data structures (ASTs, AVL/B-Trees, graphs)**, and **R biostatistical computing**.

