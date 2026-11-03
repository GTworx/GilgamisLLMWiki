# Probabilistic Artificial Intelligence

**Author(s)**: [[andreas-krause]], [[jonas-hubotter]]  
**Genre(s)**: [[artificial-intelligence-and-machine-learning]], [[data-science-and-scientific-computing]], [[game-theory]]  
**Key Themes**: [[probabilistic-inference-and-uncertainty-quantification]], [[rationality-and-decision-making]], [[evolution-of-strategies]]  
**Publication Year**: 2025  
**Source**: BOOKS/AI/2025 Probabilistic AI.pdf & Book Summary probabilistic_ai_analysis.txt (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\AI\)  
**Last updated**: 2026-11-03  

---

## Executive Summary

*Probabilistic Artificial Intelligence* (compiled February 11, 2025 at the Institute for Machine Learning, ETH Zürich, `arXiv:2502.05244v1 [cs.AI]`, 418 pp., paired with the analytical monograph `Book Summary probabilistic_ai_analysis.txt`) by [[andreas-krause]] and [[jonas-hubotter]] is a comprehensive graduate treatise that reframes artificial intelligence around a foundational axiom: **uncertainty is a first-class citizen and the mathematical glue uniting learning (prediction) with sequential decision-making (action)** (source: BOOKS/AI/2025 Probabilistic AI.pdf, pp. 1–4, 7–11; Book Summary probabilistic_ai_analysis.txt, p. 1). Whereas mainstream deep learning textbooks focus narrowly on point-estimate accuracy over static datasets, Krause and Hübotter strictly decompose **aleatoric uncertainty** (irreducible observation noise, such as sensor fog) from **epistemic uncertainty** (reducible model ignorance due to scarce data) so that autonomous systems know *what they do not know* (source: BOOKS/AI/2025 Probabilistic AI.pdf, pp. 7, 44–45).

Organized into two major parts across thirteen chapters and a 100-page Mathematical Background appendix, **Part I (Probabilistic Machine Learning, Chapters 1–7)** builds from Cox/Kolmogorov probability axioms and Bayesian linear regression (weight-space vs. function-space views) through Kalman filtering, Gaussian Processes (kernels, GP-UCB foundations), Variational Inference (Laplace approximation, KL divergence, Evidence Lower Bound / ELBO), Markov Chain Monte Carlo (Metropolis-Hastings, Langevin dynamics / HMC), and Bayesian Deep Learning (calibration, temperature scaling, deep ensembles) (source: BOOKS/AI/2025 Probabilistic AI.pdf, pp. 7–8, 83–156). **Part II (Sequential Decision-Making, Chapters 8–13)** operationalizes epistemic uncertainty to guide data acquisition and safe action: Active Learning via submodular Mutual Information maximization (Ch. 8), Multi-Armed Bandits and Bayesian Optimization via Upper Confidence Bound (UCB) and Thompson Sampling (Ch. 9), Markov Decision Processes (Ch. 10), Tabular and Model-Free Deep RL including Maximum Entropy RL and RLHF / Learning from Preferences (Ch. 11–12), and Model-Based RL with optimistic and safety-constrained exploration (Ch. 13) (source: BOOKS/AI/2025 Probabilistic AI.pdf, pp. 8–9, 161–298).

---

## Key Arguments / Chapter Breakdown

* **Chapter 1 & Part I (Chapters 2–4): Exact Bayesian Inference, Filtering & Gaussian Processes (pp. 1–82, PDF pp. 11–92)**:
  * *Aleatoric vs. Epistemic Uncertainty & Function-Space Priors*: Contrasts Boolean symbolic logic with probabilistic inference; derives the equivalence between weight-space ridge regression and Bayesian MAP estimation, decomposes predictive variance into aleatoric noise ($\sigma_n^2$) and epistemic uncertainty, and develops Kalman Filters (Ch. 3) and non-parametric Gaussian Processes (Ch. 4) (source: BOOKS/AI/2025 Probabilistic AI.pdf, pp. 7, 11–16, 39–70).

* **Part I Continued (Chapters 5–7): Variational Inference, MCMC & Calibrated Bayesian Deep Learning (pp. 83–156, PDF pp. 93–166)**:
  * *Information Theory, ELBO, Gradient Sampling & Calibration*: Formulates Shannon surprise $S[p(x)] = -\log p(x)$, entropy $H[p]$, and KL divergence; derives the Evidence Lower Bound (ELBO) for Variational Inference (Ch. 5, pp. 88–101), gradient-informed MCMC (Langevin dynamics and Hamiltonian Monte Carlo, Ch. 6), and Bayesian neural networks with expected calibration error (ECE) mitigation (Ch. 7) (source: BOOKS/AI/2025 Probabilistic AI.pdf, pp. 8, 83–155).

* **Part II (Chapters 8–9): Active Learning & Bayesian Optimization (pp. 157–196, PDF pp. 167–206)**:
  * *Submodularity of Mutual Information & Optimism in the Face of Uncertainty*: Proves how greedy maximization of mutual information $I(Y_A; f)$ achieves near-optimal active learning guarantees due to diminishing returns (submodularity, Ch. 8), and formulates Bayesian Optimization (GP-UCB, Expected Improvement, Thompson Sampling, and LITE) for sample-efficient black-box scientific discovery such as drug design (Ch. 9, p. 191 / PDF p. 201) (source: BOOKS/AI/2025 Probabilistic AI.pdf, pp. 8, 161–201).

* **Part II Continued (Chapters 10–13): MDPs, Actor-Critics, RLHF & Safe Model-Based Reinforcement Learning (pp. 197–298, PDF pp. 207–308)**:
  * *From Maximum Entropy RL to Constrained Safe Exploration*: Bridges MDPs and POMDPs (Ch. 10) with tabular and deep Actor-Critic RL, Soft Actor-Critic (Maximum Entropy RL), and Learning from Preferences / RLHF (Ch. 11–12), culminating in Model-Based RL where epistemic world-model ensembles drive both optimistic exploration and safety-constrained exploration without simulator resets (Ch. 13, p. 291 / PDF p. 301) (source: BOOKS/AI/2025 Probabilistic AI.pdf, pp. 9, 217–301).

---

## Key Quotes & Citations

* "A key aspect of intelligence is to not only make predictions, but reason about the uncertainty of those predictions, and use this uncertainty to make decisions and gather new information." (source: BOOKS/AI/2025 Probabilistic AI.pdf, Preface, p. iii / PDF p. 3)
* "The entropy of a distribution p is the average surprise about samples from p. In this way, entropy is a notion of uncertainty associated with the distribution p: if the entropy of p is large, we are 'on average very surprised' by samples from p." (source: BOOKS/AI/2025 Probabilistic AI.pdf, ch. 5, p. 91 / PDF p. 101)
* "Besides making exploration more efficient, another use of uncertainty is to make exploration more safe. Today, reinforcement learning is still far away from being deployed directly to the real world. In practice, reinforcement learning is almost always used together with a simulator, in which the agent can 'safely' train and explore. Yet, in many domains, it is not possible to simulate the training process." (source: BOOKS/AI/2025 Probabilistic AI.pdf, ch. 13, p. 291 / PDF p. 301)

---

## Thematic Connections

* **Information Dynamics & Topological Choice**: Krause and Hübotter's information-theoretic treatment of Shannon surprise, KL divergence, and preference learning (Ch. 5, 8, 12.7) connects directly with [[mikhail-prokopenko]], [[ori-livson]], and [[siddharth-pritam]]'s [[the-non-orientable-topology-of-condorcets-paradox]].
* **Evolutionary Game Theory & Exploration-Exploitation**: Unites UCB/Thompson Sampling and RL policy optimization with [[robert-axelrod]]'s iterated strategy tournaments in [[the-evolution-of-cooperation]].
* **Foundational Bridge Across the AI Textbook Corpus**: Extends [[wolfgang-ertel]]'s [[introduction-to-artificial-intelligence]], [[miroslav-kubat]]'s [[an-introduction-to-machine-learning]], and [[sandro-skansi]]'s [[introduction-to-deep-learning-from-logical-calculus-to-artificial-intelligence]] into unified Bayesian sequential decision-making.

---

## Related pages

- [[andreas-krause]]
- [[jonas-hubotter]]
- [[artificial-intelligence-and-machine-learning]]
- [[data-science-and-scientific-computing]]
- [[game-theory]]
- [[probabilistic-inference-and-uncertainty-quantification]]
- [[rationality-and-decision-making]]
- [[evolution-of-strategies]]
- [[mikhail-prokopenko]]
- [[ori-livson]]
- [[siddharth-pritam]]
- [[the-non-orientable-topology-of-condorcets-paradox]]
- [[robert-axelrod]]
- [[the-evolution-of-cooperation]]
- [[wolfgang-ertel]]
- [[introduction-to-artificial-intelligence]]
- [[miroslav-kubat]]
- [[an-introduction-to-machine-learning]]
- [[sandro-skansi]]
- [[introduction-to-deep-learning-from-logical-calculus-to-artificial-intelligence]]
