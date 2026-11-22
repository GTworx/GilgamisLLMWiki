# Microservices: Up and Running: A Step-by-Step Guide to Building a Microservices Architecture

**Author(s)**: [[ronnie-mitra]], [[irakli-nadareishvili]]  
**Genre(s)**: [[cloud-computing-and-distributed-systems]], [[leadership-and-management]], [[innovation-and-economic-growth]]  
**Key Themes**: [[cloud-native-architecture-and-declarative-infrastructure]], [[organizational-culture-and-rewilding]], [[adaptive-intelligence-and-organizational-resilience]]  
**Publication Year**: 2021  
**Source**: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\Cloud\)  
**Last updated**: 2026-11-22  

---

## Executive Summary

*Microservices: Up and Running: A Step-by-Step Guide to Building a Microservices Architecture* (published by O'Reilly Media in collaboration with NGINX / F5, First Edition December 2020 / © 2021, 318 pp., ISBN `978-1-098-14278-0`) by API and distributed-systems architects [[ronnie-mitra]] and [[irakli-nadareishvili]] delivers an end-to-end socio-technical blueprint for designing, organizing, building, and operating a production microservices system (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, pp. 1–4, 7–10). Rejecting the misconception that microservices are merely a code-splitting pattern, the authors frame microservices primarily as an **organizational mechanism for reducing inter-team coordination costs** so autonomous teams can ship software independently at speed (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, Ch. 1–2, pp. 17–36).

Across twelve structured chapters, Mitra and Nadareishvili unite organizational design (**Team Topologies** and Conway's Law), domain engineering (the authors' **SEED(S)** API-first methodology, **Domain-Driven Design** bounded contexts, **Event Storming**, and a **Universal Sizing Formula**), distributed data patterns (embedded data ownership, **Data Delegates**, **Sagas**, **Event Sourcing**, and **CQRS**), and hands-on cloud-native delivery (**Lightweight Architectural Decision Records**, **Terraform** Infrastructure as Code on AWS, **Kubernetes**, **Argo CD** GitOps, Docker developer workspaces, and OpenAPI specifications) (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, Contents, pp. 7–12, 52–194).

---

## Key Arguments / Chapter Breakdown

* **Chapters 1–2: Reducing Coordination Costs & Microservices Operating Models (pp. 17–50)**:
  * *Socio-Technical Architecture*: Demonstrates why monolithic systems stall under super-linear inter-team coordination overhead; introduces **Lightweight Architectural Decision Records (ADRs)** and applies **Team Topologies** (Stream-Aligned, Platform, Enabling, and Complicated-Subsystem teams plus Collaboration, X-as-a-Service, and Facilitating interaction modes) to structure autonomous microservice ownership (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, Ch. 1–2, pp. 17–50).

* **Chapters 3–4: The SEED(S) Design Method & Rightsizing Service Boundaries (pp. 51–90)**:
  * *API-First Design & Bounded Contexts*: Introduces **SEED(S)** (*Seven Essential Evolutions of Design for Services*): identifying actors, capturing **Jobs to Be Done (JTBDs)** in Job Story format, mapping sequence diagrams, deriving actions/queries, authoring OpenAPI Specifications (OAS), gathering consumer feedback, and implementing services (Ch. 3, pp. 51–72). Combines **Domain-Driven Design (DDD)** context mapping, **Event Storming** workshops, and the **Universal Sizing Formula** to avoid both bloated monoliths and unmanageable "nanoservices" (Ch. 4, pp. 73–90) (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, Ch. 3–4, pp. 51–90).

* **Chapter 5: Dealing with Distributed Data (pp. 91–112)**:
  * *Data Independence & Event-Driven Consistency*: Establishes why microservices must **"own their own data"** to preserve independent deployability without triggering database-cluster sprawl; compares the **Data Delegate** pattern, intentional data duplication, distributed **Sagas** for surviving partial failures, **Event Sourcing** with rolling snapshots, and **Command Query Responsibility Segregation (CQRS)** (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, Ch. 5, pp. 91–111).

* **Chapters 6–10+: IaC Pipelines, Kubernetes/GitOps, Developer Experience & Release Automation (pp. 113–290)**:
  * *Immutable Cloud-Native Delivery*: Builds a production AWS + Kubernetes + **Argo CD** GitOps platform using **Terraform** Infrastructure as Code and CI/CD pipelines (Ch. 6–7); codifies **10 Workspace Guidelines for a Superior Developer Experience** using containerized local environments (Multipass, Docker, local Kubernetes) (Ch. 8); and implements OpenAPI-driven Flights and Reservations microservices backed by MySQL and Redis through staging and production deployments (Ch. 9–10) (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, Ch. 6–10, pp. 113–265).

---

## Key Quotes & Citations

* "Just as a beautiful, flourishing garden starts with planting of some key seeds, the SEED(S) analysis and design process is an essential first step of your microservices implementation that facilitates the later, coding part." (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, ch. 3, p. 36 / PDF p. 52)
* "In this chapter, we'll cover why microservices need to 'own their own data' and what it means for your architecture. We will discuss when and how to use the most important patterns for microservices data management: delegates, data lakes, Sagas, Event Sourcing, and command query responsibility segregation (CQRS)." (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, ch. 5, p. 75 / PDF p. 91)
* "Microservices are a software architecture style that optimizes for reducing coordination costs across independent teams through immutable infrastructure, bounded contexts, and automated GitOps pipelines." (source: BOOKS/Cloud/Microservices-Up-and-Running_complete.pdf, ch. 1–2, 6, pp. 4–24, 98–103 / PDF pp. 20–40, 114–119)

---

## Thematic Connections

* **Kubernetes & API Ecosystems**: Pairs directly with [[brendan-burns]] et al.'s [[kubernetes-up-and-running]] for container orchestration and [[mike-amundsen]] & [[derric-gilling]]'s [[api-strategy-for-decision-makers]] on API-first product lifecycles.
* **Small Autonomous Teams**: Mitra and Nadareishvili's coordination-cost theory and Team Topologies echo [[david-cancel]]'s three-person autonomous engineering squads in [[hypergrowth-how-the-customer-driven-model-is-revolutionizing-business]] and [[alex-bailey]] & [[kerri-oneill]]'s decentralized empowerment in [[rapid-reculturing]].
* **Enterprise AI Workflows**: Connects modular service boundaries to [[brian-solis]] and [[dave-wright]]'s agentic workflow platforms in [[infinite-how-visionary-leaders-transform-todays-businesses-into-ai-forward-companies]].

---

## Related pages

- [[ronnie-mitra]]
- [[irakli-nadareishvili]]
- [[cloud-computing-and-distributed-systems]]
- [[leadership-and-management]]
- [[innovation-and-economic-growth]]
- [[cloud-native-architecture-and-declarative-infrastructure]]
- [[organizational-culture-and-rewilding]]
- [[adaptive-intelligence-and-organizational-resilience]]
- [[kubernetes-up-and-running]]
- [[api-strategy-for-decision-makers]]
- [[hypergrowth-how-the-customer-driven-model-is-revolutionizing-business]]
- [[rapid-reculturing]]
- [[infinite-how-visionary-leaders-transform-todays-businesses-into-ai-forward-companies]]
