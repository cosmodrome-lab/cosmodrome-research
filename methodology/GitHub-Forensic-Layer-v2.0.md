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

**Methodological anchor:** If token governance ≠ code control → sovereignty divergence exists. This principle drives the entire module.

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

## 3. Evidence Categories (18 Total)

Each category includes: source artifacts, forensic value for ECI, and evidence status with explicit limitations.

### STRUCTURAL MODE

#### 3.1 Declared Governance Layer

- **Artifacts:** GOVERNANCE.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, security policy files, ADR/RFC directories, CODEOWNERS
- **Forensic value:** Declared model of authority (roles, rights, veto, emergency powers). Baseline for Contradiction Mode.
- **Status:** *Declared Governance Layer (GitHub) — officially published team position.*

#### 3.2 Merge Authority Topology

- **Target:** Not who writes code, but who can merge to main/production.
- **Metrics:** % PR merged by top-N maintainers, review dependency graph, CODEOWNERS enforcement, single-maintainer dependency.
- **Forensic value:** If 2 people can block an upgrade → coordination barrier high → exit feasibility decreases. Strongest GitHub signal for de-facto control.
- **Status:** *Merge Authority Evidence — observable permission structure; highest-confidence GitHub signal.*

#### 3.3 Development Concentration & Bus Factor

| Metric | What It Measures |
|--------|-----------------|
| Contributor Gini Coefficient | Distribution of contribution power; Gini > 0.8 = high concentration |
| Nakamoto Coefficient (dev) | Minimum actors controlling >50% of commits/merges |
| Shannon Entropy | Information-theoretic evenness of contribution distribution |
| Bus Factor (git blame) | Minimum people whose departure stops critical module development |
| Core/Periphery Ratio | % activity from core group vs. external contributors |

- **Status:** *Operational Governance Signals — indirect but quantitatively measurable.*

#### 3.4 Shadow Contributors & Domain Analysis

- **Method:** Email domain analysis in commit metadata (`git log --format='%ae'`), organizational affiliation correlation.
- **Forensic value:** If 70% of code from @paradigm.xyz or @lido.fi emails in a "decentralized" project → declaration of independent development is false.
- **Status:** *Shadow Contributor Evidence — metadata-derived; strong signal but subject to spoofing.*

#### 3.5 Permission Layer Visibility

- **Extractable:** Multisig admin addresses in README/deploy scripts, hardcoded addresses in migration scripts, hardcoded roles in contracts.
- **Forensic value:** Bridge connecting GitHub evidence to on-chain evidence. Deploy scripts reveal intended privileged roles.
- **Status:** *Permission Bridge Evidence (GitHub → On-Chain).*

#### 3.6 Dependency & Supply Chain Risk

- **Targets:** Third-party libraries, closed/obscure repos controlled by narrow circle, dependency update patterns.
- **Forensic value:** Governance votes for perfect code, but if a dependency is controlled by a single anonymous account → backdoor risk.
- **Status:** *Supply Chain Risk Evidence — critical for security; requires cross-validation with audits.*

#### 3.7 Commit Signing & Access Discipline

- **Metrics:** % signed (verified) commits, key distribution, enforced signing policies.
- **Forensic value:** Maturity of access control, formalized responsibility chains.
- **Status:** *Access Control Practices — operational security layer.*

#### 3.8 Process Evidence (Issues/PR Decision Patterns)

- **Targets:** How controversial changes are discussed, who has final approval, PR rejection rates for external contributors.
- **Forensic value:** Practical governance vs. declared governance. If one contributor consistently ends discussions → de-facto authority.
- **Status:** *Process Evidence — qualitative but observable patterns.*

### TEMPORAL MODE

#### 3.9 Governance Change Log

- **Source:** Commit history on governance files/directories, diff analysis, author attribution.
- **Forensic value:** Timeline of power shifts (veto added/removed, quorum changes). Correlation with on-chain events.
- **Status:** *Governance Change Log — time-stamped and actor-attributed; close to verifiable.*

#### 3.10 Rule Mutation Velocity

- **Targets:** Change frequency in governance contracts, access control, emergency functions, upgradeability.
- **Context analysis:** Before which event? Before/after on-chain vote? Silent commits?
- **Forensic value:** Pre-on-chain power — ability to modify rules in code before activation or voting.
- **Status:** *Rule Mutation Evidence — strongest when correlated with on-chain events.*

#### 3.11 Deleted History & Force Pushes

- **Detection:** Force push events (GitHub Events API), branch deletions correlated with forum discussions, timeline gaps.
- **Forensic value:** Equivalent to document destruction. History rewriting in governance-adjacent code is a red flag.
- **Status:** *History Manipulation Evidence — strongest negative signal; absence of evidence = evidence of concealment.*

#### 3.12 Release Control

- **Targets:** Who performs version tagging, production releases, contract deployments, NPM package publication.
- **Forensic value:** If releases controlled by single entity → governance token is already secondary.
- **Status:** *Release Control Evidence — last-mile indicator of what ships to production.*

### CONTRADICTION MODE

#### 3.13 Governance-Code Divergence Score

- **Method:** Systematic comparison of governance forum proposals vs. GitHub implementations.
- **Three sub-types:**
  - *Procedural divergence:* process not followed as declared
  - *Semantic divergence:* implemented code does not match proposal intent
  - *Timing divergence:* code predates public discussion or vote
- **Status:** *Composite metric — requires cross-layer analysis; flagship COSMODROME indicator.*

### NEW IN v2.0

#### 3.14 Governance Latency Layer

- **Focus:** Latency asymmetry between commit, public discussion, vote, and deployment.
- **Key signals:**
  - Code committed significantly before public forum discussion?
  - PR discussed privately, forum sees only "final version"?
  - Deploy happens immediately after vote without realistic review window?
- **Forensic value:** Detects *Governance Preparedness Bias* — if code is ready before public discussion, governance may be a formality. Critical for Lido and MakerDAO cases.
- **Status:** *Governance Latency Evidence — temporal indicator; strongest when combined with forum analysis.*

#### 3.15 Release Sovereignty Indicator

- **Scope beyond basic Release Control:** Who signs releases? Who publishes NPM packages? Who deploys production artifacts? Who controls the CI/CD pipeline credentials?
- **Forensic value:** Stronger than merge authority alone. Production release pipeline control = final veto over all governance decisions.
- **Status:** *Release Sovereignty Evidence — operational; high confidence when combined with Permission Bridge.*

#### 3.16 Ghost Participation / Governance Mimicry Index (GMI)

- **Method:** Interaction graph analysis of PR approvals. Detect patterns where N accounts always approve 1 account without substantive review.
- **Key signals:**
  - Approval-only accounts: approve PRs but never comment, request changes, or submit code
  - Synchronized approval timing: multiple approvals within minutes of each other
  - Zero-friction approvals: 100% approval rate with no rejections or discussions
- **Forensic value:** Detects Sybil-style attacks on development governance. 10 accounts always approving 1 account without edits = not consensus, but mimicry.
- **Status:** *Governance Mimicry Evidence — pattern-based; requires statistical validation of thresholds.*

#### 3.17 The Invisible Fork (Off-Platform Coordination Detection)

- **Method:** Detect anomalous patterns indicating real work happens outside GitHub.
- **Key signals:**
  - Mega-Commits: Large, complex code blocks appearing without incremental PR history
  - Activity pauses followed by sudden complete implementations
  - PR discussions that reference decisions made elsewhere ("as agreed", "per our discussion")
- **Forensic value:** Proves real coordination happens in private Slack/Discord/Telegram. GitHub is used as a loading dock, not a workshop. For ECI: maximum opacity signal (Low Transparency Score).
- **Status:** *Off-Platform Coordination Evidence — behavioral inference; indicative, not conclusive.*

#### 3.18 Timezone Clustering

- **Method:** Timestamp analysis of commits to identify timezone clusters.
- **Forensic value:** If "global community" operates on San Francisco time → coordination barrier for external participants is prohibitively high.
- **Status:** *Geographic Clustering Evidence — behavioral pattern; indicative (remote workers, flexible schedules).*

---

## 4. LM/AI-Enhanced Analysis Layer

### 4.1 Sentiment Analysis on Issues & PRs

- Apply sentiment classification to governance-relevant issue/PR discussions.
- Track polarity over time: contentious, submissive, disengaged?
- Detect chilling effects: declining engagement after controversial decisions = governance suppression.

### 4.2 Commit Message & PR Description Analysis

- LM classification by governance relevance (security, access control, permissions, emergency, upgrade).
- Automated detection of governance-significant changes committed without forum proposals.
- Stealth governance detection: changes framed as "refactor" that actually alter power distribution.

### 4.3 Contributor Communication Pattern Analysis

- Authority pattern detection: whose opinions consistently end discussions?
- Decision influence network mapping: who tags whom, who defers to whom.
- Implicit hierarchy detection vs. declared role structure.

### 4.4 Automated Contradiction Detection

- Cross-reference forum proposals (text) with GitHub implementations (code).
- LM-powered semantic comparison: does implemented code match stated intent?
- Scope creep/reduction detection between proposal and implementation.
- Backbone of Governance-Code Divergence Score (§3.13).

### 4.5 Predictive Risk Scoring

- Train models on historical governance failure patterns.
- Feature inputs: mutation velocity, concentration metrics, sentiment trends, contribution entropy.
- Output: probability scores for governance risk categories.
- *[DEFERRED] Requires completed case studies for training data. Planned after 5+ forensic cases.*

### 4.6 Prompt Integrity Protocol

Every LM-derived finding in a COSMODROME report must be accompanied by:

- Model version and provider
- Temperature and sampling parameters
- System prompt hash (SHA-256)
- Input data snapshot hash (SHA-256)
- Timestamp of analysis run
- Output raw text (archived for reproducibility)

> Rationale: If a client asks "Why did you conclude this commit is stealth governance?", we show a transparent, reproducible analysis pipeline — not "the neural network said so".

### 4.7 LM Output Governance Rules

Mandatory constraints on how LM outputs are used:

- LM output **CANNOT** increase a risk score directly.
- LM output **CAN ONLY** trigger manual review escalation.
- All LM-derived findings require human validation before inclusion in forensic reports.
- Model biases and hallucination risks must be documented per-finding.
- Reproducibility: all parameters logged for audit trail.

> This protects COSMODROME from "AI hallucination scoring" accusations and ensures methodological defensibility.

---

## 5. Composite Metrics for ECI Integration

### 5.1 GitHub Centralization Multiplier (GCM)

Composite score adjusting ECI coordination barrier estimates. **NONLINEAR:** if top-1 merge share > 60%, multiplier amplifies exponentially.

| Component | Data Source | Weight |
|-----------|-----------|--------|
| Merge Authority Gini | PR merge distribution | 0.20 |
| Top-1 Merge Share | Single actor merge dominance | 0.15 |
| Top-3 Merge Share | Oligarchic merge control | 0.10 |
| Review Gatekeeper Index | PR approval concentration | 0.15 |
| Bus Factor (critical) | git blame on core contracts | 0.15 |
| Domain Clustering | Contributor email domains | 0.10 |
| Release Signer Conc. | Tag/release actor distribution | 0.10 |
| Gov. Mutation Velocity | Governance file change rate | 0.05 |

**Nonlinear amplification:** If Top-1 Merge Share > 60% OR Bus Factor = 1 for any critical module → GCM is amplified by factor 1.5x before normalization. This prevents "averaging away" extreme concentration.

**Interpretation:** GCM 0.0–0.3 = distributed; 0.3–0.6 = moderate concentration; 0.6–0.8 = high concentration; >0.8 = single-entity effective control.

**ECI trigger:** GCM > 0.7 triggers coordination barrier uplift in ECI scoring.

### 5.2 Governance-Code Divergence Score (GCDS)

Three-component decomposition:

| Sub-Score | What It Captures |
|-----------|-----------------|
| Procedural Divergence | Process not followed as declared (votes skipped, review periods shortened) |
| Semantic Divergence | Implemented code does not match proposal intent (scope creep, silent additions) |
| Timing Divergence | Code committed before public discussion; pre-baked implementations |

**Interpretation:** Combined GCDS > 0.5 = significant governance theater risk; > 0.7 = mandatory explicit section in forensic report.

### 5.3 Pre-On-Chain Control Index (POCI)

Captures degree to which meaningful governance decisions are made before on-chain mechanisms.

- % governance-sensitive code changes made without corresponding on-chain proposals
- % governance-sensitive changes introduced pre-forum (strongest forensic signal)
- Average time delta between code commit and on-chain vote
- Frequency of "silent commits" affecting permissions or access control

### 5.4 Governance Mimicry Index (GMI)

Measures the degree of synthetic participation in development governance.

- Ratio of approval-only contributors to substantive contributors
- Approval synchronization score (timing-based)
- Zero-friction approval rate

**Interpretation:** GMI > 0.6 = suspected mimicry; > 0.8 = Sybil-grade participation theater.

---

## 6. Critical Limitations & Disclaimers

### 6.1 Identity Risk

- GitHub account ≠ verified legal identity. One person = multiple accounts. Organizations mask concentration through aliases.
- Corporate GitHub orgs appear "decentralized" while managed by a single company.
- Proxy contributors: core dev pushes through junior contributor accounts.

### 6.2 Visibility Risk

- Private repositories and closed mirrors are invisible.
- Enterprise GitHub features (audit logs, advanced permissions) may not be externally visible.

### 6.3 Causality Risk

- Commit ≠ Decision. Actual decisions may happen in Telegram/Slack/private channels.
- Correlation with governance events ≠ causation without additional evidence.

### 6.4 Manipulation Risk

- Bot activity inflates contributor counts and commit frequency. CI/CD commits must be filtered.
- Force-pushed or rewritten history may conceal original attribution.
- Commit signing spoofable if key management compromised.

### 6.5 Scope Boundary

- GitHub evidence covers development and operational governance ONLY.
- Does NOT verify: TVL, reserves, balances, financial positions, token economics.
- Does NOT replace: smart contract audits, on-chain forensics, legal structure analysis.

### 6.6 Known Evasion Patterns

To maintain methodological credibility, COSMODROME explicitly documents known ways actors can circumvent GitHub-based detection:

| Evasion Pattern | How It Works |
|----------------|-------------|
| Commit Splitting | Breaking a governance-significant change into many small "technical" commits to avoid detection |
| PR Batching | Bundling governance changes with unrelated features to obscure intent |
| Delegated Merge Accounts | Using service accounts or junior devs to merge decisions made by leadership |
| Delayed Public Mirror | Developing in private, then pushing "completed" code to public repo (The Invisible Fork) |
| Controlled "Community" Contributors | Funded contributors presenting as independent community members |
| Approval Farming | Creating multiple accounts to generate synthetic PR approvals (Ghost Participation) |
| History Laundering | Using squash merges or rebases to eliminate granular commit history |

> Acknowledging these patterns makes the methodology robust. Not acknowledging them makes it naive.

---

## 7. Cross-Validation Protocol

### 7.1 Required Cross-Checks

| GitHub Finding | Cross-Validate With |
|---------------|-------------------|
| High merge concentration | On-chain multisig structure, token distribution among core team |
| Governance file changes | Forum proposals, Snapshot/Tally votes, protocol announcements |
| Domain clustering | Known team/investor disclosures, LinkedIn/public profiles |
| Emergency code changes | On-chain emergency events, post-mortem reports |
| Permission addresses in scripts | Current on-chain contract owner/admin addresses |
| Dependency risks | Smart contract audit reports, known vulnerability databases |
| Sentiment decline | Forum activity metrics, token holder behavior (delegation changes) |
| Ghost participation signals | On-chain voting patterns of same addresses (if linked) |
| Governance latency asymmetry | Forum post timestamps vs. commit timestamps vs. vote timestamps |

### 7.2 Reporting Standard

Each GitHub evidence finding in a forensic report must include:

- **Finding:** what was observed
- **Evidence type:** which category from Section 3
- **Confidence level:** High / Medium / Low (based on cross-validation)
- **Cross-validation status:** Confirmed / Partially confirmed / Unconfirmed / Contradicted
- **Limitations:** specific caveats from Section 6 that apply

### 7.3 Red Flag Escalation Protocol

If any composite score exceeds its threshold: GCM > 0.7, GCDS > 0.5, POCI > 0.6, or GMI > 0.6 — then:

1. ECI is automatically flagged as **"Requires Human Governance Review"**.
2. Forensic report MUST contain a dedicated **"GitHub Governance Red Flags"** subsection.
3. Any client decision to ignore these signals is explicitly logged as **"Client Override"** with timestamp and rationale.

> Red flags cannot be silently ignored. This protects both COSMODROME's credibility and the client's decision audit trail.

---

## 8. Protocol Archetypes & Application

### 8.1 Protocol Archetypes

| Archetype | Description | Expected GitHub Pattern |
|-----------|------------|----------------------|
| Foundation-led | Central foundation controls roadmap, team, treasury (e.g., Optimism Foundation) | High merge/release concentration; clear CODEOWNERS; formal governance files; moderate external contribution |
| Corporate-backed | VC-funded entity controls development; token governance is advisory (e.g., Lido early phase) | Domain clustering at corporate emails; high core/periphery ratio; low external PR acceptance rate |
| DAO-native | Governance token holders direct development through proposals (e.g., MakerDAO aspirational model) | Distributed merge authority; high external PR acceptance; governance files match on-chain reality |
| Hybrid | Foundation + token governance with unclear boundaries (e.g., Arbitrum, Lido post-V2) | Mixed signals; declared DAO but operational foundation control; highest GCDS risk |

**Usage:** Each forensic case first classifies the protocol archetype, then evaluates GitHub evidence against the expected pattern. Deviations from expected pattern are the primary forensic signals.

### 8.2 High-Value Target Characteristics

- Upgradeable protocols (proxy patterns, UUPS, diamond)
- Governance frameworks with timelocks
- Multisig-managed systems
- Emergency module protocols (pause, guardian, ESM)

### 8.3 Case Study Application

| Protocol | Key GitHub Evidence Focus | Primary Mode |
|----------|--------------------------|-------------|
| MakerDAO / Sky | ESM history, spell scripts, governance contract mutations | Temporal + Contradiction |
| Lido | Dual governance impl, DSM control, staking router changes, LDO vs code gap | Structural + Contradiction |
| Optimism | Governance contracts repo, upgrade authority, security council mgmt | Structural + Temporal |
| Arbitrum | Nitro upgrade commits, security council tooling, DAO governance repos | Temporal + Structural |

---

## 9. FIF Integration

### 9.1 Sovereignty Divergence Principle

> GitHub Layer = De-Facto Technical Sovereignty Indicator. If token governance ≠ code control → sovereignty divergence exists. This divergence is the primary forensic signal of the GitHub evidence layer.

### 9.2 Module Integration Text

> GitHub-based Governance Evidence: COSMODROME systematically collects and classifies GitHub artifacts across 18 evidence categories organized in three operational modes (Structural, Temporal, Contradiction). Analysis is enhanced by LM/AI tools with strict Prompt Integrity Protocol and output governance rules (LM outputs trigger escalation, never score directly). Four composite metrics (GCM, GCDS, POCI, GMI) feed into ECI with nonlinear amplification for extreme concentration. All findings undergo mandatory cross-validation against on-chain and off-chain governance records. Known evasion patterns are explicitly documented. Red Flag Escalation Protocol ensures no critical signal is silently ignored. GitHub evidence does not verify financial positions, TVL, or token economics, and does not replace smart contract audits or legal structure analysis.

### 9.3 Module Status

- **Classification:** Mandatory Forensic Block for all COSMODROME cases.
- **First application:** Case #005 (Lido) — audit checklist ready for execution.
- **Next steps:** Execute Lido data collection pipeline, produce first scored report, calibrate thresholds.

---

## 10. Tooling & Automation Roadmap

### 10.1 Data Collection Pipeline

- GitHub REST + GraphQL API for metrics extraction
- git log parsing for commit metadata (domains, timestamps, signatures)
- GitHub Events API for force push / branch deletion detection
- Dependency tree extraction (npm audit, pip, cargo audit)
- PR interaction graph builder for GMI calculation

### 10.2 Analysis Automation

- Gini coefficient / Nakamoto coefficient calculator
- Timezone clustering visualizer from commit timestamps
- Merge authority graph generator from PR data
- LM pipeline for sentiment analysis (with Prompt Integrity logging)
- Automated GCDS scorer (forum text vs. GitHub diffs)
- Ghost participation detector (approval pattern analyzer)
- Mega-commit / invisible fork detector

### 10.3 Deferred

- Benchmark dataset for top-20 DeFi protocols (after 3+ completed cases)
- Predictive ML models (after 5+ cases with labeled training data)
- Infrastructure Dependency Risk layer (CI/CD, Docker, RPC — Adjacent Risk Layer v3.0)
- GitHub Archive integration for historical backtesting
- ZK-proof integration for verifiable private governance (research stage)

---

## References

**Academic & Research:**
- Tan et al. (2023) — GitHub OSS Governance File Dataset. arXiv:2304.00460
- NSF (2023) — GitHub OSS Governance File Dataset. par.nsf.gov/servlets/purl/10468951
- GMU (2023) — Investigating Governance of Decentralized Projects Through GitHub. journals.gmu.edu/jssr/article/view/4259
- GMU (2023) — Effect of Funding and Governance Models. journals.gmu.edu/jssr/article/view/4261
- ACM (2022) — Empirical Study of Blockchain Repositories in GitHub. dl.acm.org/doi/10.1145/3530019.3530041
- arXiv (2025) — Prevalence and Usage of Commit Signing on GitHub. arxiv.org/html/2504.19215v1

**Technical:**
- GitHub REST API — docs.github.com/en/rest/metrics
- GitHub OSS Governance Models — github.com/cornelius/open-source-governance

---

*Version 2.0 | February 2026 | COSMODROME Forensic Intelligence Framework*
