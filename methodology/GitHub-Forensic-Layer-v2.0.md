# COSMODROME — GitHub Forensic Evidence Layer v2.0

> **De-Facto Technical Sovereignty Indicator**
> Methodology Module for FIF / ECI Framework
> Mandatory Forensic Block for All COSMODROME Cases
> February 2026

---

## 1. Executive Summary

GitHub is the only public source where governance actions leave time-stamped traces tied to actors. Neither Snapshot, Tally, nor governance forums simultaneously provide rule declarations, their revision history, and power concentration metrics in a single version-controlled environment.

**Core thesis:** Governance tokens control voting. GitHub controls implementation. The divergence between these two centers of power is where COSMODROME finds its most valuable forensic signals.

**Strategic position:** The GitHub Forensic Layer is a mandatory block in every COSMODROME forensic case. It provides a unique analytical capability that no existing DeFi analytics platform offers: systematic assessment of de-facto technical sovereignty through development governance evidence.

**Methodological anchor:** If token governance ≠ code control → sovereignty divergence exists.

### 1.1 Evidence Hierarchy

> Within FIF, GitHub-based evidence is systematically treated as a second-order, off-chain source that can upgrade or downgrade confidence in primary layers (on-chain state, legally binding documents, treasury records, custody attestations), but never override them on its own.

---

## 2. Position Within COSMODROME Methodology

### 2.1 Evidence Layer Classification

| Layer | Description | Relationship to GitHub |
|-------|-------------|----------------------|
| On-Chain (Primary) | Token distribution, voting records, smart contract state, TVL, reserves | GitHub cannot override; cross-validates |
| GitHub (Auxiliary) | Development governance, code control concentration, pre-on-chain rule changes | This module |
| Forum / Off-Chain (Auxiliary) | Governance proposals, community discourse, temperature checks | GitHub detects contradiction with |
| Legal / Corporate (Contextual) | Entity structure, jurisdiction, filings | GitHub reveals operational identity behind |

### 2.2 Three Operational Modes

1. **Structural Mode** — Static power topology: who can merge, who reviews, who releases, who controls dependencies, who are the shadow contributors.
2. **Temporal Mode** — Dynamic sequence analysis: commit → vote → deployment timelines, governance latency asymmetry, rule mutation velocity, emergency change detection.
3. **Contradiction Mode** — Divergence detection: declared governance rhetoric vs. actual code changes, permissions, operational patterns, and stealth governance.

---

## 3. Evidence Categories (19 Total)

Each category includes: source artifacts, forensic value for ECI, and evidence status with explicit limitations.

### STRUCTURAL MODE

#### 3.1 Declared Governance Layer
- **Artifacts:** GOVERNANCE.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, security policy files, ADR/RFC directories, CODEOWNERS
- **Forensic value:** Declared model of authority. Baseline for Contradiction Mode.
- **Status:** *Declared Governance Layer — officially published team position.*

#### 3.2 Merge Authority Topology
- **Target:** Not who writes code, but who can merge to main/production.
- **Metrics:** PR merge distribution by actor, review dependency graph, CODEOWNERS enforcement, single-maintainer dependency.
- **Forensic value:** Strongest GitHub signal for de-facto control.
- **Status:** *Merge Authority Evidence — observable permission structure; highest-confidence GitHub signal.*

#### 3.3 Development Concentration & Bus Factor

| Metric | What It Measures |
|--------|-----------------|
| Contributor Gini Coefficient | Distribution of contribution power |
| Nakamoto Coefficient (dev) | Minimum actors controlling majority of commits/merges |
| Shannon Entropy | Information-theoretic evenness of contribution distribution |
| Bus Factor (git blame) | Minimum people whose departure stops critical module development |
| Core/Periphery Ratio | % activity from core group vs. external contributors |

- **Status:** *Operational Governance Signals — indirect but quantitatively measurable.*

#### 3.4 Shadow Contributors & Domain Analysis
- **Method:** Email domain analysis in commit metadata, organizational affiliation correlation.
- **Forensic value:** Detects false declarations of independent development.
- **Status:** *Shadow Contributor Evidence — metadata-derived; strong signal but subject to spoofing.*

#### 3.5 Permission Layer Visibility
- **Extractable:** Multisig admin addresses in deploy scripts, hardcoded addresses in migration scripts, hardcoded roles in contracts.
- **Forensic value:** Bridge connecting GitHub evidence to on-chain evidence.
- **Status:** *Permission Bridge Evidence (GitHub → On-Chain).*

#### 3.6 Dependency & Supply Chain Risk
- **Targets:** Third-party libraries, obscure repos controlled by narrow circle, dependency update patterns.
- **Forensic value:** Governance votes for perfect code, but if a dependency is controlled by a single anonymous account → backdoor risk.
- **Status:** *Supply Chain Risk Evidence — requires cross-validation with audits.*

#### 3.7 Commit Signing & Access Discipline
- **Metrics:** % signed (verified) commits, key distribution, enforced signing policies.
- **Status:** *Access Control Practices — operational security layer.*

#### 3.8 Process Evidence (Issues/PR Decision Patterns)
- **Targets:** How controversial changes are discussed, who has final approval, PR rejection rates for external contributors.
- **Forensic value:** Practical governance vs. declared governance.
- **Status:** *Process Evidence — qualitative but observable patterns.*

### TEMPORAL MODE

#### 3.9 Governance Change Log
- **Source:** Commit history on governance files/directories, diff analysis, author attribution.
- **Forensic value:** Timeline of power shifts correlated with on-chain events.
- **Status:** *Governance Change Log — time-stamped and actor-attributed.*

#### 3.10 Rule Mutation Velocity
- **Targets:** Change frequency in governance contracts, access control, emergency functions, upgradeability.
- **Forensic value:** Pre-on-chain power — ability to modify rules in code before activation or voting.
- **Status:** *Rule Mutation Evidence — strongest when correlated with on-chain events.*

#### 3.11 Deleted History & Force Pushes
- **Detection:** Force push events, branch deletions correlated with forum discussions, timeline gaps.
- **Forensic value:** History rewriting in governance-adjacent code is a red flag.
- **Status:** *History Manipulation Evidence — strongest negative signal.*

#### 3.12 Release Control
- **Targets:** Who performs version tagging, production releases, contract deployments.
- **Forensic value:** If releases controlled by single entity → governance token is already secondary.
- **Status:** *Release Control Evidence — last-mile indicator of what ships to production.*

### CONTRADICTION MODE

#### 3.13 Governance-Code Divergence Score (GCDS)
- **Method:** Systematic comparison of governance forum proposals vs. GitHub implementations.
- **Three sub-types:**
  - *Procedural divergence:* process not followed as declared
  - *Semantic divergence:* implemented code does not match proposal intent
  - *Timing divergence:* code predates public discussion or vote
- **Status:** *Composite metric — flagship COSMODROME indicator.*

### NEW IN v2.0

#### 3.14 Governance Latency Layer (3-Type Decomposition)

| Latency Type | What It Measures | Signal If Anomalous |
|-------------|------------------|-------------------|
| Commit → Forum | Was code written before public discussion began? | Pre-baked governance |
| Forum → Vote | Was there real deliberation time? | Rubber-stamp voting |
| Vote → Deploy | Was there review time after approval? | Rushed deployment |

- **Status:** *Governance Latency Evidence — all three sub-types must be measured independently.*

#### 3.15 Release Sovereignty Indicator
- **Scope:** Who signs releases? Who publishes packages? Who controls CI/CD pipeline credentials?
- **Status:** *Release Sovereignty Evidence — high confidence when combined with Permission Bridge.*

#### 3.16 Ghost Participation / Governance Mimicry Index (GMI)
- **Key signals:** Approval-only accounts, synchronized approval timing, zero-friction approvals.
- **Forensic value:** Detects Sybil-style attacks on development governance.
- **Status:** *Governance Mimicry Evidence — pattern-based; requires statistical validation.*

#### 3.17 The Invisible Fork (Off-Platform Coordination Detection)
- **Key signals:** Mega-Commits, activity pauses followed by sudden complete implementations, PR discussions referencing decisions made elsewhere.
- **Forensic value:** GitHub used as a loading dock, not a workshop.
- **Status:** *Off-Platform Coordination Evidence — behavioral inference; indicative, not conclusive.*

#### 3.18 Foundation Residual Control Check
- **Scope:** Who admins the GitHub organization? Who owns published packages? Who controls Docker images and oracle infrastructure?
- **Forensic value:** If a foundation retains infrastructure control while declaring DAO governance, GitHub-level decentralization is decorative.
- **Status:** *Foundation Control Evidence — infrastructure-level; high impact.*

#### 3.19 Timezone Clustering
- **Method:** Timestamp analysis of commits to identify timezone clusters.
- **Forensic value:** If "global community" operates on a single timezone → coordination barrier for external participants is high.
- **Status:** *Geographic Clustering Evidence — behavioral pattern; indicative.*

---

## 4. LM/AI-Enhanced Analysis Layer

### 4.1 Sentiment Analysis on Issues & PRs
Detect polarity over time and chilling effects after controversial decisions.

### 4.2 Commit Message & PR Description Analysis
LM classification by governance relevance. Stealth governance detection: changes framed as "refactor" that alter power distribution.

### 4.3 Contributor Communication Pattern Analysis
Authority pattern detection, decision influence network mapping, implicit hierarchy detection.

### 4.4 Automated Contradiction Detection
Cross-reference forum proposals with GitHub implementations. Backbone of Governance-Code Divergence Score.

### 4.5 Predictive Risk Scoring
*[DEFERRED] Requires completed case studies for training data. Planned after 5+ forensic cases.*

### 4.6 Prompt Integrity Protocol

Every LM-derived finding must be accompanied by:
- Model version and provider
- System prompt hash (SHA-256)
- Input data snapshot hash (SHA-256)
- Timestamp of analysis run
- Output raw text (archived for reproducibility)

### 4.7 LM Output Governance Rules

- LM output **CANNOT** increase a risk score directly.
- LM output **CAN ONLY** trigger manual review escalation.
- All LM-derived findings require human validation before inclusion in forensic reports.

---

## 5. Composite Metrics for ECI Integration

### 5.1 GitHub Centralization Multiplier (GCM)

Composite score adjusting ECI coordination barrier estimates.

| Component | Data Source |
|-----------|-----------|
| Merge Authority Gini | PR merge distribution |
| Top-1 Merge Share | Single actor merge dominance |
| Top-3 Merge Share | Oligarchic merge control |
| Review Gatekeeper Index | PR approval concentration |
| Bus Factor (critical) | git blame on core contracts |
| Domain Clustering | Contributor email domains |
| Release Signer Concentration | Tag/release actor distribution |
| Governance Mutation Velocity | Governance file change rate |

Component weights and nonlinear amplification thresholds are disclosed in client-facing dossiers.

**Interpretation tiers:** Distributed → Moderate Concentration → High Concentration → Single-Entity Effective Control.

### 5.2 Governance-Code Divergence Score (GCDS)

| Sub-Score | What It Captures |
|-----------|-----------------|
| Procedural Divergence | Process not followed as declared |
| Semantic Divergence | Implemented code does not match proposal intent |
| Timing Divergence | Code committed before public discussion |

Interpretation thresholds are disclosed in client-facing dossiers.

### 5.3 Pre-On-Chain Control Index (POCI)

Captures degree to which meaningful governance decisions are made before on-chain mechanisms activate.

### 5.4 Governance Mimicry Index (GMI)

Measures the degree of synthetic participation in development governance.

Interpretation thresholds are disclosed in client-facing dossiers.

---

## 6. Critical Limitations & Disclaimers

### 6.1 Identity Risk
GitHub account ≠ verified legal identity. Corporate orgs appear "decentralized" while managed by a single company.

### 6.2 Visibility Risk
Private repositories are invisible. Enterprise GitHub features may not be externally visible.

### 6.3 Causality Risk
Commit ≠ Decision. Actual decisions may happen in private channels.

### 6.4 Manipulation Risk
Bot activity inflates contributor counts. Force-pushed history may conceal original attribution.

### 6.5 Scope Boundary
GitHub evidence covers development and operational governance ONLY. Does NOT verify TVL, reserves, or financial positions. Does NOT replace smart contract audits.

### 6.6 Known Evasion Patterns

| Evasion Pattern | How It Works |
|----------------|-------------|
| Commit Splitting | Breaking governance-significant changes into many small "technical" commits |
| PR Batching | Bundling governance changes with unrelated features |
| Delegated Merge Accounts | Using service accounts to merge decisions made by leadership |
| Delayed Public Mirror | Developing privately, then pushing completed code (The Invisible Fork) |
| Controlled "Community" Contributors | Funded contributors presenting as independent |
| Approval Farming | Multiple accounts generating synthetic PR approvals |
| History Laundering | Squash merges or rebases eliminating granular commit history |

---

## 7. Cross-Validation Protocol

### 7.1 Required Cross-Checks

| GitHub Finding | Cross-Validate With |
|---------------|-------------------|
| High merge concentration | On-chain multisig structure |
| Governance file changes | Forum proposals, Snapshot/Tally votes |
| Domain clustering | Known team/investor disclosures |
| Emergency code changes | On-chain emergency events, post-mortems |
| Permission addresses in scripts | Current on-chain contract owner/admin addresses |
| Governance latency asymmetry | Forum post timestamps vs. commit timestamps vs. vote timestamps |

### 7.2 Finding Format (Required)

Each finding must include:
- **Signal:** what was observed (factual, no interpretation)
- **Interpretation hypothesis:** what the signal may indicate
- **Benign explanation:** alternative non-malicious interpretation (required for every significant finding)
- **Confidence level:** High / Medium / Low
- **Cross-validation status:** Confirmed / Partially confirmed / Unconfirmed / Contradicted

### 7.3 Red Flag Escalation Protocol

If any composite metric exceeds its threshold (thresholds disclosed in client dossiers):
1. ECI is automatically flagged as **"Requires Human Governance Review"**
2. Forensic report MUST contain a dedicated **"GitHub Governance Red Flags"** subsection
3. Any client decision to ignore these signals is logged as **"Client Override"** with timestamp

---

## 8. Protocol Archetypes & Application

| Archetype | Description | Expected GitHub Pattern |
|-----------|------------|----------------------|
| Foundation-led | Central foundation controls roadmap, team, treasury | High merge/release concentration; formal governance files |
| Corporate-backed | VC-funded entity controls development; token governance is advisory | Domain clustering; high core/periphery ratio |
| DAO-native | Governance token holders direct development | Distributed merge authority; high external PR acceptance |
| Hybrid | Foundation + token governance with unclear boundaries | Mixed signals; highest GCDS risk |

### 8.1 Case Study Application

| Protocol | Key GitHub Evidence Focus | Primary Mode |
|----------|--------------------------|-------------|
| MakerDAO / Sky | ESM history, spell scripts, governance contract mutations | Temporal + Contradiction |
| Lido | Dual governance impl, DSM control, LDO vs code gap | Structural + Contradiction |
| Optimism | Governance contracts, upgrade authority, security council | Structural + Temporal |
| Arbitrum | Nitro upgrade commits, DAO governance repos | Temporal + Structural |

---

## 9. FIF Integration

> GitHub Layer = De-Facto Technical Sovereignty Indicator. If token governance ≠ code control → sovereignty divergence exists.

**Module Status:** Mandatory Forensic Block for all COSMODROME cases.

---

## References

- Tan et al. (2023) — GitHub OSS Governance File Dataset. arXiv:2304.00460
- NSF (2023) — GitHub OSS Governance File Dataset
- GMU (2023) — Investigating Governance of Decentralized Projects Through GitHub
- ACM (2022) — Empirical Study of Blockchain Repositories in GitHub
- GitHub REST API — docs.github.com/en/rest/metrics

---

*Version 2.0.1 — Revised | March 2026 | COSMODROME Forensic Intelligence Framework*
