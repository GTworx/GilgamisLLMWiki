# AI Watermarking, Neural Steganography, and Synthetic Text Detection: Cryptographic Distortion-Free Watermarks and Impossibility Limits

## Metadata
- **Index**: Work 1505
- **Author(s)**: [[rohith-kuditipudi]], [[tatsunori-hashimoto]]
- **Genre(s)**: [[cybersecurity-and-digital-forensics]], [[artificial-intelligence-and-machine-learning]], [[pure-and-applied-mathematics]]
- **Key Themes**: [[rule-of-law-and-experimental-justice]], [[artificial-intelligence-scaling-compute-and-governance]]

## Summary
Technical and cryptographic compendium examining the forensic verification of AI-generated content. Compiles Kuditipudi and Hashimoto's foundational papers on 'Robust Distortion-Free Watermarks for Language Models', neural linguistic steganography, Ghosal et al.'s survey on the fundamental theoretical possibilities and impossibility limits of AI text detection, and prompt-specific poisoning attacks.

## Analytical Overview
This volume addresses the critical information integrity challenge of the generative AI era: cryptographically proving whether text or images originated from a machine or a human.

Key cryptographic and forensic methods:
1. **Distortion-Free Pseudorandom Watermarking**: Features Kuditipudi et al.’s breakthrough algorithm, which embeds cryptographic watermarks into language model sampling without altering the model's output probability distribution (distortion-free), preserving linguistic perplexity while allowing detectors to verify origin from short text spans.
2. **Theoretical Limits of Post-Hoc Text Detection**: Compiles comprehensive surveys proving that statistical post-hoc classifiers (zero-shot perplexity or neural detectors) suffer from unavoidable trade-offs: as models approach human-level fluency, the total variation distance between human and machine text approaches zero, rendering un-watermarked detection mathematically impossible without high false-positive rates.
3. **Neural Steganography & Poisoning**: Analyzes methods for hiding covert messages within generated text distributions and defenses against prompt-specific adversarial poisoning attacks on text-to-image diffusion models.

## Primary Sources
- [2025 POISONING ATTACKS ON LLMS REQUIRE A NEAR-CONSTANT NUMBER OF POISON SAMPLES.pdf](file:///C:/Users/gokha/iCloudDrive/Documents/_GilgameshLibrary/ARTICLES-REPORTS/AI/AI - Alignment_/2025 POISONING ATTACKS ON LLMS REQUIRE A NEAR-CONSTANT NUMBER OF POISON SAMPLES.pdf) — (30p, 1648KB)
- [2019 Ziegler Neural Linguistic Steganography.pdf](file:///C:/Users/gokha/iCloudDrive/Documents/_GilgameshLibrary/ARTICLES-REPORTS/AI/AI - Watermarking/2019 Ziegler Neural Linguistic Steganography.pdf) — (9p, 364KB)
- [2023 Ghosal et al Towards Possibilities & Impossibilities of AI-generated Text Detection- A Survey.pdf](file:///C:/Users/gokha/iCloudDrive/Documents/_GilgameshLibrary/ARTICLES-REPORTS/AI/AI - Watermarking/2023 Ghosal et al Towards Possibilities & Impossibilities of AI-generated Text Detection- A Survey.pdf) — (30p, 4492KB)
- [2023 Kuditipudi et al Robust Distortion-free Watermarks for Language Models.pdf](file:///C:/Users/gokha/iCloudDrive/Documents/_GilgameshLibrary/ARTICLES-REPORTS/AI/AI - Watermarking/2023 Kuditipudi et al Robust Distortion-free Watermarks for Language Models.pdf) — (57p, 3291KB)
- [2023 Prompt-Specific Poisoning Attacks on Text-to-Image Generative Models.pdf](file:///C:/Users/gokha/iCloudDrive/Documents/_GilgameshLibrary/ARTICLES-REPORTS/AI/AI - Watermarking/2023 Prompt-Specific Poisoning Attacks on Text-to-Image Generative Models.pdf) — (19p, 15466KB)
- [2023 Zhang et al Watermarks in the Sand- Impossibility of Strong Watermarking for Generative Models.pdf](file:///C:/Users/gokha/iCloudDrive/Documents/_GilgameshLibrary/ARTICLES-REPORTS/AI/AI - Watermarking/2023 Zhang et al Watermarks in the Sand- Impossibility of Strong Watermarking for Generative Models.pdf) — (38p, 3703KB)
- [2024 Hidden in the Noise- Two-Stage Robust Watermarking for Images.pdf](file:///C:/Users/gokha/iCloudDrive/Documents/_GilgameshLibrary/ARTICLES-REPORTS/AI/AI - Watermarking/2024 Hidden in the Noise- Two-Stage Robust Watermarking for Images.pdf) — (36p, 42610KB)
