# Case #005: Lido — GitHub Audit Checklist

> **Target:** github.com/lidofinance (245+ repos, Feb 2026)  
> **Core repo:** lidofinance/core (468 stars, 267 forks)  
> **Key repos:** dual-governance, community-staking-module, easy-track  
> **Archetype:** Corporate-backed → Hybrid transition  
> **Methodology:** COSMODROME GitHub Forensic Layer v2.0

---

## Evidence Integrity Block

| Parameter | Value |
|-----------|-------|
| Snapshot date (UTC) | 2026-02-24 |
| Data source | GitHub web UI, public PR pages, public release pages |
| Extraction method | Manual sampling (not API export) |
| Repo state at snapshot | lidofinance/core: 9786+ commits, 52 contributors, 468 stars |
| Sample size | 8 merged PRs (Mar-Oct 2025), 1 release (v2.1.0) |
| Tooling | None (manual review). Full quantification requires GitHub REST/GraphQL API |

**Reproducibility note:** All findings below are derived from publicly visible data. Any party with GitHub access can verify these observations independently.

---

## Investigation Status

| Phase | Description | Status |
|-------|------------|--------|
| Structural scan (sample) | Merge authority, review patterns, release control from 8 PRs | DONE — signal detected |
| Full quantification | All merged PRs, Gini, Nakamoto, actor shares | PENDING — requires GitHub API export |
| CODEOWNERS analysis | Formal permission mapping | PENDING — requires repo inspection |
| Bus Factor | git blame on critical contracts | PENDING — requires clone |
| Nakamoto Dev Coefficient | Min actors for >51% merges / >80% critical code | PENDING — requires full dataset |
| On-chain cross-validation | Multisig, Easy Track, DSM guardian overlap | PENDING — client layer |
| Governance latency (3-type) | Commit↔forum, forum↔vote, vote↔deploy | PENDING — client layer |
| GCDS scoring | Forum proposals vs. code implementations | PENDING — client layer |
| Foundation residual control | GitHub org admin, npm, Docker, oracle infra | PENDING — client layer |
| Final GCM/ECI scoring | Composite metrics from all components | PENDING — after quantification |

---

## Structural Mode

### Declared Governance Layer
- **Check:** Scan repos for GOVERNANCE.md, CONTRIBUTING.md, CODEOWNERS, security policies.
- **Found:** CONTRIBUTING.md in core. No explicit GOVERNANCE.md. Dual-governance repo covers contracts. DAO references in README only.
- **Confidence:** Medium.

### CODEOWNERS Analysis
- **Check:** Does CODEOWNERS file exist? Who are the required reviewers? Does formal authority match observed merge/review patterns?
- **Status:** NOT YET ANALYZED.
- **Why it matters:** If CODEOWNERS matches observed merge/review concentration → formalized centralization (policy-driven). If it doesn't match → shadow authority (de-facto power exceeds declared roles).

### Merge Authority Topology

**Observed pattern (sample, n=8):**
- One Member-status account performs majority of merges to main/develop, including all develop→master syncs and dependency merges.
- One Contributor-status account serves as primary reviewer on all 8 sampled PRs.
- Consistent flow: Contributor submits → Actor B reviews → Actor A merges.
- In 2 cases, a third actor (Actor C) self-merged after Actor B's approval.

**Open questions:**
- Does Actor C's self-merge indicate distributed permissions or exception? Requires full dataset.
- Is merge concentration policy-driven (maintainer model) or emergent?

**Benign explanation:** Many mature OSS projects use a small maintainer group by design. Concentration alone is not inherently problematic — it becomes a governance risk when combined with on-chain control overlap and low transparency about the arrangement.

**Confidence:** Medium (consistent pattern in sample, but n=8 is insufficient for statistical claims).

### Development Concentration

**Observed:**
- Contributor Gini coefficient: 0.686 (bootstrap) → 0.817 (maturity). Source: external research, not independently replicated.
- 52 contributors listed; core group dominates activity.

**Derived metrics (pending full quantification):**
- Nakamoto Dev Coefficient (merge): estimated ~2 (min actors for >51% of merges). Requires full PR dataset to confirm.
- Nakamoto Dev Coefficient (code): unknown. Requires git blame on critical modules.

**Benign explanation:** High Gini is common in OSS. The relevant question is whether concentration is increasing or decreasing over time, and whether it extends to governance-critical decisions.

**Confidence:** Medium-High (Gini from external study; trend direction confirmed).

### Shadow Contributors
- **Check:** Email domain analysis, bot filtering, organizational affiliation.
- **Found:** One identified personal Gmail email. Member vs Contributor badge split observed.
- **Confidence:** Low — requires full git log domain extraction.

### Permission Bridge
- **Check:** Deploy scripts, migration files → on-chain admin addresses.
- **Found:** Core maintainers linked to DAO via Easy Track mechanism. Gap between dev centralization and DAO declarations.
- **Confidence:** Medium — requires on-chain address mapping (client layer).

### Ghost Participation (GMI)
- **Check:** PR approval interaction graph, rubber-stamp detection.
- **Status:** NOT YET ANALYZED.

### Foundation Residual Control Risk
- **Check:** Who admins the GitHub org (lidofinance)? Who owns npm packages? Who controls Docker images for production? Who controls oracle infrastructure?
- **Status:** NOT YET ANALYZED.
- **Why it matters:** If the foundation (or a single entity) retains infrastructure control, GitHub-level decentralization is secondary. The entity that controls deployment infrastructure holds the real veto.

---

## Temporal Mode

### Governance Change Log
- **Check:** Diff history on governance files, access control changes.
- **Known:** 9786 commits in core. Active Jan-Feb 2026.
- **Confidence:** High data volume available for analysis.

### Governance Latency (3-Type Decomposition)

Three distinct latency measurements required:

| Latency Type | What It Measures | Signal If Anomalous |
|-------------|------------------|-------------------|
| **Commit → Forum** | Was code written before public discussion began? | Pre-baked governance: decisions made before community input |
| **Forum → Vote** | Was there real deliberation time between proposal and vote? | Rubber-stamp voting: community given no meaningful window |
| **Vote → Deploy** | Was there review time between approval and deployment? | Rushed deployment: no safety window for objections |

- **Check:** Timestamps for LIP-23 (Negative rebase sanity check) and LIP-25 (Staking Router 2.0).
- **Status:** NOT YET ANALYZED. Priority investigation item.
- **Why it matters:** If code was ready before public discussion → governance may be pro-forma ratification, not actual decision-making.

### Release History
- **Check:** All tagged releases — who created, who signed, pattern over time.
- **Found (single data point):** v2.1.0 released by one actor, GPG-signed.
- **Open question:** Is this consistent across 3-5 prior releases? One release ≠ pattern.
- **Confidence:** Low — insufficient for pattern claim.

### Deleted History
- **Check:** Force push events, branch deletions, timeline gaps.
- **Found:** No evidence of manipulation. Low concern so far.

---

## Contradiction Mode

### Governance-Code Divergence
- **Check:** Research Lido forum proposals vs. actual code. Inactive branches for ghost features.
- **Known:** Refactoring disclaimer in core — old guides mismatch reality. V2 improved alignment but persistent gap between DAO governance rhetoric and operational centralization.
- **Confidence:** Medium — requires systematic LM-assisted comparison for GCDS scoring.

### Invisible Fork Detection
- **Check:** Mega-commits (large code blocks without incremental PR history), activity pauses followed by sudden complete implementations, PR comments referencing off-platform decisions.
- **Status:** NOT YET ANALYZED.

---

## Three Focal Pain Points

### A. Deposit Security Module (DSM)
- **Question:** Who controls the repository code for guardian key management?
- **Required:** Merge authority topology on DSM-related code. Permission bridge to on-chain guardian addresses.

### B. Exit Bus Factor
- **Question:** How many people can independently maintain withdrawal/exit logic?
- **Required:** git blame on WithdrawalQueue.sol, ValidatorExitBus.sol. Nakamoto Dev Coefficient for critical path.

### C. LDO vs Code Divergence
- **Question:** What was promised on Research Lido forum vs. what exists in active/inactive branches?
- **Required:** GCDS calculation with three sub-components (procedural, semantic, timing).

---

## Composite Scores

**Not yet scored.** Provisional signal only — insufficient quantitative data for composite metrics.

This checklist documents scope and gaps. It MUST NOT be used as standalone governance risk scoring.

Full scoring requires:
- Complete PR dataset (not 8-PR sample)
- CODEOWNERS formal authority mapping
- git blame authorship distribution (merge ≠ authorship)
- On-chain overlap analysis (code control may ≠ governance control)
- Release history depth (1 release ≠ pattern)
- Governance latency data (all 3 types)
- Foundation infrastructure control assessment

---

## Public / Private Layer Boundary

### Published (this repository)
- Merge concentration signal (anonymized actors)
- Review concentration signal
- Contributor Gini evolution
- Investigation scope and gaps
- Methodology references

### Available under engagement
- Identity mapping (GitHub → on-chain addresses)
- On-chain overlap analysis (multisig, Easy Track, DSM)
- Governance latency forensic timeline
- Semantic divergence analysis (forum vs. code)
- Guardian key control tracing
- Cross-repo control graph
- CI/CD and infrastructure ownership
- Foundation residual control assessment
- Scored GCM, GCDS, POCI, GMI, ECI

> Deep forensic audit available upon request.

---

## Preliminary Evidence

See: [Lido GitHub Governance Evidence (Public Layer)](evidence/github-evidence-public.md)

---

*Methodology: [GitHub Forensic Layer v2.0](../../methodology/GitHub-Forensic-Layer-v2.0.md) | COSMODROME*
