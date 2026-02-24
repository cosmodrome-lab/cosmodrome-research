# Case #005: Lido — GitHub Audit Checklist

> **Target:** github.com/lidofinance (245 repos, Feb 2026)  
> **Core repo:** lidofinance/core (468 stars, 267 forks)  
> **Key repos:** dual-governance, community-staking-module, easy-track  
> **Archetype:** Corporate-backed → Hybrid transition  
> **Methodology:** GitHub Forensic Layer v2.0  

---

## Structural Mode

### Declared Governance Layer

- **Check:** Scan all repos for GOVERNANCE.md, CONTRIBUTING.md, CODEOWNERS, security policies.
- **Known:** CONTRIBUTING.md in core (bug fixes, features, community). No explicit GOVERNANCE.md. Dual-governance repo (46 stars) covers contracts. DAO references in README only.
- **Assessment:** Medium confidence. Declared governance incomplete; gap between DAO rhetoric and documented development governance.

### Merge Authority Topology

- **Check:** PR merge history (merged_by), CODEOWNERS analysis, branch protection rules.
- **Known:** Merges concentrated (tamtamchik in recent PRs). Core group (~half contributors) = 98.1% activity. Hub-and-spoke network.
- **Assessment:** HIGH concentration. Single-digit maintainer group controls effectively all production merges.

### Development Concentration

- **Check:** Contributor Gini, Nakamoto coefficient, core/periphery split.
- **Known:** Gini: 0.686 (bootstrap) → 0.817 (maturity). 52 contributors, top-1 = 24%. Core dominates.
- **Assessment:** HIGH. Gini > 0.8 crosses threshold.

### Shadow Contributors

- **Check:** Email domain analysis across all repos. Filter bots. Cross-reference with known Lido team/investors.
- **Known:** No public domain analysis. Potential pseudonymous accounts.
- **Assessment:** REQUIRES INVESTIGATION. Priority task.

### Permission Bridge

- **Check:** Deploy scripts, migration files for hardcoded addresses → on-chain admin/owner addresses.
- **Known:** Core maintainers linked to DAO (Easy Track). Gap between dev centralization and DAO declarations.
- **Assessment:** HIGH value. Link GitHub maintainers → on-chain multisig signers.

### Dependency Analysis

- **Check:** package.json/yarn.lock, Snyk/npm audit.
- **Known:** TypeScript/Solidity, Hardhat ecosystem. Audit repo exists (Sigma Prime for V2).
- **Assessment:** Medium. Standard deps, periodic re-scan needed.

### Ghost Participation (GMI)

- **Check:** PR approval interaction graph. Rubber-stamp pattern detection.
- **Known:** Not yet analyzed.
- **Assessment:** REQUIRES INVESTIGATION.

---

## Temporal Mode

### Governance Change Log

- **Check:** Diff history on governance-related files, access control, emergency functions.
- **Known:** 9786 commits in core. Active Jan-Feb 2026.
- **Assessment:** HIGH data volume available.

### Governance Latency

- **Check:** Timestamp comparison: dual governance code commits vs. forum proposals vs. Snapshot votes.
- **Known:** Dual governance repo exists. Timeline not yet analyzed.
- **Assessment:** PRIORITY INVESTIGATION.

### Deleted History

- **Check:** Force push events, branch deletions, timeline gaps.
- **Known:** No evidence found.
- **Assessment:** Low concern. Continue monitoring.

### Release Control

- **Check:** Who tags versions, publishes packages, deploys contracts. CI/CD ownership.
- **Known:** Not yet analyzed.
- **Assessment:** REQUIRES INVESTIGATION.

---

## Contradiction Mode

### Governance-Code Divergence

- **Check:** Research Lido forum proposals vs. actual code. Inactive branches for ghost features.
- **Known:** Refactoring disclaimer in core — old guides mismatch. V2 improved, persistent gap.
- **Assessment:** Medium-High divergence expected. LM analysis needed.

### Invisible Fork Detection

- **Check:** Mega-commits, activity pauses, references to off-platform discussions.
- **Known:** Not yet analyzed.
- **Assessment:** REQUIRES INVESTIGATION.

---

## Three Focal Pain Points

### A. Lido DSM (Deposit Security Module)

- **Question:** Who controls the repository with guardian keys?
- **Analysis:** Merge Authority on DSM repo. Permission Bridge to on-chain guardians.
- **Expected:** Narrow control group for critical security module.

### B. Exit Bus Factor

- **Question:** How many people understand withdrawal/exit logic?
- **Analysis:** git blame on withdrawal and exit modules. Bus Factor calculation.
- **Expected:** Single-digit Bus Factor on critical exit infrastructure.

### C. LDO vs Code Divergence

- **Question:** What was promised on Research Lido vs. what exists in branches?
- **Analysis:** GCDS calculation. Abandoned features, scope changes, silent additions.
- **Expected:** Measurable divergence between declared roadmap and reality.

---

## Preliminary Composite Scores

| Metric | Score | Assessment |
|--------|-------|-----------|
| GCM | ~0.80 | HIGH: single-entity effective control territory |
| GCDS | ~0.65 (est.) | ELEVATED: persistent gap DAO rhetoric vs ops |
| POCI | ~0.80 (est.) | HIGH: pre-chain dev power concentrated |
| GMI | TBD | Requires PR approval graph analysis |

**Red Flag Escalation:** GCM > 0.7 and POCI > 0.6 — both thresholds exceeded. Report MUST include GitHub Governance Red Flags subsection.

---

*Methodology: GitHub Forensic Layer v2.0 | COSMODROME*
