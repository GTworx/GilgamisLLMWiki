# Machine Learning in Medicine — A Complete Overview

**Author(s)**: [[ton-j-cleophas]], [[aeilko-h-zwinderman]]  
**Genre(s)**: [[artificial-intelligence-and-machine-learning]], [[data-science-and-scientific-computing]], [[evolutionary-biology]]  
**Key Themes**: [[probabilistic-inference-and-uncertainty-quantification]], [[rationality-and-decision-making]], [[human-centered-ai-and-augmented-leadership]]  
**Publication Year**: 2015  
**Source**: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\AI\)  
**Last updated**: 2026-11-03  

---

## Executive Summary

*Machine Learning in Medicine — A Complete Overview* (published by Springer International Publishing, 2015, 498 pp., `DOI: 10.1007/978-3-319-15195-3`, with assistance from Henny I. Cleophas-Allers) by clinical pharmacologist [[ton-j-cleophas]] and University of Amsterdam biostatistician [[aeilko-h-zwinderman]] is an encyclopedic **80-chapter clinical handbook** uniting the authors' three earlier *Machine Learning in Medicine* volumes plus 20 new methodologies into a single unified reference (source: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf, pp. 1–8). Noting Usama Fayyad's observation that global database volume doubles every 20 months, Cleophas and Zwinderman address a critical bottleneck in modern healthcare: clinicians trained only in classical frequentist hypothesis testing ($p$-values on small cohorts) are overwhelmed by high-dimensional genomic, proteomic, and electronic health record (EHR) datasets containing non-linear interactions, multiple outcomes, and extreme outliers (source: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf, pp. 6–8).

Structured across **80 self-contained chapters** grouped into three overarching parts—**Part I: Cluster and Classification Models (Chapters 1–18)**, **Part II: (Log)Linear Models (Chapters 19–49)**, and **Part III: Rules and Ensemble Models (Chapters 50–80)**—each chapter opens with a concrete clinical purpose and scientific question (ranging from $N=12$ pilot studies to $N=1,445$ family cohorts and $N=10,000+$ hospital registries), walks through step-by-step execution in SPSS / SPSS Modeler (including XML Scoring Wizards and visual node streams), and demonstrates how to integrate epidemiologic **propensity scores** and interaction terms into machine learning models to control confounding (source: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf, pp. 7–11, 29 / PDF p. 51, 193 / PDF p. 201, 411 / PDF p. 401).

---

## Key Arguments / Chapter Breakdown

* **Part I (Chapters 1–18): Cluster and Classification Models in Clinical Cohorts (pp. 1–116, PDF pp. 10–125)**:
  * *Hierarchical/K-Means Clustering, Density Binning & Nearest Neighbors*: Applies hierarchical, k-means, and two-step clustering to stratify patient subgroups, multidimensional scaling, optimal high-risk bin discretization (e.g., predicting overweight risk across 1,445 families, Ch. 5, pp. 25–29 / PDF p. 51), and k-nearest neighbors for clinical classification (source: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf, pp. 7, 10–11, 51).

* **Part II (Chapters 19–49): Generalized (Log)Linear, Survival & Mixed Models (pp. 117–308, PDF pp. 126–317)**:
  * *Automated Linear Modeling, XML Scoring Wizards, Ridge/Lasso & Cox Time-to-Event*: Covers automatic linear regression with XML model export and Scoring Wizard deployment on novel patient records (Ch. 31, p. 193 / PDF p. 201), generalized linear mixed models, Poisson/negative-binomial count models, quantile regression, and regularized elastic-net survival models (source: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf, pp. 7, 201).

* **Part III (Chapters 50–80): Rules Models, Neural Networks, Markov Chains, SVMs & Ensembled Node Streams (pp. 309–488, PDF pp. 318–497)**:
  * *Clinical Decision Trees, Bayesian Networks, Markov Transitions & Ensembled Streams*: Develops CHAID/CART decision trees, association rules (apriori), multilayer perceptrons, radial basis functions, stochastic Markov chains for longitudinal disease progression, Support Vector Machines, and visual SPSS Modeler ensembled binary/continuous node streams (p. 411 / PDF p. 401) (source: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf, pp. 7–8, 401).

---

## Key Quotes & Citations

* "The amount of data stored in the world's databases doubles every 20 months, as estimated by Usama Fayyad... and clinicians, familiar with traditional statistical methods, are at a loss to analyze them. Traditional methods have, indeed, difficulty to identify outliers in large datasets, and to find patterns in big data and data with multiple exposure/outcome variables." (source: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf, Preface, p. v / PDF p. 6)
* "Machine learning may have little options for adjusting confounding and interaction, but you can add propensity scores and interaction variables to almost any machine learning method." (source: BOOKS/AI/2015_Book_MachineLearningInMedicine-ACom.pdf, Preface, p. vii / PDF p. 8)

---

## Thematic Connections

* **Active Learning & Bayesian Optimization in Medicine**: Directly complements [[andreas-krause]] and [[jonas-hubotter]]'s medical diagnosis active learning and drug-discovery Bayesian optimization in [[probabilistic-artificial-intelligence]] and [[mustafa-suleyman]]'s AlphaFold/CRISPR synthesis in [[the-coming-wave-ai-power-and-our-future]].
* **Neuroscience & Biomedical Telemetry**: Connects clinical biostatistics with [[sandra-ackerman]]'s [[discovering-the-brain]] and [[william-g-braun-iii]] et al.'s physiological telemetry in [[developing-the-super-soldier-enhancing-military-performance]].

---

## Related pages

- [[ton-j-cleophas]]
- [[aeilko-h-zwinderman]]
- [[artificial-intelligence-and-machine-learning]]
- [[data-science-and-scientific-computing]]
- [[evolutionary-biology]]
- [[probabilistic-inference-and-uncertainty-quantification]]
- [[rationality-and-decision-making]]
- [[human-centered-ai-and-augmented-leadership]]
- [[andreas-krause]]
- [[jonas-hubotter]]
- [[probabilistic-artificial-intelligence]]
- [[mustafa-suleyman]]
- [[the-coming-wave-ai-power-and-our-future]]
- [[sandra-ackerman]]
- [[discovering-the-brain]]
- [[william-g-braun-iii]]
- [[developing-the-super-soldier-enhancing-military-performance]]
