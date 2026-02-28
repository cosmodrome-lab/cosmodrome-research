# Governance Monitoring Infrastructure

COSMODROME operates an automated governance intelligence system that continuously monitors protocol repositories for changes in governance-critical components.

## Coverage

Five major DeFi protocols are currently under active monitoring:

- **Lido** — staking infrastructure, ~28% of staked ETH
- **Eigenlayer** — restaking infrastructure
- **MakerDAO** — lending and stablecoin infrastructure
- **Arbitrum** — Layer 2 governance
- **Optimism** — Layer 2 governance

## What We Track

The system monitors changes to files that control protocol governance:

- **CODEOWNERS** — who has merge authority over critical code
- **Access control contracts** — role assignments, permission changes
- **Multisig configurations** — signer additions, removals, threshold changes
- **Proxy and upgrade contracts** — implementation changes, upgrade patterns
- **Security policies** — incident response, disclosure procedures
- **Timelock parameters** — delay modifications, emergency bypass mechanisms

## How It Works

Scanning runs every three hours. Each detected change is captured with full metadata: author, timestamp, affected files, commit reference. Every finding receives a SHA-256 content hash at the moment of collection.

Once per week, all findings are aggregated, integrity-verified, and sealed into an evidence file. The sealed file contains a Merkle root computed over all individual findings — creating a cryptographic proof that no data was added, removed, or modified after the fact.

## Evidence Standards

This monitoring system feeds directly into COSMODROME forensic assessments. When we publish a case study stating that a protocol's CODEOWNERS file was modified on a specific date by a specific author — that claim is backed by:

1. Original finding captured within hours of the change
2. SHA-256 hash computed at capture time
3. Weekly sealed evidence file with Merkle root
4. Immutable record in the monitoring repository

This is the difference between forensic analysis and opinion.

## Access

Raw monitoring data and sealed evidence files are maintained in a private operational repository. Processed findings and verified evidence are incorporated into published case studies and client reports.

For monitoring inquiries: **cosmodrome-lab@proton.me**
