# Practical Fraud Prevention: Fraud and AML Analytics for Fintech and eCommerce, Using SQL and Python

**Author(s)**: [[gilit-saporta]], [[shoshana-maraney]]  
**Genre(s)**: [[cybersecurity-and-digital-forensics]], [[data-science-and-scientific-computing]], [[cloud-computing-and-distributed-systems]]  
**Key Themes**: [[cloud-scale-fraud-analytics-and-security-data-lakes]], [[hybrid-threats-and-cyber-warfare]], [[rationality-and-decision-making]]  
**Publication Year**: 2022  
**Source**: BOOKS/Cloud/3683-practical-fraud-prevention.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\Cloud\)  
**Last updated**: 2026-11-22  

---

## Executive Summary

*Practical Fraud Prevention: Fraud and AML Analytics for Fintech and eCommerce, Using SQL and Python* (published by O'Reilly Media in collaboration with Ping Identity, March 2022, 398 pp., ISBN `978-1-098-13830-1`) by veteran fraud-intelligence practitioners [[gilit-saporta]] (Director of Fraud Analytics at DoubleVerify; formerly PayPal and Forter) and [[shoshana-maraney]] (formerly Forter and Identiq) is a comprehensive operational and data-science treatise on defending digital commerce, consumer banking, marketplaces, and fintech platforms against intelligent financial adversaries (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, pp. 2, 5–6, 19–20). Opening with Airbnb cofounder Nathan Blecharczyk's maxim *"With commerce comes fraud,"* the authors demystify the adversarial cat-and-mouse dynamics governing trillions of dollars in online transactions (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Preface, p. 19).

Organized into five authoritative parts, Saporta and Maraney construct a complete taxonomy of **fraudster traits and archetypes** (from Amateur, Cookie-Cutter, and Gig-Economy fraudsters to Bot Generators, Organized Crime, and Friendly Fraudsters), formulate the core economic optimization of fraud defense—**maintaining dynamic tension between blocking fraud and avoiding false-decline customer friction**—and critically examine **machine learning under adversarial drift**, delayed chargeback labels, and explainability constraints (Part I). Parts II through V translate theory into actionable SQL and Python analytics across **eCommerce** (stolen credit cards, IP typology hierarchies, reshippers/mules, BORIS/BOPIS, gift-card/crypto fraud, first-party friendly fraud), **Consumer Banking** (account takeover, phishing, malware, social engineering), **Marketplace Fraud** (collusion, dubious goods, scams), and **Anti-Money Laundering (AML) & Compliance Analytics** (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Contents, pp. 9–15, 35–370).

---

## Key Arguments / Chapter Breakdown

* **Part I — Introduction to Fraud Analytics (Chapters 1–5, pp. 35–134)**:
  * *Adversarial Archetypes, Dynamic Tension & Story-Based ML*: Dissects impersonation, dark-web linking, card testing, and eight distinct **Fraudster Archetypes** (Ch. 1–2); frames fraud defense around profit margins, **Tiers of Trust**, and the psychological cost of false declines (Ch. 3); compares Rules Engines, ML, Hybrid Systems, and Consortium Models (Ch. 4); and analyzes five structural hurdles of fraud ML—class rarity, delayed feedback, noisy labels, **intelligent adversaries**, and bias/explainability—advocating **story-based models** co-designed by data scientists and domain investigators (Ch. 5) (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Ch. 1–5, pp. 37–133).

* **Part II — Ecommerce Fraud Analytics (Chapters 6–10, pp. 135–214)**:
  * *Payment, Fulfillment & First-Party Abuse*: Builds hierarchical IP geolocation/proxy typologies to detect stolen-card attacks (Ch. 6); catalogs ten physical and remote fulfillment-interception tactics including porch piracy, reshippers, parcel mules, AVS manipulation, and triangulation dropshipping (Ch. 7); analyzes Buy-Online-Pickup/Return-in-Store (**BOPIS/BORIS**) loopholes (Ch. 8), instant-liquidity **digital goods, ticketing, gift-card, and cryptocurrency fraud** (Ch. 9), and **First-Party / Friendly Fraud** (genuine mistake, family fraud, buyer's remorse, reseller and refund abuse) (Ch. 10) (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Ch. 6–10, pp. 137–214).

* **Part III — Consumer Banking Fraud Analytics (Chapters 11–14, pp. 215–288)**:
  * *Account Takeover, Malware & Social Engineering*: Investigates credential stuffing, account takeover (ATO), SIM swapping, authorized push-payment scams, phishing campaigns, and banking trojan malware combining technical compromise with psychological manipulation (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Part III, pp. 14, 215–288).

* **Parts IV–V — Marketplace Fraud & AML / Compliance Analytics (Chapters 15–18, pp. 289–370)**:
  * *Two-Sided Platform Abuse & Financial Crime*: Addresses seller-side scams, counterfeit/dubious goods, buyer-seller collusion, and regulatory Anti-Money Laundering (AML) transaction monitoring, structuring detection, and KYC compliance workflows (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Parts IV–V, pp. 15, 289–370).

---

## Key Quotes & Citations

* "'With commerce comes fraud,' wrote Airbnb cofounder Nathan Blecharczyk back in 2010, and it's safe to say that the maxim has proven itself over and over in the years since then." (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Preface, p. xvii / PDF p. 19)
* "Over the past two decades, the booming ecommerce and fintech industries have become a breeding ground for fraud. Organizations that conduct business online are constantly engaged in a cat-and-mouse game with these invaders." (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Back Cover, PDF p. 2)
* "Fraud fighters, with their heads down in the data, excel at identifying new suspicious patterns and tracking down perpetrators. The constant pressure of fraud prevention means that often, day-to-day activities prevent fraud fighters from taking a breath, putting their head above the parapet, and looking around to see what's happening outside." (source: BOOKS/Cloud/3683-practical-fraud-prevention.pdf, Preface, p. xviii / PDF p. 20)

---

## Thematic Connections

* **Security Data Lakes & Behavioral Forensics**: Forms a powerhouse cybersecurity triad with [[david-baum]]'s [[deploying-a-modern-security-data-lake]] and [[marshall-s-rich]]'s [[advanced-network-forensics-a-cyber-behavioral-science-approach]] on [[cloud-scale-fraud-analytics-and-security-data-lakes]].
* **Adversarial ML & LLM Threats**: Complements [[andrei-kucharavy]] et al.'s [[large-language-models-in-cybersecurity-threats-exposure-and-mitigation]] and [[andreas-krause]] & [[jonas-hubotter]]'s [[probabilistic-artificial-intelligence]] on statistical decision-making under uncertainty and intelligent adversaries.
* **Quantitative Criminology & DeFi**: Connects empirical financial-crime analytics to [[alex-r-piquero]] & [[david-weisburd]]'s [[handbook-of-quantitative-criminology]] and [[marco-di-maggio]]'s [[blockchain-crypto-and-defi-bridging-finance-and-technology]].

---

## Related pages

- [[gilit-saporta]]
- [[shoshana-maraney]]
- [[cybersecurity-and-digital-forensics]]
- [[data-science-and-scientific-computing]]
- [[cloud-computing-and-distributed-systems]]
- [[cloud-scale-fraud-analytics-and-security-data-lakes]]
- [[hybrid-threats-and-cyber-warfare]]
- [[rationality-and-decision-making]]
- [[deploying-a-modern-security-data-lake]]
- [[advanced-network-forensics-a-cyber-behavioral-science-approach]]
- [[large-language-models-in-cybersecurity-threats-exposure-and-mitigation]]
- [[probabilistic-artificial-intelligence]]
- [[handbook-of-quantitative-criminology]]
- [[blockchain-crypto-and-defi-bridging-finance-and-technology]]
