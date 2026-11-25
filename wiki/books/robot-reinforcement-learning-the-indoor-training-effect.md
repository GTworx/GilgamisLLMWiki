# The Indoor-Training Effect in Robot Reinforcement Learning: Distribution Shifts in Transition Functions

**Author(s)**: [[robot-learning-research-group]]  
**Publication Year**: 2025  
**Primary Genre**: [[robotics-autonomous-systems-and-spatial-computing]], [[data-science-and-scientific-computing]]  
**Core Themes**: [[robotics-humanoid-automation-and-physical-embodiment]], [[artificial-intelligence-scaling-compute-and-governance]]  
**Physical Source Files**: 1 file(s)  

---

## Executive Summary
This 18-page technical robotics paper published in 2025 investigates a counter-intuitive phenomenon in robot reinforcement learning (RL): the 'Indoor-Training Effect'. When autonomous mobile robots and quadrupeds trained exclusively in structured indoor environments are deployed into complex outdoor unstructured terrains, they frequently outperform policies trained on broad randomized outdoor data. The authors analyze the underlying distribution shifts in transition functions and Markov Decision Processes (MDPs), proving that constrained indoor environments force RL policies to learn tightly bounded, robust low-level stability priors that generalize superiorly to external perturbations.

---

## Core Thematic Insights & Structural Framework

- **Sim-to-Real Transition Function Shifts**: Identifies mathematical conditions under which constrained, low-noise training distributions prevent policy over-fitting to noise artifacts.
- **Locomotion Stability Priors**: Constrained training induces conservative torque boundaries and high-frequency reflex loops that maintain balance on unexpected outdoor slopes and mud.
- **Domain Randomization Limitations**: Excessive simulation domain randomization can dilute learning signals, whereas structured curriculum learning yields faster convergence.
- **Practical Deployment Guidelines**: Provides actionable training recipes for industrial quadruped robots and autonomous warehouse AGVs transitioning to outdoor loading docks.

---

## Key Data Points & Excerpts

> "Paradoxically, training robots within the rigid confines of indoor hallways produces more robust locomotive reflexes than exposing them to noisy outdoor terrain from the start."

> "A well-conditioned transition function learned in structured spaces provides the optimal foundation for zero-shot generalization across chaotic physical environments."

---

## Physical File Manifest & Verification
The following verified physical files from `_GilgameshLibrary/` constitute this canonical entry:
- `_GilgameshLibrary/ARTICLES-REPORTS/Robotics/2025 The Indoor-Training Effect - unexpected gains from distribution shifts in the transition function.pdf`

---

## Conceptual Connections & Cross-References

### Thematic Synergies
- [[robotics-humanoid-automation-and-physical-embodiment]]
- [[artificial-intelligence-scaling-compute-and-governance]]

### Genre Context
- [[robotics-autonomous-systems-and-spatial-computing]]
- [[data-science-and-scientific-computing]]

### Related Canonical Works & Cross-References
- [[anthropic-what-work-can-robots-do-automation-economics]]
- [[morgan-stanley-robot-almanac-vol-3-humanoids-and-automation]]
- [[snake-robot-kinematics-and-hyper-redundant-locomotion]]

---
*Cataloged in Gilgamesh LLM Wiki on 2026-11-25 (Option AR-8A Ingestion).*
