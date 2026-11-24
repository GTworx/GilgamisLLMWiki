# Industrial IoT at Scale: Predix Platform Architecture, Edge Analytics, and Digital Twin Lexicon

**Author(s)**: [[ge-digital]]
**Publication Year**: 2018
**Genre(s)**: [[internet-of-things-and-industrial-automation]], [[cloud-computing-and-distributed-systems]]
**Key Themes**: [[industrial-iot-edge-telemetry-and-it-ot-convergence]], [[general-purpose-technologies-and-learning-by-doing]]
**Source**: Multi-volume dossier (2 files):
- `ARTICLES-REPORTS/IoT/Dolbec GED at Scale.pdf (13 pp., Vincent Dolbec, GE Digital Platform Architecture Case Study)`
- `ARTICLES-REPORTS/IoT/GE_Digital_Glossary[1].pdf (6 pp., GE Digital Industrial Internet of Things Lexicon)`
**Last updated**: 2026-11-24

---

## Executive Summary

This two-part technical systems architecture dossier by GE Digital investigates the engineering blueprints, edge-to-cloud data fabrics, and operational concepts behind deploying the Industrial Internet of Things (IIoT) at enterprise scale. Authored by GE Digital architect Vincent Dolbec alongside GE's official IIoT terminology lexicon, the dossier details the architecture of the Predix platform—General Electric's pioneering cloud platform for industrial asset performance management (APM). The works explain how sensor time-series telemetry from heavy industrial machinery (jet engines, gas turbines, locomotives, wind farms) is processed via edge gateways, ingested into scalable cloud time-series data stores, and mapped into high-fidelity 'Digital Twins' to optimize operating efficiency and prevent catastrophic mechanical failures.

---

## Key Strategic, Operational & Technical Takeaways

- **The Concept of the Digital Twin**: Defines the Digital Twin as a dynamic, physics-based and data-driven computational model of a physical asset, continuously updated with real-time operational telemetry to simulate wear, efficiency, and remaining useful life (RUL).
- **Edge-to-Cloud Distributed Processing**: Explains why heavy industrial analytics cannot be entirely cloud-hosted: high-frequency vibration data (kHz sampling) must be filtered, normalized, and acted upon at the edge to trigger sub-second safety interlocks.
- **Time-Series Telemetry Ingestion at Scale**: Outlines scalable ingestion pipelines built to absorb millions of sensor events per second, contrasting relational databases with specialized columnar time-series storage engines.
- **Asset Performance Management (APM)**: Details how predictive analytics eliminate unplanned downtime across airline fleets and power generation grids, transitioning industrial maintenance from reactive calendar schedules to condition-based intervention.
- **Standardizing Industrial Terminology**: The accompanying lexicon codifies foundational terms—from Edge Execution Environments and Data Historians to SCADA abstraction layers and Asset Information Models.

---

## Notable Excerpts & Citations

- "The Industrial Internet is not about consumer gadgets; it is about keeping multi-million-dollar gas turbines spinning and jet engines flying safely through predictive mathematical intelligence." (source: GE Digital at Scale, p. 2)
- "A Digital Twin is a living computational replica of a physical machine. By blending sensor telemetry with thermodynamic physics models, we can predict mechanical failure weeks before a physical vibration is detectable." (source: GE Digital Glossary, p. 1)

---

## Thematic Connections & Conceptual Cross-References

- [[schneider-electric-ecostruxure-and-smart-energy-architecture]]
- [[industrial-cybersecurity-alliance-it-ot-convergence]]
- [[mckinsey-building-an-industrial-saas-software-business]]

---

## Related entities in Wiki
- [[ge-digital]]
- [[internet-of-things-and-industrial-automation]]
- [[cloud-computing-and-distributed-systems]]
- [[industrial-iot-edge-telemetry-and-it-ot-convergence]]
- [[general-purpose-technologies-and-learning-by-doing]]
