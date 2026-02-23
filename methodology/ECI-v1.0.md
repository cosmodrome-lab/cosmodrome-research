Выделяй всё от # до последней строки, копируй (Ctrl+C), вставляй в GitHub (Ctrl+V):
Effective Coordination Index (ECI) Framework v1.0
Overview
The Effective Coordination Index measures the real-world feasibility of collective action within a protocol's governance system. It answers a specific question: Can stakeholders actually coordinate to protect their interests when governance conditions change adversely?
ECI was developed during COSMODROME's forensic analysis of emergency governance mechanisms across major DeFi protocols (Arbitrum, Optimism, Maker/Sky).
The Coordination Problem
Many protocols declare protective mechanisms for token holders: veto rights, rage quit, exit windows, governance vetoes. On paper, these mechanisms exist. In practice, they require coordination — and coordination has costs.
ECI quantifies these costs across three dimensions:
1. Capital Barrier
What is the minimum capital required to activate the protection mechanism?

Quorum thresholds (absolute token amount or percentage)
Minimum stake requirements
Deposit or bonding requirements

Example: If a governance veto requires 10% of circulating supply to vote against, and top 5 holders control 40%, the remaining stakeholders must coordinate across thousands of addresses to reach threshold.
2. Time Barrier
How much time do stakeholders have to coordinate?

Proposal notice period
Voting window duration
Timelock before execution
Emergency bypass provisions (which may reduce time to zero)

Example: A 3-day voting window with a 2-day timelock gives stakeholders 5 days total. An emergency mechanism with no timelock gives zero days.
3. Information Barrier
Can stakeholders even know they need to act?

Proposal visibility (on-chain only vs. forum discussion vs. active notification)
Technical complexity of proposed changes
Obfuscation through parameter bundling
Language and documentation accessibility

ECI Calculation
ECI is expressed as a composite score from 0 to 100:

ECI 80-100: Coordination is feasible. Protection mechanisms are accessible to a broad stakeholder base with reasonable time and capital requirements.
ECI 50-79: Coordination is constrained. Protection mechanisms exist but require significant capital concentration or rapid response.
ECI 20-49: Coordination is impractical. Protection mechanisms are theoretically available but structurally inaccessible to most stakeholders.
ECI 0-19: Coordination is illusory. Declared protection mechanisms cannot be executed under realistic conditions.

Application to Emergency Governance
ECI was first applied to comparative analysis of emergency governance across three models:
ProtocolModelECI ScoreAssessmentArbitrumDistributed individual authority (Security Council)Moderate9/12 elected members can act unilaterally; broad mandate but accountable through electionsOptimismCentralized entity control (Optimism Foundation)LowSingle entity holds emergency powers; no on-chain stakeholder overrideMaker/SkyPlutocratic capital threshold (ESM)LowEmergency Shutdown requires 150,000 MKR (~$1.87B); effectively inaccessible
Limitations
ECI measures structural feasibility, not intent. A high ECI score means stakeholders can coordinate — not that they will. Behavioral factors (apathy, free-rider problem, information asymmetry) are acknowledged but not modeled.
ECI is designed for governance mechanisms with defined activation thresholds. It is less applicable to informal governance (social consensus, off-chain signaling).
Version History
VersionDateChangesv1.02025Initial framework - applied to Arbitrum, Optimism, Maker/Sky emergency governance comparison
COSMODROME - Effective Coordination Index v1.0
cosmodrome-lab@proton.me
