# Introduction to Deep Learning: From Logical Calculus to Artificial Intelligence

**Author(s)**: [[sandro-skansi]]  
**Genre(s)**: [[artificial-intelligence-and-machine-learning]], [[neuroscience-and-philosophy-of-mind]], [[data-science-and-scientific-computing]]  
**Key Themes**: [[neurobiology-of-consciousness-and-non-algorithmic-mind]], [[probabilistic-inference-and-uncertainty-quantification]], [[rationality-and-decision-making]]  
**Publication Year**: 2018  
**Source**: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\AI\)  
**Last updated**: 2026-11-03  

---

## Executive Summary

*Introduction to Deep Learning: From Logical Calculus to Artificial Intelligence* (published by Springer International Publishing in the *Undergraduate Topics in Computer Science* series, 2018, 196 pp., `DOI: 10.1007/978-3-319-73004-2`) by University of Zagreb logician and data scientist [[sandro-skansi]] is a foundational textbook that frames artificial intelligence as **'philosophical engineering'**—the discipline of translating philosophical, logical, psychological, and linguistic concepts into executable mathematical algorithms (source: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf, pp. 1–8). Drawing an analogy to the four Kendo martial-arts mastery stages (*Big, Strong, Fast, Light*, p. 7), Skansi builds deep learning intuition from first principles before introducing high-level Keras abstractions (source: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf, pp. 7–11).

Structured across ten chapters, the book traces the genealogy of neural computation from Warren McCulloch and Walter Pitts's 1943 *A Logical Calculus of the Ideas Immanent in Nervous Activity*, Frank Rosenblatt's Perceptron, and Marvin Minsky & Seymour Papert's 1969 **XOR linear-inseparability problem** to Geoffrey Hinton's backpropagation and cognitive connectionism (Chapter 1, pp. 1–15); establishes the calculus, linear algebra, and Gaussian probability prerequisites (Chapter 2, pp. 17–51); derives shallow networks, the Delta Rule from Sum of Squared Errors (SSE), gradient descent, softmax, and regularization (Chapters 3–5, pp. 52–120); and systematically develops **Convolutional Neural Networks (CNNs)** for computer vision (Chapter 6), **Recurrent Neural Networks (RNNs)**, **Long Short-Term Memory (LSTM)** gates, and GRUs for sequential language modeling (Chapter 7, pp. 142–151), **Autoencoders**, word embeddings (**Word2Vec**), and **Boltzmann Machines / Deep Belief Networks** (Chapters 8–10) (source: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf, pp. 11–18, 51, 101, 151).

---

## Key Arguments / Chapter Breakdown

* **Chapters 1–2: From Logic to Cognitive Science & Mathematical Prerequisites (pp. 1–50, PDF pp. 11–60)**:
  * *McCulloch-Pitts Logical Neurons, The XOR Bottleneck & Gaussian Initialization*: Demonstrates how McCulloch-Pitts binary threshold neurons implement propositional logic gates (AND, OR, NOT) and why single-layer perceptrons fail on the non-linearly separable XOR truth table (Ch. 1, pp. 1–8), followed by multivariable gradient calculus, matrix algebra, and Gaussian weight initialization (Ch. 2, p. 38 / PDF p. 51) (source: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf, pp. 11, 51).

* **Chapters 3–5: Machine Learning Foundations, Feedforward Networks & Deep Modifications (pp. 51–106, PDF pp. 61–116)**:
  * *Deriving the Delta Rule, Backpropagation & Overfitting Defense*: Derives the partial derivative $\partial E / \partial w_i$ of the Mean Squared Error (MSE) to link the Delta Rule with full multilayer backpropagation (Ch. 4, p. 90 / PDF p. 101), and introduces ReLU activations, Dropout, L1/L2 regularization, and Momentum/Adam optimizers (Ch. 5) (source: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf, p. 101).

* **Chapters 6–10: CNNs, RNNs/LSTMs, Autoencoders, NLP Embeddings & Deep Belief Networks (pp. 107–186, PDF pp. 117–196)**:
  * *Spatial Convolutions, Temporal Memory Gates & Distributed Representations*: Explains convolutional kernels and pooling in CNNs (Ch. 6), vanishing/exploding gradients and forget/input/output gate equations in LSTMs (Ch. 7, p. 142 / PDF p. 151), dimensionality reduction via Autoencoders (Ch. 8), distributional semantics in Word2Vec (Ch. 9), and energy-based Restricted Boltzmann Machines (Ch. 10) (source: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf, p. 151).

---

## Key Quotes & Citations

* "Artificial intelligence as a discipline can be considered to be a sort of 'philosophical engineering'. What I mean by this is that AI is a process of taking philosophical ideas and making algorithms that implement them." (source: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf, Preface, p. viii / PDF p. 8)
* "There is an old idea from Kendo which seems to find its way to the new world of cutting-edge technology. The idea is that you learn a martial art in four stages: big, strong, fast, light." (source: BOOKS/AI/2018_Book_IntroductionToDeepLearning.pdf, Preface, p. vii / PDF p. 7)

---

## Thematic Connections

* **Bridging Symbolic Logic and Connectionism**: Connects directly with [[wolfgang-ertel]]'s first-order predicate logic and neural networks in [[introduction-to-artificial-intelligence]] and [[roger-penrose]]'s Turing/Gödel analysis in [[the-emperors-new-mind-concerning-computers-minds-and-the-laws-of-physics]].
* **From Deterministic Backprop to Bayesian Deep Learning**: Provides the feedforward, CNN, and LSTM architectural foundation extended into calibrated Bayesian neural networks by [[andreas-krause]] and [[jonas-hubotter]] in [[probabilistic-artificial-intelligence]] (Ch. 7).

---

## Related pages

- [[sandro-skansi]]
- [[artificial-intelligence-and-machine-learning]]
- [[neuroscience-and-philosophy-of-mind]]
- [[data-science-and-scientific-computing]]
- [[neurobiology-of-consciousness-and-non-algorithmic-mind]]
- [[probabilistic-inference-and-uncertainty-quantification]]
- [[rationality-and-decision-making]]
- [[wolfgang-ertel]]
- [[introduction-to-artificial-intelligence]]
- [[roger-penrose]]
- [[the-emperors-new-mind-concerning-computers-minds-and-the-laws-of-physics]]
- [[andreas-krause]]
- [[jonas-hubotter]]
- [[probabilistic-artificial-intelligence]]
