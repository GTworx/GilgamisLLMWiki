# Characterizing Quantum Supremacy in Near-Term Devices

**Author(s)**: [[sergio-boixo]]
**Publication Year**: 2016
**Genre(s)**: [[quantum-information-science-and-computing]], [[data-science-and-scientific-computing]]
**Key Themes**: [[fault-tolerant-quantum-computing-and-error-correction]], [[quantum-foundations-measurement-and-many-worlds]]
**Source**: `ARTICLES-REPORTS/QuantumCompute/Characterizing Quantum Supremacy in Near-Term Devices 2016.pdf (23 pp., Sergio Boixo, Sergei V. Isakov, Vadim N. Smelyanskiy, Ryan Babbush, Nan Ding, Zhang Jiang, Michael J. Bremner, John M. Martinis, Hartmut Neven, Google Quantum AI)`
**Last updated**: 2026-11-24

---

## Executive Summary

This seminal 23-page theoretical foundation paper by Sergio Boixo, John M. Martinis, Hartmut Neven, and the Google Quantum AI team established the comprehensive mathematical, complexity-theoretic, and experimental framework for demonstrating quantum computational supremacy using near-term noisy superconducting processors. Published three years prior to the historic Sycamore experiment, the authors formalize random circuit sampling on 2D square lattices of superconducting qubits, introduce cross-entropy benchmarking (XEB) to measure fidelity, and establish the computational complexity proofs demonstrating why classical supercomputers cannot sample from the resulting Porter-Thomas probability distributions.

---

## Key Strategic, Scientific & Engineering Takeaways

- **Foundational Paradigm of Quantum Supremacy**: Formalizes the proposal to demonstrate quantum computational supremacy using 40–50 noisy superconducting qubits executing pseudorandom quantum circuits.
- **Porter-Thomas Distribution & Anti-Concentration**: Proves that random quantum circuits scramble quantum information rapidly, causing output probabilities to anti-concentrate and follow a Porter-Thomas distribution that is #P-hard for classical Turing machines to simulate.
- **Formulation of Cross-Entropy Benchmarking (XEB)**: Introduces the XEB statistical metric, allowing researchers to verify that a physical quantum processor is genuinely sampling from the exponentially complex target quantum state in the presence of noise.
- **Experimental Hardware Specifications**: Specifies the precise physical requirements—two-qubit gate fidelities exceeding 99%, low crosstalk, and individual qubit readout—that guided Google's hardware roadmap from Foxtail and Bristlecone to Sycamore.
- **The Complexity Boundary**: Concludes that a 49-qubit quantum processor operating at depth 20 exceeds the memory and computational capacity of the world's largest classical supercomputers, establishing the benchmark that defined the era of quantum supremacy.

---

## Notable Excerpts & Citations

- "A foundational question in quantum information science is whether quantum processors without error correction can outperform classical computers on well-defined computational tasks. Here we propose a concrete scheme to achieve quantum supremacy." (source: Boixo et al., 2016, Abstract, p. 1)
- "Sampling from the output distribution of random quantum circuits is computationally intractable for classical computers, providing a rigorous and experimentally accessible milestone for quantum computational advantage." (source: Boixo et al., 2016, p. 12)

---

## Thematic Connections & Conceptual Cross-References

- [[arute-quantum-supremacy-using-a-programmable-superconducting-processor]]
- [[zlokapa-boundaries-of-quantum-supremacy-via-random-circuit-sampling]]
- [[nature-quantum-computing-milestone-package]]

---

## Related entities in Wiki
- [[sergio-boixo]]
- [[quantum-information-science-and-computing]]
- [[data-science-and-scientific-computing]]
- [[fault-tolerant-quantum-computing-and-error-correction]]
- [[quantum-foundations-measurement-and-many-worlds]]
