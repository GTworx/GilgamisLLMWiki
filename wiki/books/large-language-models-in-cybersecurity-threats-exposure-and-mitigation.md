# Large Language Models in Cybersecurity: Threats, Exposure and Mitigation

**Author(s)**: [[andrei-kucharavy]], [[octave-plancherel]], [[valentin-mulder]], [[alain-mermoud]], [[vincent-lenders]]  
**Genre(s)**: [[cybersecurity-and-digital-forensics]], [[artificial-intelligence-and-machine-learning]], [[security-studies]]  
**Key Themes**: [[hybrid-threats-and-cyber-warfare]], [[agi-trajectories-and-superalignment]], [[human-centered-ai-and-augmented-leadership]]  
**Publication Year**: 2024  
**Source**: BOOKS/AI/AI LLM Cybesecurity.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\AI\)  
**Last updated**: 2026-11-03  

---

## Executive Summary

*Large Language Models in Cybersecurity: Threats, Exposure and Mitigation* (published by Springer Open Access in 2024, 249 pp., `DOI: 10.1007/978-3-031-54827-7`, supported by armasuisse Science and Technology, with Forewords by Swiss National Cyber Security Centre Director Florian Schütz and Council of Europe Director Jan Kleijssen) edited by [[andrei-kucharavy]], [[octave-plancherel]], [[valentin-mulder]], [[alain-mermoud]], and [[vincent-lenders]] is a comprehensive 25-chapter technical treatise produced by the Swiss Cyber-Defence (CYD) Campus in collaboration with EPFL, ETH Zürich, IBM Research Europe, and Sophos AI (source: BOOKS/AI/AI LLM Cybesecurity.pdf, pp. 1–16). Designed directly to support Measure Four of the Swiss National Cyberstrategy (NCS) and the EU AI Act / Cyber Resilience Act, the volume provides a rigorous engineering assessment of how Large Language Models alter the offense–defense balance in cyberspace (source: BOOKS/AI/AI LLM Cybesecurity.pdf, pp. 5–10).

Structured across five parts, the book demystifies three decades of NLP research culminating in Transformer attention architectures and code-generation models such as OpenAI Codex (Part I, Chapters 1–5, pp. 35–51); maps the **inherent vulnerabilities and exposure of LLMs** including training-data extraction, membership inference, model poisoning, backdoors, and direct/indirect prompt injection (Part II, Chapters 6–9); analyzes **malign and offensive uses of LLMs** including automated spear-phishing, polymorphic malware generation, and LLM-instrumented sock-puppet influence operations that exploit the *'liar's dividend'* to erode public trust in objective truth (Part III, Chapters 10–14, p. 121); evaluates **defensive cybersecurity applications** in SOC automation, log analysis, and vulnerability repair alongside the hazards of insecure AI-generated code (Part IV, Chapters 15–19); and codifies **mathematical, cryptographic, and regulatory mitigations** including Byzantine-robust and differentially private federated learning (solving the *privacy–robustness–utility trilemma* by Rachid Guerraoui and Nirupam Gupta at EPFL, Ch. 21, p. 201) (source: BOOKS/AI/AI LLM Cybesecurity.pdf, pp. 8–16, 51, 121, 201).

---

## Key Arguments / Chapter Breakdown

* **Forewords, Preface & Part I (Chapters 1–5): Foundations, LLM Families & Fundamental Limitations (pp. v–70, PDF pp. 5–80)**:
  * *Transformers, Codex & Structural Hallucinations*: Traces the evolution from statistical language models to GPT/Codex-12B (trained on GitHub/PyPI Python repositories, Ch. 3, p. 35 / PDF p. 51), explaining why autoregressive token prediction structurally produces confabulations ('hallucinations') and lacks formal semantic grounding (source: BOOKS/AI/AI LLM Cybesecurity.pdf, pp. 5–10, 51).

* **Part II (Chapters 6–9): Vulnerabilities and Exposure of Deployed LLMs (pp. 71–104, PDF pp. 81–114)**:
  * *Data Leakage, Poisoning & Prompt Injection*: Details how memorized PII and proprietary source code can be extracted verbatim from foundation model weights, how adversarial poisoning of web-scraped corpora implants sleeper backdoors, and why LLMs fail to separate system instructions from untrusted user data (prompt injection) (source: BOOKS/AI/AI LLM Cybesecurity.pdf, pp. 9–10).

* **Part III (Chapters 10–14): Malign Uses — Social Engineering, Disinformation & Malware Assistance (pp. 105–146, PDF pp. 115–156)**:
  * *Counterfeit People & The Liar's Dividend*: Examines LLM-aided social media influence operations (Ch. 11, p. 109 / PDF p. 121), showing how swarms of LLM-driven 'counterfeit people' not only scale tailored propaganda at near-zero marginal cost, but also generate the **liar's dividend**—enabling bad actors to dismiss authentic evidence as 'AI-generated' (source: BOOKS/AI/AI LLM Cybesecurity.pdf, p. 121).

* **Parts IV & V (Chapters 15–25): Defensive Cyber Operations, Secure Coding & Robust Federated Governance (pp. 147–238, PDF pp. 157–248)**:
  * *SOC Co-Pilots & The Privacy–Robustness–Utility Trilemma*: Evaluates LLMs for intrusion detection, reverse engineering, and vulnerability patching while quantifying how developer over-reliance on AI coding assistants introduces subtle CWE vulnerabilities; concludes with EPFL's Byzantine-resilient, differentially private distributed learning protocols (Ch. 21, p. 195 / PDF p. 201) and international legal governance (source: BOOKS/AI/AI LLM Cybesecurity.pdf, pp. 8, 16, 201).

---

## Key Quotes & Citations

* "A new technology getting integrated into cyber-physical systems can create a novel attack surface that can and will be rapidly exploited. A new technology unexpectedly exploited by an attacker can give them a crucial advantage, leading to a series of compromises. Large Language Models (LLMs) are just such a technology." (source: BOOKS/AI/AI LLM Cybesecurity.pdf, Preface, p. ix / PDF p. 9)
* "Besides false information, synthetic content may also increase general skepticism towards objective truth, making it easier to discredit authentic online content as 'AI-generated'. Hence, a substantial increase of synthetic content online, propagated by sock puppet accounts, would normalize this behavior—producing the liar's dividend." (source: BOOKS/AI/AI LLM Cybesecurity.pdf, ch. 11, p. 109 / PDF p. 121)

---

## Thematic Connections

* **Cyber-Behavioral Forensics & Incident Handling**: Directly expands [[marshall-s-rich]]'s [[advanced-network-forensics-a-cyber-behavioral-science-approach]] and [[paul-cichonski]] et al.'s [[computer-security-incident-handling-guide-nist-sp-800-61r2]] into the era of generative AI threat actors and SOC co-pilots.
* **Cyber Deterrence & Grey-Zone Information Warfare**: Connects with [[max-smeets]], [[stefan-soesanto]], and [[alex-wilner]]'s cyber and AI coercion analyses in [[deterrence-in-the-21st-century]].
* **The Infocalypse & Fragility Amplifiers**: Parallels [[mustafa-suleyman]] and [[michael-bhaskar]]'s warning on synthetic disinformation and the 'Infocalypse' in [[the-coming-wave-ai-power-and-our-future]] (Ch. 10).

---

## Related pages

- [[andrei-kucharavy]]
- [[octave-plancherel]]
- [[valentin-mulder]]
- [[alain-mermoud]]
- [[vincent-lenders]]
- [[cybersecurity-and-digital-forensics]]
- [[artificial-intelligence-and-machine-learning]]
- [[security-studies]]
- [[hybrid-threats-and-cyber-warfare]]
- [[agi-trajectories-and-superalignment]]
- [[human-centered-ai-and-augmented-leadership]]
- [[marshall-s-rich]]
- [[advanced-network-forensics-a-cyber-behavioral-science-approach]]
- [[paul-cichonski]]
- [[computer-security-incident-handling-guide-nist-sp-800-61r2]]
- [[max-smeets]]
- [[stefan-soesanto]]
- [[alex-wilner]]
- [[deterrence-in-the-21st-century]]
- [[mustafa-suleyman]]
- [[michael-bhaskar]]
- [[the-coming-wave-ai-power-and-our-future]]
