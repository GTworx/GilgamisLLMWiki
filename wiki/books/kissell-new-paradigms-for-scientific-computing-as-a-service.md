# New Paradigms for Scientific Computing as a Service: Bridging HPC, Cloud, and Quantum Co-Processors

**Author(s)**: [[kevin-kissell]]
**Publication Year**: 2018
**Genre(s)**: [[quantum-information-science-and-computing]], [[cloud-computing-and-distributed-systems]]
**Key Themes**: [[fault-tolerant-quantum-computing-and-error-correction]], [[cloud-native-architecture-and-declarative-infrastructure]]
**Source**: `ARTICLES-REPORTS/QuantumCompute/New Paradigms For Scientific Computing As a Service -Google-kissell.pdf (16 pp., Kevin Kissell, Google Cloud Technical Directorate)`
**Last updated**: 2026-11-24

---

## Executive Summary

Authored by Kevin Kissell of Google Cloud's Technical Directorate, this 16-page systems architecture whitepaper details the structural evolution of High-Performance Computing (HPC) into 'Scientific Computing as a Service'. Kissell outlines how cloud infrastructure modernizes traditional monolithic supercomputing clusters through containerization, Kubernetes orchestration, elastic cloud hardware (TPUs, GPUs), and the eventual integration of quantum co-processors (QPUs). The paper addresses data gravity, petascale parallel storage filesystems (Lustre), high-bandwidth low-latency networking (gVNIC), and the architectural middleware required to orchestrate hybrid classical-quantum scientific workflows.

---

## Key Strategic, Scientific & Engineering Takeaways

- **Deconstructing Monolithic Supercomputing**: Explains how traditional queue-based on-premise supercomputing centers (Slurm/PBS) create massive operational friction, which cloud-native scientific infrastructure eliminates through elastic, on-demand cluster provisioning.
- **Containerization & Orchestration for HPC**: Details the integration of Singularity and Docker containers managed via Kubernetes, enabling reproducible, portable scientific computing pipelines across diverse hardware architectures.
- **Integrating Quantum Co-Processors (QPUs)**: Formulates the systems architecture for hybrid classical-quantum pipelines, where cloud HPC clusters handle heavy data ingestion, preprocessing, and linear algebra, offloading discrete intractable kernel subroutines to QPUs via low-latency API brokers.
- **Storage Fabrics and Data Gravity**: Analyzes petascale scientific data management, contrasting object storage (Google Cloud Storage) with high-throughput parallel filesystems to eliminate I/O starvation on dense GPU/TPU nodes.
- **Economic Model of Elastic Scientific Compute**: Demonstrates how bursting scientific simulations to the cloud drastically reduces total cost of ownership (TCO) compared to over-provisioning static on-premise supercomputing facilities.

---

## Notable Excerpts & Citations

- "Scientific Computing as a Service re-architects how humanity tackles grand computational challenges. By blending elastic cloud orchestration with advanced accelerators and emerging quantum coprocessors, we remove the infrastructure friction that slows discovery." (source: Kissell, Google Cloud Whitepaper, p. 2)
- "The quantum processor of tomorrow will not exist in isolation; it will live as an ultra-specialized coprocessor inside a massive, cloud-native distributed computing fabric." (source: Kissell, Google Cloud Whitepaper, p. 12)

---

## Thematic Connections & Conceptual Cross-References

- [[google-quantum-ai-presents-new-superconducting-quantum-processor]]
- [[1qbit-bringing-quantum-computing-from-theory-to-application]]
- [[project-suncatcher-space-based-ai-infrastructure]]

---

## Related entities in Wiki
- [[kevin-kissell]]
- [[quantum-information-science-and-computing]]
- [[cloud-computing-and-distributed-systems]]
- [[fault-tolerant-quantum-computing-and-error-correction]]
- [[cloud-native-architecture-and-declarative-infrastructure]]
