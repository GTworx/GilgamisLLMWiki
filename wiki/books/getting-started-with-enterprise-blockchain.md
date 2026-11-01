# Getting Started with Enterprise Blockchain: A Guide to Design and Development

**Author(s)**: [[michael-bradley]], [[david-gorman]], [[matt-lucas]], [[matthew-golby-kirk]]  
**Genre(s)**: [[blockchain-and-decentralized-finance]], [[strategic-studies]], [[leadership-and-management]]  
**Key Themes**: [[decentralized-trust-and-cryptographic-governance]], [[cooperation-and-reciprocity]], [[semiconductor-geopolitics-and-chokepoints]]  
**Publication Year**: 2019  
**Source**: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf (Mount: C:\Users\gokha\iCloudDrive\Documents\_GilgameshLibrary\BOOKS\Blockchain_\)  
**Last updated**: 2026-11-01  

---

## Executive Summary

*Getting Started with Enterprise Blockchain: A Guide to Design and Development* (published by O'Reilly Media and IBM Corporation, 2019, 86 pp.) by [[michael-bradley]], [[david-gorman]], [[matt-lucas]], and [[matthew-golby-kirk]] (with a Foreword by Clause Inc. CTO Dan Selman) is an engineering and governance handbook for designing, deploying, and scaling **private, permissioned enterprise blockchain networks** built on Linux Foundation's **Hyperledger Fabric** (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, pp. 3–9, 13–29). Unlike public, unpermissioned cryptocurrency networks (such as Bitcoin) that rely on pseudonymous participants and energy-intensive Proof-of-Work to establish trust among strangers, enterprise business networks require known participant identities (PKI X.509 certificates), selective data privacy, deterministic finality, high transaction throughput, and regulatory compliance (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, pp. 9, 13–28, 51).

Across five concise chapters, the authors guide architects through selecting high-value multi-party business use cases (supply chain provenance, trade finance, food safety, letter-of-credit settlement), establishing consortium governance models (founder-led, consortium-shared, or regulator-anchored), configuring Hyperledger Fabric channels, private data collections, endorsement policies, and Hardware Security Modules (HSMs), and writing smart contracts (chaincode) that synchronize multi-company workflows without a single centralized database custodian (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, pp. 5–8, 31–85).

---

## Key Arguments / Chapter Breakdown

* **Foreword & Chapter 1: Introduction to Blockchain in the Enterprise (pp. v–ix, 1–18)**:
  * *Shared Ledgers vs. Siloed Reconciliations*: Contrasts traditional business networks—where each firm maintains its own private ledger reconciled through costly, error-prone messaging and audits—with a single shared, append-only permissioned ledger using cryptographic proofs, X.509 digital identity, and smart contracts (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, pp. 7–9, 13–21).

* **Chapter 2: Choosing an Appropriate Use Case (pp. 19–30)**:
  * *When You Do (and Don't) Need a Blockchain*: Defines rigorous qualification criteria for enterprise blockchain: multiple organizations, lack of a single trusted intermediary, shared asset state transitions, auditability requirements, and friction from manual reconciliation. Warns against using blockchain as an overpriced internal database (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, pp. 19–30).

* **Chapter 3: Designing a Blockchain Network — Governance, Privacy & Security (pp. 31–54)**:
  * *Consortium Governance and Selective Privacy*: Details consortium legal/funding governance, network topology, Hyperledger Fabric endorsement policies (e.g., 2-of-3 organizations must sign a transaction), private data collections, GDPR compliance (keeping PII off-chain via cryptographic hashes), and PKI Certificate Authorities (CAs) (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, pp. 31–54).

* **Chapters 4–5: Developing Blockchain Applications & Network Operations (pp. 55–85)**:
  * *Execute-Order-Validate Architecture*: Explains Hyperledger Fabric's three-phase transaction flow (*Execute/Endorse* -> *Order* via Raft/Kafka ordering service -> *Validate/Commit*), smart contract lifecycle management, REST API integration with legacy ERP systems, and production DevOps monitoring (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, pp. 55–85).

---

## Key Quotes & Citations

* "Blockchain is a shared, distributed ledger that records transactions across business networks with the aim of helping businesses remove inefficiencies from trade. It does this through the use of cryptographic proofs, which help engender trust by ensuring facts are reported consistently to all those with a need to see them." (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, ch. 1, p. 13)
* "Blockchain forces business and technical leaders to confront fundamental (and difficult!) issues around standardization of data formats, trust, privacy, governance, and legal/regulatory oversight." (source: BOOKS/Blockchain_/Book OReilley IBM getting-started-with-enterprise-blockchain_46025046USEN.pdf, Foreword, p. 8)

---

## Thematic Connections

* **Public DeFi vs. Enterprise Permissioned Ledgers**: Pairs directly with [[marco-di-maggio]]'s [[blockchain-crypto-and-defi-bridging-finance-and-technology]], contrasting permissionless token-incentivized networks with permissioned PKI corporate consortia.
* **Cryptographic Chain of Custody in Forensics**: Hyperledger Fabric's immutable audit trails and PKI endorsement policies underpin the blockchain-based forensic evidence integrity frameworks analyzed by [[marshall-s-rich]] in [[advanced-network-forensics-a-cyber-behavioral-science-approach]].

---

## Related pages

- [[michael-bradley]]
- [[david-gorman]]
- [[matt-lucas]]
- [[matthew-golby-kirk]]
- [[blockchain-and-decentralized-finance]]
- [[strategic-studies]]
- [[leadership-and-management]]
- [[decentralized-trust-and-cryptographic-governance]]
- [[cooperation-and-reciprocity]]
- [[semiconductor-geopolitics-and-chokepoints]]
- [[marco-di-maggio]]
- [[blockchain-crypto-and-defi-bridging-finance-and-technology]]
- [[marshall-s-rich]]
- [[advanced-network-forensics-a-cyber-behavioral-science-approach]]
