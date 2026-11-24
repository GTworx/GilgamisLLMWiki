# Protect Your Chip Design Intellectual Property: An Overview of Hardware Security, Logic Locking, and Split Manufacturing

**Author(s)**: [[johann-knechtel]], [[satwik-patnaik]], [[ozgur-sinanoglu]]
**Publication Year**: 2019
**Genre(s)**: [[semiconductor-engineering-and-industrial-policy]], [[cybersecurity-and-digital-forensics]]
**Key Themes**: [[semiconductor-geopolitics-and-chokepoints]], [[zero-trust-architecture-and-cryptographic-resilience]]
**Source**: `ARTICLES-REPORTS/Semiconductors/2019 Protect Your Chip Design Intellectual Property - An Overview.pdf` (6 pp., NYU Tandon School of Engineering & NYU Abu Dhabi)
**Last updated**: 2026-11-24

---

## Executive Summary

Authored by leading hardware cybersecurity researchers Johann Knechtel, Satwik Patnaik, and Özgür Sinanoğlu, this technical paper addresses the acute vulnerabilities inherent in the modern **globalized, fabless semiconductor supply chain**. Because fabless design houses (e.g., Apple, Qualcomm, Nvidia) must outsource fabrication to untrusted third-party offshore foundries, their intellectual property (IP) is exposed to reverse engineering, unauthorized overproduction, hardware Trojan insertion, and counterfeiting. The authors provide a comprehensive taxonomy of state-of-the-art hardware protection mechanisms, categorizing them into pre-silicon (IP watermarking, logic locking, IC camouflaging) and post-silicon defenses (split manufacturing, layout obfuscation), while analyzing their mathematical resiliency against Boolean Satisfiability (SAT) attack algorithms.

---

## Key Strategic & Architectural Takeaways

- **The Untrusted Foundry Problem**: The transition to offshore pure-play foundries eliminates fabless capital costs but creates systemic supply-chain threat vectors: rogue foundry operators can reverse engineer GDSII layout masks, clone proprietary accelerators, or clone unauthorized silicon wafers for black markets.
- **Logic Locking Fundamentals**: Inserts key-gates (XOR/XNOR or multiplexers) into the combinational logic of the netlist; the chip functions incorrectly unless an activation key is written into secure, tamper-proof on-chip memory post-fabrication.
- **The SAT Attack Threat Vector**: Demonstrates how SAT solver-based oracle attacks (Pramod Subramanyan et al.) deciphered first-generation logic locking schemes by applying distinguishing input patterns to an activated chip and pruning key candidates, forcing the development of SAT-resilient defenses (e.g., Anti-SAT, SARLock, Stripped-Functionality Logic Locking).
- **Split Manufacturing**: Splitting the chip layout into front-end-of-line (FEOL: silicon transistors and low metal layers, fabricated by an advanced offshore foundry) and back-end-of-line (BEOL: high metal layers routing interconnects, completed in a secure domestic facility), preventing the offshore fab from deducing circuit topology.
- **Hardware Trojans & Physical Attacks**: Assesses the stealthy insertion of malicious dormant circuitry triggered by rare count cycles or thermal triggers to leak cryptographic keys or cause catastrophic failure.

---

## Notable Excerpts & Citations

- "In the current horizontal semiconductor business model, design houses possess no physical oversight over fabrication. Trust in hardware cannot be assumed; it must be cryptographically and physically enforced." (source: Protect Your Chip Design IP, Introduction, p. 1)
- "Logic locking bridges the trust gap by ensuring that an IC remains completely unfunctional in the foundry cleanroom, unlocking its full functionality only after secure key provisioning by the design owner." (source: Protect Your Chip Design IP, p. 3)

---

## Thematic Connections & Conceptual Cross-References

- [[the-chips-and-science-act-of-2022]]
- [[nstc-vision-and-strategy-semiconductors]]
- [[nist-cybersecurity-framework-2-0]]

---

## Related entities in Wiki
- [[johann-knechtel]]
- [[satwik-patnaik]]
- [[ozgur-sinanoglu]]
- [[semiconductor-engineering-and-industrial-policy]]
- [[cybersecurity-and-digital-forensics]]
- [[semiconductor-geopolitics-and-chokepoints]]
- [[zero-trust-architecture-and-cryptographic-resilience]]
