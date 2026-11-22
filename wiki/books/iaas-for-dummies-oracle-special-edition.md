# IaaS For Dummies, 2nd Oracle Special Edition

**Author(s)**: [[lawrence-c-miller]]  
**Genre(s)**: [[cloud-computing-and-distributed-systems]], [[innovation-and-economic-growth]]  
**Key Themes**: [[cloud-native-architecture-and-declarative-infrastructure]], [[general-purpose-technologies-and-learning-by-doing]], [[adaptive-intelligence-and-organizational-resilience]]  
**Publication Year**: 2018  
**Source**: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\Cloud\)  
**Last updated**: 2026-11-22  

---

## Executive Summary

*IaaS For Dummies, 2nd Oracle Special Edition* (published by John Wiley & Sons, 2018, 69 pp., ISBN `978-1-119-54515-6`) by enterprise IT and cybersecurity author [[lawrence-c-miller]] (CISSP) provides CIOs, CTOs, and enterprise architects with a structured architectural primer on **Infrastructure as a Service (IaaS)** and the transition from first-generation multi-tenant virtualization to **second-generation cloud infrastructure** (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, pp. 3–4, 7–11). Cutting through industry **"cloudwashing"** (Gartner's term for rebranding legacy software as cloud), Miller grounds cloud computing in NIST's five essential characteristics (*on-demand self-service, broad network access, resource pooling, rapid elasticity, measured service*) and maps the shared-responsibility demarcation lines separating IaaS, PaaS, and SaaS (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, Ch. 1, pp. 10–11).

Across five chapters, Miller details why mission-critical enterprise workloads demand **predictable low-latency performance**, isolation, and regulatory control that noisy-neighbor first-generation VMs struggled to deliver—introducing **on-demand single-tenant bare-metal compute**, NVMe local flash, non-oversubscribed cloud networking, managed Kubernetes containers, and dedicated private cloud interconnects (`FastConnect` vs. IPSec VPN) (Ch. 1–3). He concludes with five core enterprise migration blueprints—datacenter evacuation, High-Performance Computing (HPC), cloud-native application development, cloud archiving, and lift-and-shift modernization—followed by ten architectural evaluation criteria for enterprise IaaS (Ch. 4–5) (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, Contents, pp. 5–6, 20–65).

---

## Key Arguments / Chapter Breakdown

* **Chapter 1: Cloud Fundamentals & Enterprise Workloads (pp. 9–19)**:
  * *Second-Generation IaaS*: Establishes the NIST cloud taxonomy (Public, Private, Hybrid; SaaS, PaaS, IaaS) and explains how second-generation IaaS extends customer control deeper into the stack via **single-tenant bare-metal servers** alongside VMs, delivering deterministic latency, high throughput, and predictable performance for mission-critical ERP and database workloads (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, Ch. 1, pp. 10–17).

* **Chapter 2: Core Cloud Infrastructure Primitives — Compute, Storage & Networking (pp. 20–33)**:
  * *Full-Stack Infrastructure Architecture*: Surveys bare-metal and VM compute shapes, managed **Container Engine for Kubernetes**, hybrid on-premises **Cloud at Customer**, tiered storage (**Local NVMe**, Block Volumes, File Storage, Object Storage, Archive Storage), managed database services, and isolated Virtual Cloud Networks (VCNs) (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, Ch. 2, pp. 20–33).

* **Chapters 3–5: Hybrid Connectivity, Enterprise Use Cases & Ten IaaS Evaluation Pillars (pp. 34–66)**:
  * *Migration Playbooks*: Contrasts dedicated private-circuit connectivity (`FastConnect`) with encrypted public-Internet VPNs (Ch. 3); examines five production IaaS patterns—datacenter migration, **High-Performance Computing (HPC)**, cloud-native apps, archival storage, and **lift-and-shift** (Ch. 4); and distills ten enterprise IaaS pillars: *Performance, Predictability, Availability, Openness, Versatility, Visibility, Control, Management, Scalability,* and database optimization (Ch. 5) (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, Ch. 3–5, pp. 34–65).

---

## Key Quotes & Citations

* "The days of purchasing hardware and maintaining massive data centers to run IT must come to an end. Managing and maintaining your infrastructure is simply too expensive... Utilizing an infrastructure with an elastic, pay-as-you-go service model not only reduces costs and worries, but also frees IT organizations to innovate in ways that will enhance business growth." (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, Introduction, p. 1 / PDF p. 7)
* "To try to cut down a bit on the cloudwashing (a term Gartner uses to refer to the marketing practice of adding the word cloud to practically any technology product or service), let's keep it simple. There are five essential characteristics of the cloud (as defined by NIST): On-demand self-service; Broad network access; Resource pooling; Rapid elasticity; Measured service." (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, ch. 1, p. 4 / PDF p. 10)
* "Whereas first-generation IaaS offerings provide cloud-based virtual machines (VMs) in a multitenant environment... second-generation IaaS offerings can additionally provide on-demand, single-tenant 'bare metal' machines." (source: BOOKS/Cloud/Book IaaS_For_Dummies_2nd_Oracle_Special_Edition.pdf, ch. 1, p. 5 / PDF p. 11)

---

## Thematic Connections

* **Public vs. Hyperconverged Private Cloud**: Directly dialogues with [[scott-d-lowe]]'s [[enterprise-cloud-for-dummies-nutanix-special-edition]], which argues for bringing public-cloud agility back into hyperconverged on-premises enterprise clouds.
* **Miller's Enterprise Cloud & IoT Canon**: Bridges [[lawrence-c-miller]]'s [[iot-for-dummies-applications-solutions-and-security-compendium]] at the edge with [[lawrence-c-miller]]'s [[saas-for-dummies-oracle-special-edition]] at the application layer.
* **Container Orchestration & Cost Governance**: Connects bare-metal/VM IaaS foundations to [[brendan-burns]] et al.'s [[kubernetes-up-and-running]] and [[flexera-research]]'s [[state-of-it-asset-management-2022]].

---

## Related pages

- [[lawrence-c-miller]]
- [[cloud-computing-and-distributed-systems]]
- [[innovation-and-economic-growth]]
- [[cloud-native-architecture-and-declarative-infrastructure]]
- [[general-purpose-technologies-and-learning-by-doing]]
- [[adaptive-intelligence-and-organizational-resilience]]
- [[enterprise-cloud-for-dummies-nutanix-special-edition]]
- [[saas-for-dummies-oracle-special-edition]]
- [[iot-for-dummies-applications-solutions-and-security-compendium]]
- [[kubernetes-up-and-running]]
- [[state-of-it-asset-management-2022]]
