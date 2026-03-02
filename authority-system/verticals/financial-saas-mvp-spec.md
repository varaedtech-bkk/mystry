# RevIntegrity Cloud - MVP Functional Spec

## Product Goal

Provide continuous, explainable reconciliation between SaaS billing systems and accounting ledgers, producing audit-ready finance outputs.

---

## 1) User Roles

- **Finance Admin:** configures rules, approvals, exports
- **Finance Analyst:** investigates mismatches, resolves tasks
- **Auditor (read-only):** reviews evidence trails and logs

---

## 2) Functional Modules

## A. Data Connectors

### Inputs
- Billing: Stripe, Chargebee (phase 1)
- Accounting: QuickBooks Online, Xero (phase 1)

### Functional Requirements
- OAuth/API credential setup
- Daily sync + manual refresh
- Sync health monitoring and error logs

---

## B. Canonical Revenue Model

Normalize the following entities:
- customer
- subscription
- invoice
- payment
- credit note
- plan/contract term
- ledger entry

Requirement:
- every normalized record stores source system ID + ingestion timestamp

---

## C. Reconciliation Engine

Core checks:
1. invoice total vs ledger posted total
2. payment posted vs cash entries
3. active subscriptions vs recognized revenue schedule
4. deferred revenue movement consistency

Each mismatch must include:
- severity (low/medium/high)
- suspected root cause
- recommended action
- linked source records

---

## D. Policy Engine (Rule-Based)

Support:
- configurable mapping rules (product -> account code)
- recognition timing templates
- override workflow with approval reason

Auditability:
- versioned rules
- who changed what and when

---

## E. Close Workspace

Views:
- open issues queue
- grouped by entity/account/period
- owner and due date

Actions:
- assign
- comment
- mark resolved
- attach evidence

---

## F. Audit Pack Export

One-click monthly export:
- unresolved/resolved mismatch log
- policy rule snapshot
- change history
- reconciliation summary by account and period

Formats:
- CSV + PDF bundle

---

## 3) Non-Functional Requirements

- Availability target: 99.5% (MVP)
- Data encryption in transit and at rest
- Full activity log for user actions
- Role-based access control

---

## 4) Suggested Data Model (Minimal)

Tables:
- `connections`
- `sync_jobs`
- `customers`
- `subscriptions`
- `invoices`
- `payments`
- `ledger_entries`
- `recon_issues`
- `policy_rules`
- `policy_rule_versions`
- `close_tasks`
- `audit_exports`
- `activity_logs`

---

## 5) MVP Screens

1. Connection setup
2. Reconciliation dashboard
3. Issue detail panel
4. Policy rule editor
5. Close workspace
6. Audit export center

---

## 6) 8-Week Build Plan

### Weeks 1-2
- connector foundation
- canonical model
- initial sync and logs

### Weeks 3-4
- reconciliation checks
- issue pipeline + severity model

### Weeks 5-6
- policy rules + versioning
- close workspace

### Weeks 7-8
- audit export
- hardening, QA, pilot onboarding

---

## 7) Pilot Success Metrics

- Close cycle time reduced by at least 20%
- Reconciliation error backlog reduced by at least 30%
- 90%+ of issues linked to clear root-cause category
- Audit prep package produced in under 30 minutes
