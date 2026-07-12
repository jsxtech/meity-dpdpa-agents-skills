---
version: "1.2"
last_updated: "2026-04-30"
dpdp_rules_version: "notified-2025"
domain: "AI/ML & Data Ethics"
type: "skill"
---

# DPDP AI/ML & Data Ethics Skill

## Skill Identity

**Skill Name:** dpdp-ai-ml-ethics
**Domain:** Artificial Intelligence, Machine Learning, Automated Decision-Making, Algorithmic Accountability
**Skill Type:** Technical, Ethics, Compliance, Privacy Engineering
**Applicable To:** Data Scientists, ML Engineers, AI Product Managers, DPOs, Legal Teams, Ethics Boards

---

## Skill Purpose

Apply DPDP Act obligations and ethical data principles to AI/ML systems that process personal data. Address automated decision-making, profiling, bias, explainability, and algorithmic accountability — ensuring AI systems respect Data Principal rights and comply with India's privacy law.

---

## Why AI/ML Needs Special Attention Under DPDP

```
AI/ML DPDP RISK HOTSPOTS
─────────────────────────────────────────────────────────────
1. LARGE-SCALE PROCESSING
   ML models consume vast amounts of personal data for training.
   Triggers SDF designation risk; heightened obligations.

2. PROFILING
   AI builds detailed profiles of individuals —
   behaviour, preferences, creditworthiness, health risk.
   Requires specific consent; right to object.

3. AUTOMATED DECISIONS
   AI makes or influences decisions affecting individuals —
   loan approval, hiring, insurance pricing, content curation.
   Requires DPIA; right to explanation; human review.

4. CHILDREN'S DATA
   Profiling and targeting children is expressly PROHIBITED.
   Any AI that could reach children needs age gating.

5. DATA MINIMISATION TENSION
   ML models improve with more data.
   DPDP requires minimum necessary data.
   Tension must be resolved in favour of privacy.

6. RETENTION
   Training data and model artefacts may retain personal data
   beyond the original purpose retention period.

7. THIRD-PARTY DATA INGESTION
   Models trained on scraped or purchased data —
   provenance, consent, and legal basis must be established.
─────────────────────────────────────────────────────────────
```

---

## Skill Capabilities

---

### Capability 1: AI System Privacy Inventory

**Trigger:** "AI data inventory", "what personal data do our AI models use", "ML data audit"

**Steps:**
1. Inventory all AI/ML systems in production and development:

   ```
   AI SYSTEM INVENTORY
   ─────────────────────────────────────────────────────────
   System Name        : [e.g., Credit Risk Model v3]
   Purpose            : [e.g., Loan approval scoring]
   Model Type         : [Classification / Regression / GenAI / etc.]
   Training Data      : [Source, categories, volume, vintage]
   Inference Data     : [Real-time inputs — what personal data?]
   Output             : [Score / Decision / Recommendation / Content]
   Affects Individuals: [Y/N — how?]
   Automated Decision : [Fully automated / Human-in-loop / Advisory]
   Children's Data    : [Y/N]
   DPIA Conducted     : [Y/N — DPIA ID]
   Last Reviewed      : [Date]
   Owner              : [Team]
   ─────────────────────────────────────────────────────────
   ```

2. For each system, identify all personal data consumed:
   - Training data (historical personal data)
   - Feature inputs at inference time
   - Outputs that constitute personal data (scores, predictions, profiles)
3. Map to Data Principal categories affected.
4. Flag systems processing children's data.
5. Flag systems making automated decisions.

**Output:** AI System Privacy Inventory; risk-flagged systems list.

---

### Capability 2: AI DPIA (AI-Specific)

**Trigger:** "DPIA for AI", "AI privacy impact assessment", "ML model DPIA"

**AI-Specific DPIA Extensions** (in addition to standard DPIA):

```
AI DPIA ADDITIONAL ASSESSMENT AREAS
══════════════════════════════════════════════════════════════
1. TRAINING DATA ASSESSMENT
   □ What is the source of training data?
   □ Was personal data in training data collected with consent for model training?
   □ Does training data include sensitive categories?
   □ Does training data include children's data?
   □ Is the training data retention period defined?
   □ Can the model "memorise" individual training records (memorisation risk)?

2. FEATURE ENGINEERING ASSESSMENT
   □ What features are derived from personal data?
   □ Are proxy features used (e.g., postcode as proxy for race)?
   □ Can features indirectly reveal sensitive categories?
   □ Is each feature necessary for the model's purpose?

3. AUTOMATED DECISION ASSESSMENT
   □ Does the model make or significantly influence decisions about individuals?
   □ What are the possible outcomes (approve / reject / score / recommend)?
   □ What is the severity of impact on Data Principals (financial, employment, health)?
   □ Is human review available and meaningful (not just rubber-stamping)?
   □ Can the decision be explained to the individual?

4. BIAS & FAIRNESS ASSESSMENT
   □ Has the model been tested for bias across demographic groups?
   □ Does the model produce disparate impacts on protected groups?
   □ Is there a mechanism to detect and correct bias post-deployment?
   □ Who reviews bias audit findings?

5. EXPLAINABILITY ASSESSMENT
   □ Can the model's decision be explained in plain language?
   □ Are feature importance scores available?
   □ Can a Data Principal understand why a decision was made about them?
   □ Is the explanation method technically robust (not misleading)?

6. DATA MINIMISATION IN ML
   □ Is the training dataset the minimum needed for the stated purpose?
   □ Can the model be trained on anonymised or synthetic data?
   □ Can features be generalised (age range vs exact age)?
   □ Is transfer learning from a privacy-preserving base model possible?

7. MODEL LIFECYCLE PRIVACY
   □ Are model artefacts (weights, embeddings) treated as personal data?
   □ What is the retention period for trained models?
   □ When a model is decommissioned, is it deleted securely?
   □ Is model versioning tracked with associated data lineage?
══════════════════════════════════════════════════════════════
```

**Output:** AI-specific DPIA report with additional risk areas assessed.

---

### Capability 3: Automated Decision-Making Compliance

**Trigger:** "automated decisions DPDP", "right to explanation", "AI decision rights", "human review for AI"

**DPDP Obligations for Automated Decision-Making:**

Under the DPDP Act and emerging AI governance principles:
- Data Principals have the right to know that automated processing is occurring
- Significant automated decisions (credit, employment, insurance) require:
  - **Transparency** — individual must be informed
  - **Explainability** — meaningful explanation of the decision factors
  - **Human review** — right to request human reassessment
  - **Right to object** — consent withdrawal / objection mechanism

**Implementation Checklist:**
```
AUTOMATED DECISION COMPLIANCE
─────────────────────────────────────────────────────────────
□ Decision subject is notified that automated processing occurred
□ Plain-language explanation available for each decision outcome
□ Explanation identifies the primary factors influencing the decision
□ Human review process is available and accessible (not theoretical)
□ Human reviewer has authority to overturn the automated decision
□ Human reviewer is trained — not just rubber-stamping AI output
□ Right to object / appeal is communicated with the decision
□ Response time for human review appeal: [defined SLA]
□ Outcome of human review is communicated to Data Principal
□ Automated decisions not made solely on sensitive data without consent
□ Children never subject to fully automated decisions without parental review
```

**Output:** Automated decision compliance assessment; human review workflow design.

---

### Capability 4: Bias Audit

**Trigger:** "AI bias audit", "fairness assessment", "discriminatory AI", "algorithmic bias"

**Steps:**
1. Define **protected attributes** relevant to the model's context:
   - Gender, age, religion, caste, region, language, disability status
   - Proxy attributes that correlate with protected characteristics

2. Run **bias metrics** across population subgroups:

   | Metric | Definition | Acceptable Threshold |
   |---|---|---|
   | Demographic Parity | Equal positive outcome rate across groups | < 10% differential |
   | Equal Opportunity | Equal true positive rate across groups | < 10% differential |
   | Predictive Parity | Equal precision across groups | < 10% differential |
   | Individual Fairness | Similar individuals receive similar outcomes | Case review |
   | Counterfactual Fairness | Same outcome if only protected attr changes | Policy decision |

3. Document bias findings for each subgroup.
4. Identify **root cause** of bias:
   - Historical bias in training data
   - Representation bias (underrepresentation of subgroup in training data)
   - Measurement bias (proxy features capturing protected attributes)
   - Aggregation bias (one model for heterogeneous groups)

5. Implement **bias mitigation**:
   - Pre-processing: re-sample training data; remove proxy features
   - In-processing: fairness constraints in training objective
   - Post-processing: threshold adjustment per subgroup

6. Re-run metrics after mitigation.
7. Document and report to DPO and senior management.
8. Schedule periodic bias re-audits (at minimum annually, or when data drifts).

**Output:** Bias audit report; mitigation plan; re-audit schedule.

---

### Capability 5: AI Data Minimisation

**Trigger:** "data minimisation for ML", "reduce personal data in AI", "privacy-preserving ML"

**Techniques:**

```
DATA MINIMISATION TECHNIQUES FOR AI/ML
══════════════════════════════════════════════════════════════
1. FEATURE SELECTION
   Remove features that are not predictive — reduces data collection
   Remove features that are proxies for sensitive attributes

2. GENERALISATION / AGGREGATION
   Age bucket (18–25) instead of exact birth date
   City instead of precise address
   Income range instead of exact salary

3. ANONYMISATION OF TRAINING DATA
   Use anonymised historical data for model training
   Differential privacy — add calibrated noise to training data
   K-anonymity — ensure each record is indistinguishable from k-1 others

4. SYNTHETIC DATA GENERATION
   Generate synthetic training data statistically similar to real data
   Validate synthetic data utility before replacing real data
   Retains statistical patterns without personal data

5. FEDERATED LEARNING
   Train model locally on user devices — raw data never leaves the device
   Only model updates (gradients) are shared — not personal data
   Suitable for mobile/IoT use cases

6. TRANSFER LEARNING
   Fine-tune a pre-trained model with minimal personal data
   Base model trained on public / anonymised data

7. ON-DEVICE PROCESSING
   Run inference on-device — personal data never sent to server
   Reduce data ingestion to aggregated signals only

8. PSEUDONYMISATION OF TRAINING PIPELINE
   Replace direct identifiers with pseudonymous IDs in training data
   Separate key management — key not accessible to model training team
══════════════════════════════════════════════════════════════
```

**Output:** Data minimisation assessment; technique recommendations; implementation plan.

---

### Capability 6: AI Training Data Governance

**Trigger:** "AI training data compliance", "is our training data DPDP compliant", "training data legal basis"

**Steps:**
1. For each training dataset, establish:

   ```
   TRAINING DATA LEGAL BASIS ASSESSMENT
   ─────────────────────────────────────────────────────────
   Dataset Name        : [e.g., Customer Transaction History]
   Original Collection : [Purpose at time of collection]
   Consent Obtained For: [Purpose stated in consent]
   Training Purpose    : [e.g., Fraud detection model]

   Is training the same purpose as original collection?
     YES → existing consent covers training (verify consent language)
     NO  → fresh consent required OR anonymise data before training
   ─────────────────────────────────────────────────────────
   ```

2. For **third-party / scraped / purchased data**:
   - Verify the data provider's legal basis for collection
   - Verify consent covered secondary use (model training)
   - Verify no children's data present
   - Obtain indemnification from data provider for DPDP compliance

3. Implement **training data retention policy**:
   - Training datasets retained only as long as needed for model development
   - Production model snapshots — defined retention (e.g., retain current + 2 previous versions)
   - Deleted training data → retrain affected models if necessary

4. Implement **training data access controls**:
   - Data science team access — need-to-know, logged
   - No raw training data in development / test environments without masking
   - Vendor / cloud ML platform access — DPA required

**Output:** Training data legal basis register; retention policy; access controls.

---

### Capability 7: Generative AI (GenAI) Compliance

**Trigger:** "generative AI DPDP", "ChatGPT compliance", "LLM privacy", "GenAI data protection"

**Specific GenAI Risks:**

```
GENERATIVE AI DPDP RISK AREAS
══════════════════════════════════════════════════════════════
1. TRAINING DATA MEMORISATION
   LLMs can reproduce verbatim training data including personal data.
   Risk: model outputs personal data of individuals without consent.
   Mitigation: PII scrubbing of training data; output filtering.

2. PROMPT INJECTION OF PERSONAL DATA
   Users input personal data (their own or others') into prompts.
   Risk: data retained by vendor; used to train future models.
   Mitigation: DPA with GenAI vendor; data retention controls; user guidance.

3. THIRD-PARTY GenAI VENDORS
   Using OpenAI, Google Gemini, Anthropic, etc. via API.
   Risk: personal data sent to overseas vendor.
   Mitigation: DPDP cross-border transfer assessment; DPA; data processing controls.

4. AI-GENERATED PERSONAL DATA
   GenAI can produce realistic but false personal data (hallucination).
   Risk: false personal data about real individuals; defamation; wrong decisions.
   Mitigation: human review; source grounding; confidence thresholds.

5. EMPLOYEE USE OF PUBLIC GenAI
   Employees paste confidential customer data into ChatGPT / Gemini.
   Risk: personal data processed by third party without consent; breach.
   Mitigation: policy; DLP controls; approved GenAI tools list.

6. SYNTHETIC PERSONAL DATA GENERATION
   GenAI used to create synthetic training data.
   Risk: synthetic data may still be linkable to real individuals.
   Mitigation: re-identification risk assessment before use.
══════════════════════════════════════════════════════════════
```

**GenAI Compliance Checklist:**
```
□ GenAI vendor DPA executed — DPDP obligations flowed down
□ Cross-border transfer to GenAI vendor assessed and permissible
□ Training data opt-out negotiated with vendor (data not used to train models)
□ PII scrubbing applied to prompts before API calls
□ Output filtering for personal data implemented
□ Employee policy on public GenAI tools published
□ DLP controls block paste of customer data to non-approved GenAI
□ DPIA conducted for GenAI-powered features
□ Hallucination risk — human review for outputs affecting individuals
□ Children's data never submitted to GenAI systems
```

**Output:** GenAI risk assessment; vendor DPA checklist; employee policy; DLP controls.

---

### Capability 8: Algorithm Register & Accountability

**Trigger:** "algorithm register", "AI accountability", "algorithmic transparency", "AI governance"

**Algorithm Register Schema:**

```
ALGORITHM REGISTER
═══════════════════════════════════════════════════════════════
Algorithm ID        : ALG-001
Name                : Customer Credit Risk Scorer
Version             : v4.2
Owner               : Risk Analytics Team
Deploy Date         : 2024-08-01
Last Reviewed       : 2025-03-01
Next Review         : 2026-03-01

PURPOSE
  Business Purpose  : Automated loan approval decision support
  DPDP Legal Basis  : Consent (loan application consent form v3.1)

DATA INPUTS
  Training Data     : 36-month transaction history, bureau data
  Inference Inputs  : Applicant transaction data, income, bureau score
  Sensitive Data?   : Y — financial data (Tier 1)
  Children's Data?  : N — age 21+ applicants only

OUTPUTS
  Output Type       : Risk score (0–1000) + Approve/Review/Decline
  Decision Impact   : High — affects loan approval and interest rate

AUTOMATION LEVEL
  Level             : Semi-automated (human review for Decline)
  Human Review      : Loan officer reviews all Decline outcomes
  Explanation       : Top 3 factors provided to applicant on Decline

RISK ASSESSMENT
  DPIA Conducted    : Y — DPIA-012 (2024-07-15)
  Residual Risk     : Medium
  Bias Audit        : Y — Last audit 2025-01-10 — Pass

PERFORMANCE
  Accuracy          : 94.2% (validation set)
  Fairness Metric   : Demographic parity across gender — 3.1% differential (within threshold)
  Drift Monitoring  : Monthly data drift alerts configured

EXPLAINABILITY
  Method            : SHAP values
  Explanation Format: Plain language top-3 factors
  Audit Log         : All decisions logged with feature importances

COMPLIANCE
  Bias Audit Passed : Y
  DPIA Approved     : Y
  DPO Sign-off      : Y — [DPO Name] — 2024-07-20
  Automated Decision Notice to Applicants: Y (in loan application form)
  Human Review Process: Y — documented in lending policy
═══════════════════════════════════════════════════════════════
```

**Output:** Populated Algorithm Register; governance sign-offs documented.

---

## Related Skills

- `dpdp-privacy-by-design-skill.md` — AI privacy engineering
- `dpdp-privacy-risk-management-skill.md` — AI risk assessment
- `dpdp-children-data-skill.md` — AI and children prohibition

---

## Skill Guardrails

- **Never deploy** an AI system processing personal data without a DPIA.
- **Never allow** fully automated high-impact decisions without human review.
- **Never use** children's data for profiling or targeting — in any AI system.
- **Never train** models on data collected for a different purpose without re-consent or anonymisation.
- **Always audit** for bias before deployment and annually thereafter.
- **Always maintain** an explainability mechanism for decisions affecting individuals.
- **Always run** a cross-border transfer assessment before using overseas GenAI APIs with personal data.

---

## Quick Commands

| Command | Action |
|---|---|
| `/ai-inventory` | Build AI system privacy inventory |
| `/ai-dpia` | Conduct AI-specific DPIA |
| `/ai-decisions` | Assess automated decision-making compliance |
| `/ai-bias-audit` | Run bias audit on AI model |
| `/ai-minimisation` | Apply data minimisation to ML pipeline |
| `/ai-training-data` | Assess training data legal basis |
| `/genai-compliance` | GenAI vendor and usage compliance check |
| `/algorithm-register` | Build and maintain Algorithm Register |

---

## References

- DPDP Act, 2023 — Sections 8–10
- MeITY DPDP Rules, 2025 (Notified)
- MeITY Responsible AI Framework (India)
- NITI Aayog — Responsible AI for All
- EU AI Act (comparative reference for high-risk AI systems)
- IEEE P7000 — Ethically Aligned Design
- NIST AI Risk Management Framework (AI RMF)
- Fairlearn, IBM AI Fairness 360 — bias audit toolkits
