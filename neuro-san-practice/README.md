\# Argonaut — AI Maritime Voyage Decision System



> \*\*An agentic AI decision system that evaluates maritime voyage risk, economics, insurance, charter obligations, and customer impact to recommend whether a vessel should transit or reroute.\*\*



\## Overview



Maritime voyage decisions often require information from multiple domains at the same time:



\- Security and corridor threats

\- War-risk insurance

\- Route economics

\- Charter-party obligations

\- Customer delivery penalties

\- Financial trade-offs

\- Independent challenge of the proposed decision



\*\*Argonaut\*\* brings these perspectives together through a multi-agent AI workflow.



Instead of asking one AI model to make the entire decision, Argonaut assigns specialized responsibilities to multiple agents and then combines their findings through a deterministic decision calculation.



The result is an explainable \*\*TRANSIT or REROUTE\*\* recommendation with:



\- Key financial numbers

\- Threat probability

\- Confidence score

\- Break-even conditions

\- A final red-team challenge



\---



\# The Problem



A maritime operator may need to decide:



> \*\*Should this vessel continue through a potentially dangerous corridor or take a longer diversion?\*\*



The answer cannot be based on security risk alone.



A decision may depend on:



\- Probability of an incident

\- War-risk insurance premium

\- Additional sailing days

\- Additional fuel/route cost

\- Customer delivery penalties

\- Charter-party clauses

\- Crew rights and operational constraints

\- Quality and freshness of available intelligence



A simple chatbot response is not sufficient for this type of decision.



Argonaut is designed as a \*\*decision-support workflow\*\*, where specialized agents independently analyze different dimensions before a final recommendation is produced.



\---



\# Solution



Argonaut uses a multi-agent architecture:



```text

&#x20;                        ┌─────────────────────┐

&#x20;                        │ Voyage\_Commander     │

&#x20;                        │   Orchestrator       │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;             ┌─────────────────────┼─────────────────────┐

&#x20;             │                     │                     │

&#x20;             ▼                     ▼                     ▼

&#x20;      ┌─────────────┐       ┌─────────────┐       ┌─────────────┐

&#x20;      │   Sentinel  │       │    Broker   │       │  Helmsman   │

&#x20;      │ Security    │       │ Insurance   │       │ Route/Econ. │

&#x20;      └──────┬──────┘       └──────┬──────┘       └──────┬──────┘

&#x20;             │                     │                     │

&#x20;             └─────────────────────┼─────────────────────┘

&#x20;                                   │

&#x20;                        ┌──────────┴──────────┐

&#x20;                        │                     │

&#x20;                        ▼                     ▼

&#x20;                 ┌─────────────┐       ┌─────────────┐

&#x20;                 │   Counsel   │       │    Ledger   │

&#x20;                 │  Charter    │       │  Customer   │

&#x20;                 │ Constraints │       │   Impact    │

&#x20;                 └──────┬──────┘       └──────┬──────┘

&#x20;                        │                     │

&#x20;                        └──────────┬──────────┘

&#x20;                                   │

&#x20;                                   ▼

&#x20;                           ┌─────────────┐

&#x20;                           │   Skeptic   │

&#x20;                           │ Red-Team    │

&#x20;                           └──────┬──────┘

&#x20;                                  │

&#x20;                                  ▼

&#x20;                          ┌────────────────┐

&#x20;                          │ decision\_math  │

&#x20;                          │ Deterministic  │

&#x20;                          │ Calculation    │

&#x20;                          └───────┬────────┘

&#x20;                                  │

&#x20;                                  ▼

&#x20;                        ┌─────────────────────┐

&#x20;                        │ Voyage\_Commander    │

&#x20;                        │ Final Decision      │

&#x20;                        └─────────────────────┘

```



\---



\# Agents



\## Voyage\_Commander



The front-facing orchestrator.



Responsibilities:



\- Collect required voyage inputs

\- Coordinate specialist agents

\- Ensure specialist findings are explicitly passed between stages

\- Trigger the red-team review

\- Run deterministic decision calculations

\- Produce the final voyage decision brief



\---



\## Sentinel



\*\*Security and threat intelligence specialist\*\*



Analyzes the selected maritime corridor.



Provides:



\- Threat level

\- Threat probability

\- Incident age

\- JWC listing status

\- Threat intelligence warning



\---



\## Broker



\*\*War-risk insurance specialist\*\*



Calculates an illustrative insurance premium based on:



\- Cargo value

\- Threat level

\- Vessel class

\- Corridor



\---



\## Helmsman



\*\*Route and voyage economics specialist\*\*



Evaluates the diversion.



Provides:



\- Additional sailing days

\- Additional reroute cost

\- Route economics



\---



\## Counsel



\*\*Charter-party specialist\*\*



Reviews charter-specific constraints.



Considers:



\- War-risk clauses

\- Safe-port warranties

\- AIS requirements

\- Crew rights



\---



\## Ledger



\*\*Customer and financial impact specialist\*\*



Evaluates customer consequences such as:



\- Delivery-window requirements

\- Late-delivery penalties

\- Contractual financial exposure



\---



\## Skeptic



\*\*Independent red-team reviewer\*\*



Argonaut does not allow the final recommendation to pass without challenge.



Skeptic reviews the collected specialist findings and identifies \*\*exactly one material weakness\*\*, such as:



\- Stale threat intelligence

\- Unsupported assumptions

\- Inconsistent numbers

\- Missing information

\- Dependencies between findings



This creates an explicit challenge layer before the final decision.



\---



\# Deterministic Decision Layer



The final recommendation is not based purely on an LLM-generated opinion.



Argonaut passes the collected evidence into `decision\_math`.



The calculation compares the expected cost of continuing through the corridor against the cost of rerouting.



Conceptually:



```text

Transit Expected Cost

&#x20;       vs.

Reroute Cost

```



The system also calculates:



\- Expected cost difference

\- Financial margin

\- Insurance break-even point

\- Reroute-cost break-even point

\- Customer-penalty break-even point

\- Confidence



This makes the final recommendation auditable and explainable.



\---



\# Example Decision



\## Scenario



```text

Vessel: Ocean Pioneer

Vessel Class: VLCC

Cargo: Crude Oil

Cargo Value: $120M

Direct Route: Red Sea / Bab-el-Mandeb via Suez Canal

Diversion: Cape of Good Hope

Customer: CUST-001

Charter: Time Charter

```



\### Specialist Findings



\*\*Sentinel\*\*



```text

Threat Level: Elevated

Threat Probability: 31%

Incident Age: 9 days

JWC Listed: Yes

```



\*\*Broker\*\*



```text

Insurance Premium: $1,080,000

```



\*\*Helmsman\*\*



```text

Additional Days: 10

Reroute Cost: $884,000

```



\*\*Ledger\*\*



```text

Customer Penalty: $1,000,000

```



\### Deterministic Calculation



```text

Transit Expected Cost: $1,414,800

Reroute Cost:          $1,884,000



Financial Advantage:   $469,200

```



\### Final Decision



```text

RECOMMENDATION: TRANSIT



Confidence: 74.9%

```



\### Red-Team Challenge



```text

Stale threat data:

incident data is 9 days old,

exceeding the 7-day freshness threshold.

```



This demonstrates an important property of Argonaut:



> \*\*The system can recommend a financially preferable action while explicitly exposing the weakness that could invalidate the decision.\*\*



\---



\# Opposite Decision Scenario



Argonaut can also produce a different decision when the threat and economics change.



Example:



```text

Direct Route: Strait of Hormuz

Diversion:    Strait of Malacca



Threat:       54%

Insurance:    $3.6M

Reroute Cost: $884K

```



The deterministic decision layer recommends:



```text

RECOMMENDATION: REROUTE



Confidence: 95%

```



This demonstrates that Argonaut is not hard-coded to always recommend rerouting.



The recommendation changes based on the collected evidence and deterministic calculations.



\---



\# Input Validation



Argonaut validates required voyage information before starting the specialist workflow.



Required inputs:



```text

Vessel Class

Cargo Value

Direct Route

Diversion Route

Customer Reference

Charter Type

```



If required information is missing, the system stops before invoking specialist agents.



Example:



```text

I'm missing one required field to begin the assessment:



Charter type

```



This prevents the system from producing a decision from incomplete voyage information.



\---



\# General Question Handling



Argonaut is also designed to distinguish between:



\### Voyage decision requests



These trigger the multi-agent workflow.



\### General maritime questions



These can be answered directly without unnecessarily launching the full specialist workflow.



For example:



```text

"What is the difference between Time Charter and Voyage Charter?"

```



does not require a complete voyage-risk assessment.



This helps prevent unnecessary agent execution.



\---



\# Technology Stack



\- \*\*Neuro SAN / neuro-san\*\*

\- Python

\- HOCON agent configuration

\- NVIDIA hosted LLM

\- Coded Tools

\- Multi-agent orchestration

\- Deterministic decision calculations



Current model configuration:



```text

nvidia/nemotron-3-super-120b-a12b

```



\---



\# Coded Tools



Argonaut uses deterministic coded tools for domain calculations and lookups.



```text

zone\_threat\_lookup

&#x20;       │

&#x20;       └── Synthetic corridor threat intelligence



war\_risk\_pricing

&#x20;       │

&#x20;       └── Illustrative war-risk insurance calculation



voyage\_economics

&#x20;       │

&#x20;       └── Diversion economics



charter\_clause\_lookup

&#x20;       │

&#x20;       └── Charter-party clause lookup



customer\_contract\_lookup

&#x20;       │

&#x20;       └── Customer contractual impact



decision\_math

&#x20;       │

&#x20;       └── Deterministic final cost comparison

```



The architecture intentionally separates:



\*\*AI reasoning → domain evidence → deterministic calculation → final explanation\*\*



\---



\# Why Multi-Agent?



A single general-purpose agent could attempt to solve the entire problem, but that creates several risks:



\- Mixed responsibilities

\- Hidden assumptions

\- Difficult debugging

\- Poor explainability

\- Harder validation



Argonaut instead gives each agent a clearly defined responsibility.



```text

Security

Insurance

Route Economics

Charter

Customer Impact

&#x20;       ↓

Independent Review

&#x20;       ↓

Deterministic Calculation

&#x20;       ↓

Decision

```



This makes the workflow easier to understand, test, and extend.



\---



\# Why the Skeptic Agent?



The Skeptic is intentionally placed immediately before the final calculation.



Its job is not to make another recommendation.



Its job is to ask:



> \*\*"What is the biggest weakness in the evidence supporting this decision?"\*\*



This adds a red-team layer to the decision process.



\---



\# Demo Flow



A typical demonstration follows this sequence:



```text

1\. Enter voyage scenario



2\. Voyage\_Commander validates inputs



3\. Sentinel evaluates corridor risk



4\. Broker calculates insurance exposure



5\. Helmsman evaluates rerouting economics



6\. Counsel evaluates charter constraints



7\. Ledger evaluates customer impact



8\. Skeptic identifies one material weakness



9\. decision\_math performs deterministic comparison



10\. Voyage\_Commander produces final decision brief

```



\---



\# Production Considerations



The current implementation is a \*\*hackathon demonstration and decision-support prototype\*\*.



Several components intentionally use synthetic data.



In a production implementation, these could be replaced with:



\- Live maritime threat intelligence

\- Current war-risk insurance quotes

\- AIS data

\- Weather and routing data

\- Real charter-party documents

\- Customer contract systems

\- Real-time voyage economics

\- Human approval workflows



Argonaut should therefore be treated as a \*\*decision-support system\*\*, not an autonomous replacement for maritime operators, legal professionals, insurers, or security teams.



\---



\# Project Structure



```text

neuro-san-practice/

│

├── config/

│   └── llm\_config.hocon

│

├── registries/

│   ├── manifest.hocon

│   └── argonaut.hocon

│

├── coded\_tools/

│   └── argonaut/

│       ├── zone\_threat.py

│       ├── war\_risk\_pricing.py

│       ├── voyage\_economics.py

│       ├── charter\_clauses.py

│       ├── customer\_contract.py

│       └── decision\_math.py

│

├── .gitignore

└── README.md

```



\---



\# Running Argonaut



Create and activate the Python environment:



```powershell

.venv\\Scripts\\activate

```



Start Neuro SAN:



```powershell

ns run

```



Open the Neuro SAN Studio interface and select:



```text

argonaut

```



Then provide a voyage scenario containing all required inputs.



\---



\# Key Design Principles



\### 1. Specialized agents



Each agent has one clear responsibility.



\### 2. Explicit evidence passing



Specialist findings are explicitly passed to downstream agents rather than relying on conversational memory.



\### 3. Deterministic calculations



Critical financial comparisons are performed by coded logic.



\### 4. Red-team review



The Skeptic challenges the evidence before the final recommendation.



\### 5. Explainable decisions



The final response exposes the major numbers and break-even conditions.



\### 6. Graceful validation



Incomplete scenarios are rejected before unnecessary specialist execution.



\---



\# Hackathon Summary



\*\*Argonaut\*\* demonstrates how agentic AI can be used to coordinate specialized reasoning across a complex business decision.



Instead of building another generic chatbot, Argonaut focuses on a high-impact decision problem:



> \*\*How should a maritime operator balance security risk, insurance exposure, route economics, contractual obligations, and customer impact when choosing between transit and rerouting?\*\*



The goal is not simply to generate an answer.



The goal is to produce a \*\*structured, challenged, explainable decision.\*\*



\---



\## Disclaimer



Argonaut is a hackathon prototype.



Threat intelligence, insurance pricing, contractual clauses, and other domain information used in the demonstration may be synthetic or illustrative and must not be treated as real-world operational advice.



Production deployment would require validated data sources, domain-specific controls, human oversight, and appropriate legal and operational review.

