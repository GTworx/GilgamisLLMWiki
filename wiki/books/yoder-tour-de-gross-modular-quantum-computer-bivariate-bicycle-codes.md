# Tour de Gross: A Modular Quantum Computer Based on Bivariate Bicycle Codes

**Author(s)**: [[theodore-j-yoder]]
**Publication Year**: 2025
**Genre(s)**: [[quantum-information-science-and-computing]], [[data-science-and-scientific-computing]]
**Key Themes**: [[fault-tolerant-quantum-computing-and-error-correction]], [[quantum-foundations-measurement-and-many-worlds]]
**Source**: `ARTICLES-REPORTS/QuantumCompute/2025 Tour de gross - A modular quantum computer based on bivariate bicycle codes.pdf (68 pp., Theodore J. Yoder, Eddie Schoute, Patrick Rall, Andrew W. Cross, Sergey Bravyi, IBM Quantum 2025)`
**Last updated**: 2026-11-24

---

## Executive Summary

This monumental 68-page system architecture treatise by Theodore J. Yoder, Eddie Schoute, Patrick Rall, Andrew Cross, and Sergey Bravyi at IBM Quantum presents 'Tour de Gross': the definitive engineering and algorithmic blueprint for a modular, fault-tolerant quantum computer based on bivariate bicycle codes. Building on IBM's historic 'gross code' ($[[144, 12, 12]]$ qLDPC code), the authors detail an end-to-end fault-tolerant computing architecture encompassing physical transmon layout, long-range cryogenic microwave interconnects, fault-tolerant logical Clifford gate synthesis, magic-state distillation factories, and fault-tolerant syndrome decoding. The paper provides complete circuit schedules and error budgets, demonstrating that a modular quantum computer with ~10,000 physical qubits can run Shor's algorithm and quantum chemistry simulations that previously required millions of surface-code physical qubits.

---

## Key Strategic, Scientific & Engineering Takeaways

- **The 'Gross Code' Architecture**: Establishes the full systems engineering framework for the $[[144, 12, 12]]$ bivariate bicycle code, which simultaneously encodes 12 high-fidelity logical qubits within a single 144-physical-qubit modular chip.
- **Modular Cryogenic Interconnects**: Resolves the wiring bottleneck by introducing long-range coherent microwave transmission lines and inter-chip cryogenic couplers that route non-local stabilizer checks without thermal overloading.
- **Transversal and Fault-Tolerant Logical Gates**: Formulates transversal Clifford operations and lattice-surgery protocols between logical qubits, drastically simplifying the circuit complexity of fault-tolerant algorithm execution.
- **Magic-State Distillation Optimization**: Details a compact magic-state distillation factory designed specifically for bivariate bicycle codes, reducing non-Clifford $T$-gate overhead by over 80% compared to standard surface code distillation.
- **Complete Systems Execution Blueprint**: Provides an exhaustive gate-level compiler trace for running quantum phase estimation and electronic structure simulations (FeMoco nitrogenase active site), cementing bivariate bicycle codes as the leading architectural candidate for practical quantum advantage.

---

## Notable Excerpts & Citations

- "Tour de Gross presents a complete, viable system architecture for a modular fault-tolerant quantum computer based on bivariate bicycle codes, transforming qLDPC theory into an actionable engineering blueprint." (source: Yoder et al., IBM Quantum 2025, p. 1)
- "By reducing physical qubit overhead by more than an order of magnitude, bivariate bicycle codes bring utility-scale fault-tolerant quantum computing into the realm of near-term semiconductor and cryogenic engineering." (source: Yoder et al., IBM Quantum 2025, p. 45)

---

## Thematic Connections & Conceptual Cross-References

- [[bravyi-high-threshold-and-low-overhead-fault-tolerant-quantum-memory]]
- [[muller-improved-belief-propagation-for-real-time-decoding-of-quantum-memory]]
- [[nature-quantum-computing-milestone-package]]

---

## Related entities in Wiki
- [[theodore-j-yoder]]
- [[quantum-information-science-and-computing]]
- [[data-science-and-scientific-computing]]
- [[fault-tolerant-quantum-computing-and-error-correction]]
- [[quantum-foundations-measurement-and-many-worlds]]
