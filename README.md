# COSMODROME Research

**Independent Forensic Governance Analysis for DeFi Infrastructure**

> *"Governance is not voting. Governance is the architecture of control."*

---

## What Is This Repository

`cosmodrome-research` is the public evidence layer of the COSMODROME forensic intelligence system.

It contains:
- Published case study abstracts and findings
- Forensic methodology documentation
- Evidence integrity standards
- The analytical frameworks used across all COSMODROME publications

This repository does **not** contain operational infrastructure, monitoring pipelines, or unpublished intelligence.

---

## Why Governance Risk Is a Capital Risk

DeFi protocols present themselves as decentralized, transparent, and community-governed. The forensic record tells a different story.

Across the protocols we have examined, a consistent pattern emerges:

- **Governance architecture is designed to minimize friction for insiders**, not to protect external capital
- **Code changes routinely precede or bypass governance votes** — the on-chain record is the authoritative source, not the forum post
- **Information absence is itself a signal** — what is not disclosed, not collected, or actively obscured carries forensic weight equal to what is present
- **Token-weighted voting concentrates veto power** while distributing the appearance of participation

COSMODROME treats governance as an engineering object, not a political one. We apply forensic methodology to primary sources: on-chain data, Git commit histories, multisig key registries, treasury flows, and validator/sequencer concentration metrics.

---

## Forensic Case Registry

| Case ID | Protocol | Classification | Status | Publication |
|---------|----------|----------------|--------|-------------|
| CASE-001 | Arbitrum (ARB) | Self-Qualifying Constitutional Override | Forthcoming | — |
| CASE-002 | Optimism (OP) | Hostage Risk — 2-of-2 Security Council | Forthcoming | — |
| CASE-003 | Maker / Sky (MKR) | Plutocratic ESM — $238M Coordination Threshold | Forthcoming | — |
| CASE-004 | NEAR Protocol | Weak RTA — Governance Capture Window | Forthcoming | — |
| CASE-005 | Hyperliquid (HYPE) | $10M/Day Unlock Pressure vs. Opaque Validator Set | Active | [Medium →](https://medium.com/@Cosmodrome-eng) |
| CASE-006 | Aave (AAVE) | Governance Control vs. Interface Execution Layer | Published | [Medium →](https://medium.com/@Cosmodrome-eng) |

Full methodology for each case is documented in [`/cases`](./cases/) *(forthcoming)*.

---

## Analytical Framework

### Core Forensic Principle

> *Dictatorship of Code over Promises.*

What is deployed on-chain and what is committed to version control is the ground truth. Governance forum posts, blog announcements, and community calls are secondary sources subject to revision, deletion, and misrepresentation.

### Marker System

Each case study uses a color-coded marker system applied to 10 protocol-specific indicators:

| Marker | Meaning |
|--------|---------|
| 🟢 Green | Documented, verifiable, low risk |
| 🟡 Yellow | Partially disclosed or conditionally dependent |
| 🔴 Red | High risk, confirmed or structurally inevitable |
| ⚫ Black | Information absent by design or disappeared |
| ⚠️ Triangle | Requires external dependency not under protocol control |

### Four Types of Information Absence

Information absence is treated as a first-class forensic signal:

1. **Not collected** — the protocol does not measure or publish this data
2. **Closed by design** — the information exists but access is restricted
3. **Disappeared** — previously available information has been removed → *automatic risk elevation*
4. **Obfuscated** — information is technically present but structured to prevent analysis

### Evidence Integrity

All source documents referenced in COSMODROME publications are:
- Hashed at time of collection (SHA-256)
- Timestamped against block height or commit hash where applicable
- Classified by source type (on-chain / Git / official documentation / third-party)
- Retained in a tamper-evident custody chain

This standard exists because governance-relevant documents — including multisig configurations, upgrade proposals, and treasury disclosures — are routinely modified or deleted after publication.

---

## Publications

All COSMODROME analytical content is published on Medium under the **Cosmodrome-eng** publication:

🔗 [https://medium.com/@Cosmodrome-eng](https://medium.com/@Cosmodrome-eng)

### Published Articles

**Governance Is Capital Risk Series**
- [The Harvard Effect: Why ETH ETFs Are Opening Pandora's Box for Institutional Investors](https://medium.com/@Cosmodrome-eng) — Feb 23
- [Lido Dual Governance: Coordination Feasibility Under Stress](https://medium.com/@Cosmodrome-eng) — Feb 26 / Mar 7

**Aave Governance Track**
- [Aave: The CoW Swap Thread](https://medium.com/@Cosmodrome-eng) — Mar 14
- [Who Actually Controls Aave](https://medium.com/@Cosmodrome-eng) — Mar 17

**The $10 Million Daily Question (HYPE / Hyperliquid)**
- Active series. Distribution across Mirror.xyz, Reddit, and X.

---

## Methodology Document

→ [`METHODOLOGY.md`](./METHODOLOGY.md)

Core analytical standards, source classification hierarchy, and the Forensic Intelligence Framework (FIF) used across all case studies.

---

## Evidence Integrity Standards

→ [`EVIDENCE-STANDARDS.md`](./EVIDENCE-STANDARDS.md)

SHA-256 verification protocol, custody chain requirements, and the four-type absence classification system.

---

## Contact

**COSMODROME Research**
cosmodrome-lab@proton.me

For institutional inquiries, methodology licensing, or bespoke governance risk assessments.

---

*COSMODROME produces independent forensic governance intelligence. We hold no positions in the protocols we analyze. All findings are based on primary source documentation available at the time of publication. This is not investment advice.*

