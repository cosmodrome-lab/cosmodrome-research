# COSMODROME Evidence Integrity Standards

**Version:** 1.0  
**Classification:** Public

---

## Purpose

Governance-relevant documents — multisig configurations, upgrade proposals, treasury disclosures, validator set registries — are routinely modified, moved, or deleted after initial publication. This has been observed across multiple protocols in our case registry.

COSMODROME evidence integrity standards exist to ensure that our analytical conclusions remain verifiable and auditable regardless of what happens to source documents after collection.

---

## SHA-256 Verification Protocol

Every primary source document collected during case research is:

1. **Downloaded** at the point of collection — we do not rely on live URLs for evidentiary claims
2. **Hashed** using SHA-256 at time of download
3. **Timestamped** — collection timestamp recorded alongside hash
4. **Cross-referenced** — where possible, against block height (for on-chain sources) or Git commit hash (for repository sources)
5. **Classified** by source tier (see Methodology, Section 2)

Hashes for all cited sources are included in the Evidence Appendix of each published case study.

---

## Custody Chain Requirements

For a source to be used as T1–T3 evidence in a published case study, it must satisfy:

- Hash recorded before analysis of that source is written
- Hash independently verifiable from the original source location (where still available)
- If source has disappeared: hash serves as the primary record; disappearance itself is noted as a Type C absence (see Methodology, Section 5)

---

## On-Chain Source Standards

On-chain sources are referenced by:
- Contract address (checksummed)
- Transaction hash (where applicable)
- Block number at time of observation
- Network identifier

We do not cite block explorer screenshots as evidence. We cite the underlying on-chain state.

---

## Git Source Standards

Repository sources are referenced by:
- Repository URL
- Commit hash (full, not abbreviated)
- File path within repository
- Timestamp of commit

Where a commit has been force-pushed or a repository has been made private after collection, this is classified as a Type C (Disappeared) or Type B (Closed by Design) absence event.

---

## What This Standard Does Not Cover

This document describes evidence handling for published COSMODROME case studies. It does not describe:
- Internal monitoring infrastructure
- Automated collection pipelines
- Unpublished research

---

*Evidence integrity is not a bureaucratic requirement. It is the difference between forensic intelligence and opinion.*
