# Boundaries of Quantum Supremacy via Random Circuit Sampling

**Author(s)**: [[alexander-zlokapa]]
**Publication Year**: 2023
**Genre(s)**: [[quantum-information-science-and-computing]], [[data-science-and-scientific-computing]]
**Key Themes**: [[fault-tolerant-quantum-computing-and-error-correction]], [[quantum-foundations-measurement-and-many-worlds]]
**Source**: `ARTICLES-REPORTS/QuantumCompute/Boundaries of quantum supremacy via random circuit sampling Quantum Information 2023.pdf (8 pp., Alexander Zlokapa, Benjamin Villalonga, Sergio Boixo, Daniel Lidar, npj Quantum Information 2023)`
**Last updated**: 2026-11-24

---

## Executive Summary

Authored by Alexander Zlokapa (MIT), Benjamin Villalonga (Google Quantum AI), Sergio Boixo (Google Quantum AI), and Daniel Lidar (USC), this 8-page npj Quantum Information (2023) paper rigorously maps the shifting theoretical and computational boundaries between quantum supremacy and classical simulation algorithms for Random Circuit Sampling (RCS). Following Google's 2019 Sycamore demonstration, classical supercomputing teams developed advanced tensor network methods, matrix product states, and heuristic sampling algorithms that drastically reduced classical simulation runtimes. The authors analyze the fundamental trade-offs among circuit depth, qubit count, hardware noise floors, and classical computational complexity, proving that an intractable quantum supremacy regime remains robust when circuit depth and fidelity exceed strict scaling thresholds.

---

## Key Strategic, Scientific & Engineering Takeaways

- **The Shifting Classical-Quantum Boundary**: Analyzes the multi-year battle between classical simulation optimizations (tensor network contraction, Feynman path integrals) and quantum hardware scaling.
- **Stability Against Tensor-Network Slicing**: Proves that while low-depth or high-noise random quantum circuits can be approximated by classical tensor network contractions, increasing circuit depth to the full anti-concentration regime restores exponential classical simulation hardness.
- **Noise-Induced Classical Simulability**: Rigorously characterizes how physical gate errors and decoherence attenuate quantum interference, establishing an upper bound on circuit depth beyond which noise renders the circuit classically simulable.
- **Linear Cross-Entropy Benchmarking (XEB) Precision**: Demonstrates how XEB fidelity serves as a mathematically sound estimator of quantum state complexity, disproving classical spoofing claims that fail to preserve global Porter-Thomas output distributions.
- **Asymptotic Supremacy Criteria**: Concludes that quantum supremacy via random circuit sampling is not a fleeting transient state, but a fundamental complexity-theoretic reality when hardware error rates drop below critical threshold values.

---

## Notable Excerpts & Citations

- "We map the boundary between quantum advantage and classical simulability for random circuit sampling, demonstrating that classical tensor network algorithms cannot keep pace with scaling qubit counts and declining gate error rates." (source: Zlokapa et al., npj Quantum Information 2023, p. 1)
- "While classical algorithms have steadily improved, the exponential scaling of the Hilbert space ensures that a fault-resistant quantum processor operating beyond the anti-concentration depth remains fundamentally intractable for classical supercomputers." (source: Zlokapa et al., npj Quantum Information 2023, p. 7)

---

## Thematic Connections & Conceptual Cross-References

- [[boixo-characterizing-quantum-supremacy-in-near-term-devices]]
- [[arute-quantum-supremacy-using-a-programmable-superconducting-processor]]
- [[decross-computational-power-of-random-quantum-circuits-in-arbitrary-geometries]]

---

## Related entities in Wiki
- [[alexander-zlokapa]]
- [[quantum-information-science-and-computing]]
- [[data-science-and-scientific-computing]]
- [[fault-tolerant-quantum-computing-and-error-correction]]
- [[quantum-foundations-measurement-and-many-worlds]]
