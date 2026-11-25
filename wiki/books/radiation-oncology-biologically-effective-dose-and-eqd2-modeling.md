# Radiation Oncology Dosimetry: Biologically Effective Dose (BED) and Equivalent Dose in 2 Gy Fractions (EQD2) Linear-Quadratic Modeling

**Author(s)**: [[radiation-oncology-physics-consortium]]  
**Publication Year**: 2024  
**Primary Genre**: [[clinical-medicine-and-cardiology]], [[data-science-and-scientific-computing]]  
**Core Themes**: [[translational-medicine-and-clinical-diagnostics]], [[general-purpose-technologies-and-learning-by-doing]]  
**Physical Source Files**: 1 file(s)  

---

## Executive Summary
This mathematical physics and clinical radiobiology reference sheet outlines the quantitative formulas and computational models governing fractionation and radiation dosimetry in clinical radiation oncology.

The monograph details the linear-quadratic (LQ) model of radiation-induced cell killing, formulating the mathematical equations for Biologically Effective Dose ($BED = D \times [1 + d / (\alpha/\beta)]$) and Equivalent Dose in 2 Gy fractions ($EQD2 = D \times [(d + \alpha/\beta) / (2 + \alpha/\beta)]$). It details the selection of tissue-specific $\alpha/\beta$ ratios (e.g., $\alpha/\beta = 10\text{ Gy}$ for acute-responding tissues and early-stage tumors versus $\alpha/\beta = 2\text{--}3\text{ Gy}$ for late-responding normal tissues, spinal cord, and prostate cancer), allowing clinical medical physicists to safely calculate hypofractionated stereotactic body radiation therapy (SBRT) protocols and adapt re-irradiation doses without exceeding normal tissue tolerance.

---

## Core Thematic Insights & Structural Framework

- **Linear-Quadratic (LQ) Radiobiology**: Outlines the mechanistic derivation of the LQ model, where $\alpha$ represents single-hit lethal DNA double-strand breaks and $\beta$ represents multi-hit accumulated sub-lethal damage.
- **Tissue-Specific $\alpha/\beta$ Ratios**: Explains why hypofractionation (large dose per fraction) is uniquely advantageous for malignancies with low $\alpha/\beta$ ratios (prostate cancer and melanoma) while sparing late-responding normal organs.
- **Clinical Utility of EQD2**: Explains how EQD2 provides an indispensable common currency allowing clinicians to compare radically different fractionation schemes (e.g., conventional 35 fractions of 2 Gy vs. 5 fractions of 8 Gy SBRT).
- **Re-Irradiation Safety and Cumulative Organ-at-Risk (OAR) Constraints**: Provides computational guidelines for assessing spinal cord myelopathy risk and rectal toxicity when re-treating recurrent cancers.

---

## Key Data Points & Excerpts

> "In radiation oncology, total physical dose in Gray is meaningless without knowing the fraction size: the linear-quadratic model and EQD2 are the essential mathematical compass that protects normal tissues from catastrophic radiation necrosis."

> "The biologically effective dose bridges the physics of linear accelerators with the radiobiology of tumor eradication, enabling the safe delivery of curative ablative radiotherapy."

---

## Physical File Manifest & Verification
The following verified physical files from `_GilgameshLibrary/` constitute this canonical entry:
- `_GilgameshLibrary/ARTICLES-REPORTS/Healthcare/Radiation_Oncology dose BED_EQD2.pdf`

---

## Conceptual Connections & Cross-References

### Thematic Synergies
- [[translational-medicine-and-clinical-diagnostics]]
- [[general-purpose-technologies-and-learning-by-doing]]

### Genre Context
- [[clinical-medicine-and-cardiology]]
- [[data-science-and-scientific-computing]]

### Related Canonical Works & Cross-References
- [[bray-globocan-global-cancer-statistics-estimates]]
- [[translational-medicine-and-clinical-diagnostics]]
- [[lung-cancer-and-interstitial-lung-disease-comorbidities]]

---
*Cataloged in Gilgamesh LLM Wiki on 2026-11-25 (Option AR-7A Ingestion).*
