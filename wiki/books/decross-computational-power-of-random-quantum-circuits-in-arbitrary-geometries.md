# The Computational Power of Random Quantum Circuits in Arbitrary Geometries

**Author(s)**: [[michael-decross]]
**Publication Year**: 2024
**Genre(s)**: [[quantum-information-science-and-computing]], [[data-science-and-scientific-computing]]
**Key Themes**: [[fault-tolerant-quantum-computing-and-error-correction]], [[quantum-foundations-measurement-and-many-worlds]]
**Source**: `ARTICLES-REPORTS/QuantumCompute/2024 The computational power of random quantum circuits in arbitrary geometries.pdf (36 pp., M. DeCross, R. Haghshenas, M. Liu, E. Rinaldi, J. Gray, Y. Alexeev, C. H. Baldwin et al., Quantinuum / Argonne National Laboratory)`
**Last updated**: 2026-11-24

---

## Executive Summary

This comprehensive 36-page research treatise by Michael DeCross, Reza Haghshenas, and a collaborative team from Quantinuum, Argonne National Laboratory, and Caltech analyzes the computational complexity and classical simulability of random quantum circuits (RQCs) executed on non-planar hardware geometries. While earlier supremacy demonstrations (Google Sycamore, USTC Zuchongzhi) relied on planar 2D nearest-neighbor architectures, next-generation platforms like Quantinuum's trapped-ion QCCD (quantum charge-coupled device) processors feature all-to-all connectivity. The authors establish rigorous tensor-network contraction bounds, cross-entropy benchmarking (XEB) scaling laws, and hardness proofs, demonstrating that arbitrary non-local connectivity fundamentally expands the supremacy frontier, requiring astronomically larger classical tensor-network budgets to simulate.

---

## Key Strategic, Scientific & Engineering Takeaways

- **Graph Geometry and Classical Simulation Complexity**: Proves that the classical simulation cost of random quantum circuits via tensor network contraction scales exponentially with the treewidth of the circuit's interaction graph, making non-planar architectures exponentially harder to simulate than 2D planar grids.
- **Trapped-Ion All-to-All Advantage**: Quantinuum's QCCD architecture allows arbitrary physical qubit transport and all-to-all entangling gates, achieving rapid scrambling and anti-concentration in circuit depths far shallower ($d \sim \log N$) than planar 2D grids ($d \sim \sqrt{N}$).
- **Cross-Entropy Benchmarking (XEB) Scaling**: Formulates advanced linear cross-entropy benchmarking metrics to verify quantum fidelity in non-planar geometries, accounting for non-local noise correlations and spectator qubit dephasing.
- **Supercomputer Benchmark Comparisons**: Evaluates simulation runtimes on world-leading classical supercomputers (Frontier, Aurora, Summit) using state-of-the-art tensor network slicing algorithms, showing classical simulation becomes intractable at modest qubit counts.
- **Implications for Practical Quantum Algorithms**: Shows that non-planar connectivity drastically compresses the circuit depth required to execute quantum chemistry algorithms (VQE) and quantum error correction code syndrome extractions.

---

## Notable Excerpts & Citations

- "The computational hardness of random quantum circuits depends critically on the underlying hardware connectivity graph. Non-planar, high-degree geometries accelerate entanglement generation, pushing classical simulation beyond the reach of the world's largest supercomputers." (source: DeCross et al., 2024, Abstract, p. 1)
- "All-to-all connectivity in trapped-ion architectures enables quantum circuits to achieve anti-concentration in logarithmic depth, establishing an insurmountable barrier for classical tensor-network simulators." (source: DeCross et al., 2024, p. 18)

---

## Thematic Connections & Conceptual Cross-References

- [[zlokapa-boundaries-of-quantum-supremacy-via-random-circuit-sampling]]
- [[arute-quantum-supremacy-using-a-programmable-superconducting-processor]]
- [[boixo-characterizing-quantum-supremacy-in-near-term-devices]]

---

## Related entities in Wiki
- [[michael-decross]]
- [[quantum-information-science-and-computing]]
- [[data-science-and-scientific-computing]]
- [[fault-tolerant-quantum-computing-and-error-correction]]
- [[quantum-foundations-measurement-and-many-worlds]]
