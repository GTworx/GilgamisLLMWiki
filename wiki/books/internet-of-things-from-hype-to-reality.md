# Internet of Things From Hype to Reality: The Road to Digitization

**Author(s)**: [[ammar-rayes]], [[samer-salam]]  
**Genre(s)**: [[internet-of-things-and-edge-computing]], [[cloud-computing-and-distributed-systems]], [[cybersecurity-and-digital-forensics]]  
**Key Themes**: [[iot-cyber-physical-convergence-and-edge-security]], [[cloud-native-architecture-and-declarative-infrastructure]], [[decentralized-trust-and-cryptographic-governance]]  
**Publication Year**: 2019  
**Source**: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\IoT\)  
**Last updated**: 2026-11-22  

---

## Executive Summary

*Internet of Things From Hype to Reality: The Road to Digitization (Second Edition)* (published by Springer Nature Switzerland, 2019, 393 pp., `DOI: 10.1007/978-3-319-99516-8`, with Forewords by IBM's Jim Spohrer and networking systems leaders) by Cisco Distinguished Engineer [[ammar-rayes]] and Cisco Principal Engineer [[samer-salam]] is a comprehensive engineering textbook and strategic architecture blueprint bridging the gap between IoT hype and production-grade digitization (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, pp. 3–11, 25–26). Framing IoT as the technical foundation of the **Fourth Industrial Revolution**—interconnected cyber-physical systems of systems—the authors articulate a core architectural thesis: while the traditional Internet converged on **IP as the single "thin waist" of the protocol hourglass** to normalize connectivity, the Internet of Things shifts the center of gravity from connectivity to **actionable data**, requiring a **second thin waist** for application services, data semantics, and programmable interoperability (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Preface, pp. 10–11).

Spanning twelve chapters plus a glossary and engineering student project appendix, Rayes and Salam build systematically from bottom to top: the **"12 Factors for a Perfect Storm"** driving IT/OT convergence (Chapter 1), TCP/IP and IPv6 networking fundamentals (Chapter 2), sensors, RFID, video tracking, and actuators (Chapter 3), constrained-device networking requirements and determinism (Chapter 4), the layered IoT protocol stack from IEEE 802.15.4e TSCH, LoRaWAN, IEEE 802.11ah, and Time-Sensitive Networking to 6LoWPAN, RPL, 6TiSCH, CoAP, and MQTT (Chapter 5), distributed **Fog Computing** (Chapter 6), IoT Services Platforms (Chapter 7), end-to-end security and privacy (Chapter 8, co-authored with Mehiar Dabbagh), vertical ecosystems (Chapter 9), **Blockchain in IoT** for decentralized governance (Chapter 10, with Carlos Davila and Jacob Tarnow), and global standards and open-source foundations (Chapters 11–12) (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Contents, pp. 18–24, 178–348).

---

## Key Arguments / Chapter Breakdown

* **Chapters 1–3: IoT Reference Framework, The 12-Factor Perfect Storm, Networking & Cyber-Physical Transducers (pp. 27–111)**:
  * *IT/OT Convergence & Transducers*: Traces how IT/OT convergence, creative internet platforms (Uber, Airbnb, Square, Amazon, Tesla), edge analytics, cloud virtualization, and Moore's Law accelerated IoT adoption five times faster than electricity or telephony; establishes OSI/TCP-IP foundations (IPv4 vs. IPv6 addressing, latency, packet loss, routing) and details physical sensors, RFID identification, video tracking algorithms, and actuators (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Ch. 1–3, pp. 27–108).

* **Chapters 4–5: Constrained Networking Requirements & The Layered IoT Protocol Stack (pp. 112–177)**:
  * *Massive Scalability & Determinism*: Explains why industrial IoT demands constrained-node operation, deterministic bounded latency, and semantic interoperability; dissects Link Layer protocols (`IEEE 802.15.4`, `802.15.4e TSCH`, `LoRaWAN` LPWAN classes, `IEEE 802.11ah`, and `Time-Sensitive Networking` 802.1Qca/Qbv/CB), Internet Layer adaptations (`6LoWPAN`, `RPL`, `6TiSCH`), and Application Layer paradigms (Request/Response vs. Publish/Subscribe, QoS, serialization) (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Ch. 4–5, pp. 112–157).

* **Chapters 6–8: Fog Computing, IoT Services Platforms, and Security & Privacy (pp. 178–260)**:
  * *Extending Cloud to the Edge*: Defines **Fog Computing** as a distributed horizontal architecture extending compute, storage, and networking close to edge sensors to satisfy ultra-low latency, bandwidth conservation, and local autonomy; specifies IoT Services Platform lifecycle management (provisioning, configuration, telemetry, troubleshooting); and catalogs IoT threat vectors and cryptographic defenses across hardware, network, and cloud layers (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Ch. 6–8, pp. 178–260).

* **Chapters 9–12: Vertical Markets, Blockchain in IoT, Standards & Open Source (pp. 261–348)**:
  * *Ecosystems & Decentralized Trust*: Maps IoT business models across energy, industrial manufacturing, retail, transportation, finance, healthcare, and agriculture; examines how **blockchain** replaces centralized intermediaries for autonomous machine-to-machine identity and settlement (Ch. 10); and surveys standardization bodies (IETF, IEEE, ITU, oneM2M, OCF) alongside open-source IoT initiatives (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Ch. 9–12, pp. 261–348).

---

## Key Quotes & Citations

* "As the Internet evolves into the Internet of Things, the focus shifts from connectivity to data. The Internet of Things is primarily about data and gaining actionable insights from that data... How does this translate to the proverbial hourglass? At the very least, a second thin waist is required which provides a common normalization layer for application services." (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Preface, pp. xi–xii / PDF pp. 10–11)
* "To invent, you need the Internet, communication, good imagination and a pile of things." (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Dedication, PDF p. 5)
* "How the Internet of Things will bend and mold the IP hourglass in the decades to come will certainly be fascinating to witness. We, as engineers, developers, researchers, business leaders, consumers and human beings are in the vortex of this transformation." (source: BOOKS/IoT/2019_Book_InternetOfThingsFromHypeToReal.pdf, Dedication & Preface, PDF pp. 5, 11)

---

## Thematic Connections

* **Executive IoT & Hardware Security Companion**: Provides the full protocol-level engineering rigor beneath [[lawrence-c-miller]]'s practitioner trilogy [[iot-for-dummies-applications-solutions-and-security-compendium]] on [[iot-cyber-physical-convergence-and-edge-security]].
* **Cloud & Data-Intensive Platforms**: Connects edge telemetry and Fog Computing directly to [[william-waddington]] et al.'s [[architecting-data-intensive-saas-applications]] and [[joyce-kay-avila]]'s [[snowflake-the-definitive-guide]] on processing massive time-series IoT streams in cloud data platforms.
* **Blockchain & Decentralized Governance**: Chapter 10's decentralized IoT identity model dialogues with [[marco-di-maggio]]'s [[blockchain-crypto-and-defi-bridging-finance-and-technology]] and [[michael-bradley]] et al.'s [[getting-started-with-enterprise-blockchain]].
* **General Purpose Technologies**: Mirrors [[richard-g-lipsey]] et al.'s [[economic-transformations-general-purpose-technologies-and-long-term-economic-growth]] on how Fourth Industrial Revolution infrastructure reshapes industrial organization.

---

## Related pages

- [[ammar-rayes]]
- [[samer-salam]]
- [[internet-of-things-and-edge-computing]]
- [[cloud-computing-and-distributed-systems]]
- [[cybersecurity-and-digital-forensics]]
- [[iot-cyber-physical-convergence-and-edge-security]]
- [[cloud-native-architecture-and-declarative-infrastructure]]
- [[decentralized-trust-and-cryptographic-governance]]
- [[iot-for-dummies-applications-solutions-and-security-compendium]]
- [[architecting-data-intensive-saas-applications]]
- [[snowflake-the-definitive-guide]]
- [[blockchain-crypto-and-defi-bridging-finance-and-technology]]
- [[getting-started-with-enterprise-blockchain]]
- [[economic-transformations-general-purpose-technologies-and-long-term-economic-growth]]
