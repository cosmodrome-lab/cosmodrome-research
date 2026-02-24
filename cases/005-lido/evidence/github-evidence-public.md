# Case #005: Lido — GitHub Governance Evidence (Public Layer)

> **Protocol:** Lido (lidofinance/core)  
> **Date:** February 2026  
> **Methodology:** COSMODROME GitHub Forensic Layer v2.0  
> **Status:** Preliminary signal from limited sample. Quantitative validation pending.

This file documents GitHub-based governance evidence and is not a substitute for on-chain or legal records. GitHub handles are technical identifiers, not verified legal identities.

---

## Evidence Integrity

| Parameter | Value |
|-----------|-------|
| Snapshot date | 2026-02-24 UTC |
| Source | Public GitHub UI, PR pages, release pages |
| Sample | 8 merged PRs (Mar-Oct 2025), 1 tagged release |
| Method | Manual observation, no API automation |
| Reproducibility | Any party with GitHub access can verify |

---

## Observed Patterns

### Merge Flow

**Signal:** From 8 sampled merged PRs, a consistent routing pattern was observed in 6 of 8 cases: Contributor submits → Actor B reviews/approves → Actor A merges and deletes branch. In 2 cases, Actor C self-merged after Actor B's approval.

**Interpretation hypothesis:** Potential merge-review bottleneck centered around two actors.

**Benign explanation:** Many mature open-source projects use a dedicated maintainer model where a small group handles merge authority by design. This is standard practice in projects like Linux kernel, Kubernetes, and most security-critical codebases. Concentration becomes a governance concern only when combined with on-chain control overlap, low transparency, or lack of succession planning.

### Review Routing

**Signal:** Actor B appeared as reviewer on all 8 sampled PRs. Actor B also requested reviews from others and published the most recent tagged release.

**Interpretation hypothesis:** Single-reviewer dependency for quality/security gatekeeping.

**Benign explanation:** Specialized review authority is common in security-sensitive codebases. A single expert reviewer may be the most qualified person. The question is whether this creates an unacceptable single point of failure.

### Contributor Structure

**Signal:** 52 contributors listed. Contributor Gini coefficient evolved from 0.686 (bootstrap) to 0.817 (maturity) per external research (not independently replicated). Member vs Contributor badge distinction observed.

**Interpretation hypothesis:** Increasing concentration over project lifetime.

**Benign explanation:** Gini increase during maturation is a known pattern in OSS projects as early contributors leave and core maintainers consolidate. Relevant question is trend direction, not absolute value.

### External Signal

**Signal:** Code4rena audit (2025-07-lido-finance) designates "Contributors of Lido Finance" as ineligible insiders.

**Interpretation hypothesis:** Bounded insider group recognized by external auditor.

**Benign explanation:** Standard audit conflict-of-interest clause. Present in most Code4rena audits regardless of team size.

---

## What These Patterns Suggest

> Evidence suggests an operational merge-review bottleneck centered around two actors. Quantitative validation pending.

This is a **signal**, not a **conclusion**. The signal warrants investigation of:

1. Full merge share distribution across all PRs (not 8-PR sample)
2. CODEOWNERS formal authority mapping (policy vs. emergent concentration)
3. Authorship vs. merge authority (git blame on critical contracts)
4. On-chain overlap (do code controllers also hold treasury/governance power?)
5. Release history depth (1 release is a data point, not a pattern)
6. Governance latency (was code ready before public discussion?)
7. Foundation infrastructure control (who admins GitHub org, npm, Docker?)

---

## Provisional Metrics

| Metric | Signal | Confidence | What Would Change It |
|--------|--------|-----------|---------------------|
| Top-1 Merge Share | >60% (sample) | LOW | Full data showing <50% weakens signal |
| Review Gatekeeper | Single actor on 8/8 PRs | MEDIUM | Full data showing <60% makes it moderate |
| Release Sovereignty | Single actor for v2.1.0 | LOW | Multiple publishers in prior releases breaks pattern |
| Bus Factor | Unknown | NOT MEASURED | Requires git blame |
| Nakamoto Dev Coeff. | Estimated ~2 | NOT CONFIRMED | Requires full PR/blame data |
| Governance Latency | Unknown | NOT MEASURED | Requires commit↔forum↔vote timeline |
| CODEOWNERS Match | Unknown | NOT MEASURED | Determines if concentration is formal policy or shadow authority |

**Provisional GCM: Not scored.** Insufficient data for composite metric.

---

## What a Full Investigation Adds

**Quantitative layer (automatable):**
- All merged PRs (2023-present): merge/review actor shares, Gini, Nakamoto coefficient
- git blame on critical contracts: bus factor per module, authorship concentration
- Full release history: tag creator and signer patterns
- Contributor email domain clustering
- CODEOWNERS formal authority mapping
- PR latency distribution

**Governance latency (3-type):**
- Commit → Forum (was code written before discussion?)
- Forum → Vote (was deliberation time real?)
- Vote → Deploy (was review window meaningful?)

**Cross-validation layer (semi-manual):**
- On-chain address mapping: multisigs, Easy Track, DSM guardians
- Sovereignty Overlap Matrix: code power × treasury power × vote power
- Forum proposal vs. code implementation fidelity (GCDS)
- Foundation infrastructure control assessment

**Interpretive layer (expert):**
- Stealth governance detection
- Off-platform coordination inference
- Trend analysis over 2+ years
- Scored GCM, GCDS, POCI, ECI

> Deep forensic audit available upon request.

---

## Data Freshness

All findings reflect publicly available data as of February 2026. GitHub data is dynamic. Any engagement-based report includes data refresh at investigation start.

---

*Methodology: [GitHub Forensic Layer v2.0](../../methodology/GitHub-Forensic-Layer-v2.0.md) | COSMODROME — We find what audits don't look for.*
