# Nature Quantum Computing Milestone Package: Architecture, Post-Quantum Cryptography, Software, and Fault-Tolerance

**Author(s)**: [[nature-editorial-consortium]]
**Publication Year**: 2017
**Genre(s)**: [[quantum-information-science-and-computing]], [[data-science-and-scientific-computing]]
**Key Themes**: [[fault-tolerant-quantum-computing-and-error-correction]], [[quantum-foundations-measurement-and-many-worlds]]
**Source**: Multi-volume dossier (7 files):
- `ARTICLES-REPORTS/QuantumCompute/Nature 2017 Quantum Comp Papers/Nature Quantum Cover 2017_.pdf (Nature Vol. 549 Cover & Editorial)`
- `ARTICLES-REPORTS/QuantumCompute/Nature 2017 Quantum Comp Papers/Post-quantum cryptography Nature 2017.pdf (7 pp., Daniel J. Bernstein & Tanja Lange)`
- `ARTICLES-REPORTS/QuantumCompute/Nature 2017 Quantum Comp Papers/Programming languages and compiler design for realistic quantum hardware Nature 2017.pdf (8 pp., Frederic T. Chong, Diana Franklin, Margaret Martonosi)`
- `ARTICLES-REPORTS/QuantumCompute/Nature 2017 Quantum Comp Papers/Quantum computational supremacy Nature 2017.pdf (7 pp., Aram W. Harrow & Ashley Montanaro)`
- `ARTICLES-REPORTS/QuantumCompute/Nature 2017 Quantum Comp Papers/Quantum machine learning Nature 2017.pdf (8 pp., Jacob Biamonte, Peter Wittek, Nicola Pancotti et al.)`
- `ARTICLES-REPORTS/QuantumCompute/Nature 2017 Quantum Comp Papers/Roads towards fault-tolerant universal quantum computation Nature 2017.pdf (8 pp., Earl T. Campbell, Barbara M. Terhal, Christoph Vuillot)`
- `ARTICLES-REPORTS/QuantumCompute/Nature Google IBM 2017 03.pdf (Nature Special Feature on the Google vs. IBM Superconducting Race)`
**Last updated**: 2026-11-24

---

## Executive Summary

This landmark 7-part canonical collection comprises the historic September 2017 Nature Special Insight Package alongside Nature's investigative coverage of the Google vs. IBM superconducting race. Representing a defining watershed in quantum information science, the compendium features foundational review treatises authored by the world's foremost quantum theorists and systems engineers. Bernstein & Lange provide the definitive roadmap for post-quantum cryptography (lattice-based, code-based, multivariate, and hash-based signatures resistant to Shor's algorithm). Harrow & Montanaro establish the rigorous theoretical complexity foundations of quantum computational supremacy. Chong, Franklin, and Martonosi detail quantum programming languages and compiler optimizations for intermediate-representation (QIR) mapping to noisy hardware. Biamonte et al. synthesize quantum machine learning algorithms (HHL linear solvers, quantum PCA, and quantum Boltzmann machines). Campbell, Terhal, and Vuillot evaluate the architectural roads to fault-tolerant universal quantum computation across surface codes, color codes, and topological quantum memory.

---

## Key Strategic, Scientific & Engineering Takeaways

- **Post-Quantum Cryptographic Migration**: Daniel J. Bernstein and Tanja Lange outline the urgent timeline required to standardize and deploy post-quantum cryptographic primitives (NIST PQC) before cryptanalytically relevant quantum computers (CRQCs) compromise RSA and elliptic curve public-key infrastructure.
- **Supremacy Complexity Foundations**: Aram Harrow and Ashley Montanaro formalize the computational complexity proofs demonstrating why random circuit sampling and boson sampling on noisy intermediate-scale quantum (NISQ) devices cannot be efficiently simulated by classical Turing machines under standard complexity conjectures (#P-hardness).
- **Quantum Software and Compiler Stack**: Chong, Franklin, and Martonosi formulate the hardware-aware software abstraction layers necessary to map high-level quantum algorithms onto constrained physical topologies with limited qubit connectivity and short coherence times ($T_1, T_2$).
- **Quantum Machine Learning Frontiers**: Jacob Biamonte et al. analyze exponential vs. polynomial speedups in quantum linear algebra algorithms, identifying data loading (the 'input problem') as the critical bottleneck for practical quantum advantage in classical data domains.
- **Fault-Tolerance Roadmaps**: Campbell, Terhal, and Vuillot demonstrate that universal fault-tolerant computation requires physical error rates well below surface code fault-tolerance thresholds (~1%) combined with high-overhead magic-state distillation for non-Clifford gates.
- **Google vs. IBM Superconducting Race**: Documents the strategic divergence between Google Quantum AI (focusing on planar transmon 2D grids for rapid supremacy demonstration) and IBM Quantum (focusing on heavy-hex lattices and cloud-accessible quantum ecosystem software via Qiskit).

---

## Notable Excerpts & Citations

- "Quantum computers promise to revolutionize computation by exploiting quantum superposition and entanglement, but realizing this promise requires conquering decoherence through fault-tolerant quantum error correction." (source: Nature Quantum Insight, Editorial, p. 171)
- "If we wait until a large quantum computer is built to begin deploying post-quantum cryptography, it will be far too late. The migration of global communication infrastructure requires decades of cryptographic engineering." (source: Bernstein & Lange, Post-quantum cryptography, p. 188)

---

## Thematic Connections & Conceptual Cross-References

- [[bravyi-high-threshold-and-low-overhead-fault-tolerant-quantum-memory]]
- [[arute-quantum-supremacy-using-a-programmable-superconducting-processor]]
- [[schuld-is-quantum-advantage-the-right-goal-for-quantum-machine-learning]]

---

## Related entities in Wiki
- [[nature-editorial-consortium]]
- [[quantum-information-science-and-computing]]
- [[data-science-and-scientific-computing]]
- [[fault-tolerant-quantum-computing-and-error-correction]]
- [[quantum-foundations-measurement-and-many-worlds]]
