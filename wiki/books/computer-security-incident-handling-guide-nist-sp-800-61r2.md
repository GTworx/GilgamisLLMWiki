# Computer Security Incident Handling Guide (NIST Special Publication 800-61 Revision 2)

**Author(s)**: [[paul-cichonski]], [[tom-millar]], [[tim-grance]], [[karen-scarfone]]  
**Genre(s)**: [[cybersecurity-and-digital-forensics]], [[security-studies]], [[strategic-studies]]  
**Key Themes**: [[hybrid-threats-and-cyber-warfare]], [[adaptive-intelligence-and-organizational-resilience]], [[rationality-and-decision-making]]  
**Publication Year**: 2012  
**Source**: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\Cybersecurity\)  
**Last updated**: 2026-11-01  

---

## Executive Summary

*Computer Security Incident Handling Guide (NIST Special Publication 800-61 Revision 2)* (published by the National Institute of Standards and Technology, August 2012, 79 pp., `DOI: 10.6028/NIST.SP.800-61r2`) by [[paul-cichonski]], [[tom-millar]] (US-CERT / DHS), [[tim-grance]], and [[karen-scarfone]] is the foundational U.S. federal and global industry standard for establishing Computer Security Incident Response Teams (CSIRTs) and managing cybersecurity incidents across enterprise and government infrastructure (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, pp. 1–6, 10–13). Developed under the statutory mandate of the Federal Information Security Management Act (FISMA, P.L. 107-347), the guide establishes platform-independent doctrine for triaging, containing, eradicating, and learning from cyber intrusions.

At the core of NIST SP 800-61r2 is the four-phase **Incident Response Life Cycle**: (1) **Preparation**, (2) **Detection and Analysis**, (3) **Containment, Eradication, and Recovery**, and (4) **Post-Incident Activity** (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, pp. 21–44). The publication introduces a rigorous taxonomy distinguishing **precursors** (signs that an incident may occur in the future) from **indicators** (signs that an incident may have occurred or may be occurring now), replaces arbitrary severity labels with a three-dimensional prioritization matrix (**Functional Impact**, **Information Impact**, and **Recoverability Effort**), and establishes protocols for forensic evidence preservation, chain-of-custody documentation, and cross-organization threat intelligence sharing with US-CERT and ISACs (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, pp. 8–9, 26–55).

---

## Key Arguments / Chapter Breakdown

* **Executive Summary & Section 1: Introduction and Statutory Authority (pp. 1–5, PDF pp. 10–14)**:
  * *FISMA Mandate & Prevention–Response Synergy*: Defines a 'computer security incident' as a violation or imminent threat of violation of computer security policies, acceptable use policies, or standard security practices. Emphasizes that incident prevention and incident response are mutually reinforcing (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, pp. 11–14).

* **Section 2: Organizing a Computer Security Incident Response Capability (pp. 6–20, PDF pp. 15–29)**:
  * *CSIRT Organizational Models*: Evaluates Central, Distributed, and Coordinating CSIRT structures; full-time vs. partially outsourced staffing; 24/7 escalation workflows; and mandatory reporting relationships with law enforcement, legal counsel, public affairs, and US-CERT (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, pp. 15–29).

* **Section 3: Handling an Incident — The Four-Phase Life Cycle (pp. 21–44, PDF pp. 30–53)**:
  * *Preparation & Detection/Analysis*: Details jump-kit readiness, network profiling, and correlating **Precursors** vs. **Indicators** across SIEMs, IDPS, and NetFlow logs (pp. 30–40). Introduces the 3D Prioritization Matrix: *Functional Impact* (None/Low/Medium/High), *Information Impact* (None/Privacy Breach/Proprietary Breach/Integrity Loss), and *Recoverability Effort* (Regular/Supplemented/Extended/Not Recoverable) (pp. 41–43).
  * *Containment, Eradication, Recovery & Post-Incident Lessons Learned*: Evaluates containment trade-offs (sandboxing/monitoring vs. immediate network isolation), forensic disk imaging and chain of custody, phased recovery validation, and formal 'Lessons Learned' post-mortems (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, pp. 44–53).

* **Section 4 & Appendices: Coordination, Information Sharing & Checklists (pp. 45–70, PDF pp. 54–79)**:
  * *Ad-Hoc vs. Granular Automated Sharing*: Details ad-hoc, partially automated, and standardized data-exchange sharing (IODEF, RID, CEE, STIX/TAXII precursors) across trusted peer communities while safeguarding privacy and operational security (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, pp. 54–79).

---

## Key Quotes & Citations

* "Preventing problems is often less costly and more effective than reacting to them after they occur. Thus, incident prevention is an important complement to an incident response capability." (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, Exec. Summary, p. 11)
* "A precursor is a sign that an incident may occur in the future. An indicator is a sign that an incident may have occurred or may be occurring now." (source: BOOKS/Cybersecurity/2012 Chichonski et al Computer Security Incident Handling Guide NIST.SP.800-61r2.pdf, sec. 3.2.2, p. 35)

---

## Thematic Connections

* **From Reactive Incident Handling to Proactive Behavioral Forensics**: Provides the baseline artifact-and-lifecycle framework that [[marshall-s-rich]] extends with AI and forensic cyberpsychology in [[advanced-network-forensics-a-cyber-behavioral-science-approach]].
* **Cyber Deterrence & Resilience by Denial**: Operationalizes the technical resilience-by-denial and attribution capabilities analyzed by [[stefan-soesanto]] and [[max-smeets]] in [[deterrence-in-the-21st-century]].
* **Intelligent Failure & Post-Incident Learning**: Section 3.4's blame-free 'Lessons Learned' post-incident review embodies [[amy-c-edmondson]]'s psychological safety and intelligent failure doctrine in [[leading-for-tomorrow]].

---

## Related pages

- [[paul-cichonski]]
- [[tom-millar]]
- [[tim-grance]]
- [[karen-scarfone]]
- [[cybersecurity-and-digital-forensics]]
- [[security-studies]]
- [[strategic-studies]]
- [[hybrid-threats-and-cyber-warfare]]
- [[adaptive-intelligence-and-organizational-resilience]]
- [[rationality-and-decision-making]]
- [[marshall-s-rich]]
- [[advanced-network-forensics-a-cyber-behavioral-science-approach]]
- [[stefan-soesanto]]
- [[max-smeets]]
- [[deterrence-in-the-21st-century]]
- [[amy-c-edmondson]]
- [[leading-for-tomorrow]]
