# Authority System Manual

This folder is a complete operating system for selling and delivering the **PRISM Authority Sprint**.

## What This System Includes

- `positioning-kit.md`  
  Your final positioning, narrative, market gap, and messaging foundation.

- `landing-page-copy.md`  
  Exact copy for a conversion-focused landing page.

- `offer-deck.md`  
  Slide-by-slide script for discovery or pitch meetings.

- `outbound-scripts.md`  
  LinkedIn + email + follow-up scripts to book qualified calls.

- `sales-operating-system.md`  
  Qualification rubric, discovery call flow, objection handling, and close process.

- `fulfillment-sop.md`  
  21-day delivery workflow to produce consistent client outcomes.

- `content-engine.md`  
  Content pillars and 30-day publishing plan to compound authority.

- `launch-checklist.md`  
  End-to-end prelaunch checklist to make the system operational.

- `config.example.json`  
  Personalization config for generating a customized launch pack.

- `system_builder.py`  
  Script that injects your details into templates and creates deploy-ready files.

- `templates/proposal-template.md`  
  Proposal template to convert calls into signed deals.

- `templates/client-intake-form.md`  
  Pre-kickoff questionnaire for faster delivery and stronger outcomes.

- `tracking/pipeline-scorecard.csv`  
  Lightweight tracking sheet for outreach, calls, proposals, and wins.

## Generate Your Personalized Launch Pack

1. Copy `config.example.json` and update values.
2. Run:

```bash
python3 authority-system/system_builder.py \
  --config authority-system/config.example.json \
  --output authority-system/output
```

3. Open `authority-system/output/BUILD_SUMMARY.md` to review unresolved placeholders.

## 14-Day Launch Plan

### Days 1-2: Finalize Foundation
- Personalize `positioning-kit.md` with your niche examples.
- Lock your primary ICP and offer price.

### Days 3-4: Publish Offer
- Publish `landing-page-copy.md` on your website or Notion page.
- Add booking link and calendar availability.

### Days 5-6: Prepare Sales Assets
- Build your presentation from `offer-deck.md`.
- Duplicate and customize `templates/proposal-template.md`.

### Days 7-14: Run Daily Pipeline
- Send outbound using `outbound-scripts.md`.
- Run calls via `sales-operating-system.md`.
- Track everything in `tracking/pipeline-scorecard.csv`.

## Weekly Cadence

- Monday: ICP list + personalization prep
- Tuesday-Thursday: outbound and follow-ups
- Friday: calls, proposals, KPI review
- Saturday: publish one authority case or breakdown post

## Success Benchmarks (First 30 Days)

- 150-250 outbound touches
- 12-20 qualified conversations
- 5-8 proposal opportunities
- 2-4 paid clients
