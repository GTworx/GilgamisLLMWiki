# Introduction to Artificial Intelligence (Second Edition)

**Author(s)**: [[wolfgang-ertel]]  
**Genre(s)**: [[artificial-intelligence-and-machine-learning]], [[data-science-and-scientific-computing]], [[neuroscience-and-philosophy-of-mind]]  
**Key Themes**: [[probabilistic-inference-and-uncertainty-quantification]], [[rationality-and-decision-making]], [[human-centered-ai-and-augmented-leadership]]  
**Publication Year**: 2017  
**Source**: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\AI\)  
**Last updated**: 2026-11-03  

---

## Executive Summary

*Introduction to Artificial Intelligence (Second Edition)* (published by Springer International Publishing in the *Undergraduate Topics in Computer Science* series, 2017, 365 pp., `DOI: 10.1007/978-3-319-58487-4`, translated by Nathanael Black) by Ravensburg-Weingarten Professor [[wolfgang-ertel]] is a classic, mathematically self-contained university textbook designed as a concise, rigorous alternative to Russell and Norvig's 1,152-page encyclopedia (source: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf, pp. 4–9). Updated in its Second Edition with 30 new pages on Deep Learning and AlphaGo's victory in Go, the text bridges the historic divide between **symbolic logic-based AI** and **statistical/connectionist machine learning** (source: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf, pp. 6, 10–11).

Structured across ten chapters, Ertel defines AI through the Turing Test, brain science, and rational agent taxonomies (Chapter 1); develops **Propositional Logic**, SAT solvers, binary decision diagrams (BDDs), **First-Order Predicate Logic (FOPL)**, resolution proof calculi, automated theorem provers, and Prolog logic programming (Chapters 2–5, pp. 19–106, PDF p. 51); formalizes uninformed and heuristic search ($A^*$, minimax, alpha-beta pruning, Chapter 6); resolves the crisis of brittle logical rules via **Reasoning Under Uncertainty**—comparing Bayesian networks, Dempster-Shafer theory, and Jaynes's **Maximum Entropy (MaxEnt)** principle implemented in the clinical appendicitis diagnostic system **LEXMED** (Chapter 7, pp. 139–186, PDF p. 151); and synthesizes **Machine Learning**, **Neural Networks / Deep Learning**, and **Reinforcement Learning** for autonomous robots (Chapters 8–10, PDF p. 251) (source: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf, pp. 9–11, 51, 151, 251).

---

## Key Arguments / Chapter Breakdown

* **Chapters 1–5: Foundations, Propositional & First-Order Predicate Logic, Limitations & Prolog (pp. 1–106, PDF pp. 12–117)**:
  * *Resolution Calculus & Automated Theorem Proving*: Formalizes syntax, semantics, conjunctive normal form (CNF), Skolemization, Robinson's resolution rule, and equality unification in First-Order Predicate Logic (Ch. 2–3), proves Gödel's incompleteness and undecidability boundaries (Ch. 4), and implements declarative knowledge bases in Prolog (Ch. 5) (source: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf, pp. 10–11, 51).

* **Chapters 6–7: Search, Games & Reasoning Under Uncertainty via Maximum Entropy and Bayes (pp. 107–186, PDF pp. 118–197)**:
  * *Heuristic $A^*$, Minimax & The LEXMED Maximum-Entropy Expert System*: Analyzes admissible heuristics in $A^*$ route planning and game-tree search (Ch. 6), then demonstrates in Ch. 7 how incomplete probabilistic constraints ($p_3 + p_4 = 1 - a$) are uniquely and unbiasedly solved by maximizing Shannon entropy $H(p) = -\sum p_i \ln p_i$ (Pitman-Shore-Johnson theorem) alongside Bayesian belief networks (source: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf, p. 151).

* **Chapters 8–10: Machine Learning, Deep Neural Networks & Reinforcement Learning (pp. 187–320, PDF pp. 198–331)**:
  * *Decision Trees, Clustering, Deep CNNs, AlphaGo & Robot RL*: Covers ID3/C4.5 information-gain decision trees, k-means clustering, support vector machines, backpropagation, deep convolutional architectures, and Q-learning / policy iteration in physical robotics (source: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf, pp. 6, 9, 251).

---

## Key Quotes & Citations

* "Artificial Intelligence (AI) has the definite goal of understanding intelligence and building intelligent systems. However, the methods and formalisms used on the way to this goal are not firmly set, which has resulted in AI consisting of a multitude of subdisciplines today." (source: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf, Preface, p. vii / PDF p. 8)
* "To come to a definite solution despite this missing knowledge, we change our point of view. We use the given equation as a constraint for the solution of an optimization problem. We are looking for a distribution p which maximizes the entropy." (source: BOOKS/AI/2017_Book_IntroductionToArtificialIntell.pdf, ch. 7, p. 140 / PDF p. 151)

---

## Thematic Connections

* **Maximum Entropy & Probabilistic AI**: Ertel's Chapter 7 on Maximum Entropy inference and Chapter 10 on Reinforcement Learning directly bridge into [[andreas-krause]] and [[jonas-hubotter]]'s [[probabilistic-artificial-intelligence]] (Ch. 5 & Ch. 12.6 on Maximum Entropy RL).
* **Formal Logic & Deontic Jurisprudence**: Connects automated resolution theorem proving with [[jaap-hage]]'s formal legal logic in [[introduction-to-law]] and [[roger-penrose]]'s Gödelian analysis in [[the-emperors-new-mind-concerning-computers-minds-and-the-laws-of-physics]].

---

## Related pages

- [[wolfgang-ertel]]
- [[artificial-intelligence-and-machine-learning]]
- [[data-science-and-scientific-computing]]
- [[neuroscience-and-philosophy-of-mind]]
- [[probabilistic-inference-and-uncertainty-quantification]]
- [[rationality-and-decision-making]]
- [[human-centered-ai-and-augmented-leadership]]
- [[andreas-krause]]
- [[jonas-hubotter]]
- [[probabilistic-artificial-intelligence]]
- [[jaap-hage]]
- [[introduction-to-law]]
- [[roger-penrose]]
- [[the-emperors-new-mind-concerning-computers-minds-and-the-laws-of-physics]]
