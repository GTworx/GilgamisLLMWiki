# Is Quantum Advantage the Right Goal for Quantum Machine Learning?

**Author(s)**: [[maria-schuld]]
**Publication Year**: 2022
**Genre(s)**: [[quantum-information-science-and-computing]], [[data-science-and-scientific-computing]]
**Key Themes**: [[fault-tolerant-quantum-computing-and-error-correction]], [[quantum-foundations-measurement-and-many-worlds]]
**Source**: `ARTICLES-REPORTS/QuantumCompute/Is Quantum Advantage the Right Goal for Quantum Machine Learning PRXQuantum 2022.pdf (14 pp., Maria Schuld and Nathan Killoran, PRX Quantum 2022)`
**Last updated**: 2026-11-24

---

## Executive Summary

This influential 14-page perspective paper published in PRX Quantum (2022) by Maria Schuld and Nathan Killoran delivers a profound critical re-examination of the foundational goals of Quantum Machine Learning (QML). The authors challenge the community's singular fixation on chasing theoretical 'quantum advantage' (proving exponential speedups on classical benchmark datasets), arguing that this pursuit has led to artificial benchmarks that obscure practical utility. Schuld and Killoran establish that parameterized quantum circuits function mathematically as kernel methods in exponentially large Hilbert spaces. They propose reframing QML around learning theory, inductive biases, and generalization power on physical quantum data rather than contrived classical dataset speedups.

---

## Key Strategic, Scientific & Engineering Takeaways

- **Deconstructing the Quantum Advantage Obsession**: Argues that hunting for exponential speedups on classical tabular or image datasets (e.g., MNIST) is fundamentally misguided due to data loading bottlenecks ('input problem') and classical neural network superiority.
- **Equivalence Between Quantum Models and Kernel Methods**: Proves mathematically that variational quantum circuits (parameterized quantum neural networks) are equivalent to linear models operating in a quantum-defined feature space, bridging QML with classical support vector machines and kernel theory.
- **Inductive Bias as the Core Metric**: Emphasizes that machine learning success is governed by inductive bias—the assumptions a model makes about the data distribution. Researchers must ask what structural data properties naturally align with quantum Hilbert spaces.
- **Quantum Data as the True Frontier**: Concludes that QML's greatest potential lies not in processing classical data, but in processing native quantum data emitted directly from quantum sensors, quantum networks, and quantum chemical simulators.
- **Methodological Rigor and Honest Benchmarks**: Calls for rigorous statistical standards in QML research, demanding robust comparisons against tuned classical kernel baselines and de-quantized linear algebra algorithms.

---

## Notable Excerpts & Citations

- "Searching for a quantum speedup on classical data has often led the field into a trap of contriving artificial datasets. We argue that quantum machine learning must be understood through the lens of learning theory, inductive bias, and quantum data." (source: Schuld & Killoran, PRX Quantum 2022, Abstract, p. 1)
- "Quantum models are kernel methods in disguise. Understanding the geometry of the quantum state space and the inductive bias it imparts is far more critical than claiming illusory asymptotic speedups." (source: Schuld & Killoran, PRX Quantum 2022, p. 8)

---

## Thematic Connections & Conceptual Cross-References

- [[gircha-hybrid-quantum-classical-machine-learning-for-generative-chemistry]]
- [[nature-quantum-computing-milestone-package]]
- [[morgan-stanley-quantum-computing-how-will-it-impact-ai]]

---

## Related entities in Wiki
- [[maria-schuld]]
- [[quantum-information-science-and-computing]]
- [[data-science-and-scientific-computing]]
- [[fault-tolerant-quantum-computing-and-error-correction]]
- [[quantum-foundations-measurement-and-many-worlds]]
