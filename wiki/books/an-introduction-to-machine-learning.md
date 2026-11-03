# An Introduction to Machine Learning (Second Edition)

**Author(s)**: [[miroslav-kubat]]  
**Genre(s)**: [[artificial-intelligence-and-machine-learning]], [[data-science-and-scientific-computing]], [[educational-technology-and-disruptive-pedagogy]]  
**Key Themes**: [[probabilistic-inference-and-uncertainty-quantification]], [[rationality-and-decision-making]], [[evolution-of-strategies]]  
**Publication Year**: 2017  
**Source**: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\AI\)  
**Last updated**: 2026-11-03  

---

## Executive Summary

*An Introduction to Machine Learning (Second Edition)* (published by Springer International Publishing, 2017, 348 pp., `DOI: 10.1007/978-3-319-63913-0`) by University of Miami Professor [[miroslav-kubat]] is a comprehensive 17-chapter textbook that traces inductive machine learning from its 1983 disciplinary birth (*Machine Learning: An Artificial Intelligence Approach*) to modern ensemble and deep neural architectures (source: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf, pp. 4–11). Emphasizing algorithmic intuition, worked numerical examples, and 'Solidify Your Knowledge' thought experiments over opaque black-box API calls, Kubat equips engineers to understand both *how* classifiers induce decision boundaries and *when* their underlying assumptions break down in noisy, imbalanced real-world domains (source: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf, pp. 6–11, 245–251).

Across seventeen chapters, Kubat develops hill-climbing search in hypothesis space (Chapter 1); Naive Bayes and continuous probability density estimation via Gaussian mixtures (Chapter 2, p. 39 / PDF p. 51); $k$-Nearest Neighbors ($k$-NN) and curse-of-dimensionality distance weighting (Chapter 3); additive (**Perceptron**) vs. multiplicative (**WINNOW**) linear classifiers, polynomial kernels, and **Support Vector Machines (SVMs)** (Chapter 4, pp. 65–88); multilayer neural networks and **Deep Learning** (Chapters 5–6); **Computational Learning Theory** (**PAC Learning** and **Vapnik-Chervonenkis / VC Dimension**, Chapter 7, p. 142 / PDF p. 151); Decision Trees, Rule Induction, and Text Classification (Chapters 8, 10); **Voting Assemblies** (**Bagging**, **Schapire's Boosting**, **AdaBoost**, and **Stacking**, Chapters 9, 13); **Statistical Performance Evaluation** (precision/recall, ROC curves, $t$-tests, cross-validation, and learning from imbalanced classes, Chapter 12, p. 245 / PDF p. 251); Unsupervised Clustering and Reinforcement Learning (Chapters 14–17) (source: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf, pp. 6–9, 51, 151, 251).

---

## Key Arguments / Chapter Breakdown

* **Chapters 1–4: Hypothesis Search, Bayesian Classifiers, $k$-NN & Linear/SVM Boundaries (pp. 1–90, PDF pp. 13–102)**:
  * *Bayes Rule, Perceptron vs. WINNOW & Maximum-Margin Hyperplanes*: Formulates classification as hill-climbing search; shows how Naive Bayes approximates joint likelihoods $p_{c_i}(\mathbf{x}) P(c_i)$ via discretization or Gaussian kernels (Ch. 2, p. 39 / PDF p. 51); and contrasts Rosenblatt's additive Perceptron update with Littlestone's multiplicative WINNOW rule for high-dimensional irrelevant attributes alongside SVMs (Ch. 4) (source: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf, pp. 6–7, 51).

* **Chapters 5–9: Neural Networks, Deep Learning, PAC/VC Learning Theory, Decision Trees & Boosting Ensembles (pp. 91–190, PDF pp. 103–202)**:
  * *PAC Sample Complexity, VC Dimension & AdaBoost*: Derives the size of Boolean hypothesis spaces ($2^{2^n}$), Probably Approximately Correct (PAC) sample complexity bounds, and the Vapnik-Chervonenkis (VC) shattering dimension (Ch. 7, p. 142 / PDF p. 151); builds entropy-based decision trees (Ch. 8); and proves how **Bagging**, **Schapire's recursive trio boosting**, and **AdaBoost** convert weak learners into arbitrarily strong voting assemblies (Ch. 9) (source: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf, pp. 8, 151).

* **Chapters 10–17: Rule Induction, Imbalanced Data Evaluation, Multi-Label Stacking, Clustering & RL (pp. 191–336, PDF pp. 203–348)**:
  * *Experimental Rigor & Class Imbalance*: Codifies stratified $k$-fold cross-validation, paired statistical significance testing, ROC/AUC analysis, and majority-class undersampling / minority-class oversampling when evaluating classifiers on skewed medical or fraud datasets (Ch. 12–13, p. 245 / PDF p. 251) (source: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf, pp. 9, 251).

---

## Key Quotes & Citations

* "The bombshell exploded in 1983. Machine Learning: The AI Approach was a thick volume of research papers which proposed the most diverse ways of addressing the great mystery. Under their influence, a new scientific discipline was born—virtually overnight." (source: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf, Introduction, p. xii / PDF p. 11)
* "The estimates of probabilities are far from perfect, but the results are often satisfactory even when rigorous theoretical assumptions are not fulfilled." (source: BOOKS/AI/2017_Book_AnIntroductionToMachineLearnin.pdf, ch. 2, p. 39 / PDF p. 51)

---

## Thematic Connections

* **Ensemble Wisdom & Topological Social Choice**: Kubat's Chapters 9 and 13 on voting assemblies (Bagging, Boosting, Stacking) connect directly with preference aggregation and majority cycles in [[ori-livson]], [[siddharth-pritam]], and [[mikhail-prokopenko]]'s [[the-non-orientable-topology-of-condorcets-paradox]].
* **Quantitative Evaluation Across Criminology, Entertainment & Medicine**: Complements the experimental evaluation methodologies in [[alex-r-piquero]] & [[david-weisburd]]'s [[handbook-of-quantitative-criminology]], [[thorsten-hennig-thurau]] & [[mark-b-houston]]'s [[entertainment-science-data-analytics-and-practical-theory]], and [[ton-j-cleophas]] & [[aeilko-h-zwinderman]]'s [[machine-learning-in-medicine-a-complete-overview]].

---

## Related pages

- [[miroslav-kubat]]
- [[artificial-intelligence-and-machine-learning]]
- [[data-science-and-scientific-computing]]
- [[educational-technology-and-disruptive-pedagogy]]
- [[probabilistic-inference-and-uncertainty-quantification]]
- [[rationality-and-decision-making]]
- [[evolution-of-strategies]]
- [[ori-livson]]
- [[siddharth-pritam]]
- [[mikhail-prokopenko]]
- [[the-non-orientable-topology-of-condorcets-paradox]]
- [[alex-r-piquero]]
- [[david-weisburd]]
- [[handbook-of-quantitative-criminology]]
- [[thorsten-hennig-thurau]]
- [[mark-b-houston]]
- [[entertainment-science-data-analytics-and-practical-theory]]
- [[ton-j-cleophas]]
- [[aeilko-h-zwinderman]]
- [[machine-learning-in-medicine-a-complete-overview]]
