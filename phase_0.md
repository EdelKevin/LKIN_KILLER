# Phase 0 — Style Extraction SOP

> **Trigger**: First-time setup, OR the candidate's resume changes (new role, new skill, new project), OR the operator says "rerun Phase 0".
> **Purpose**: Extract a candidate's voice + skill fingerprint from their resume so the Phase 1 tailoring pipeline can run against it.

---

## Input
- The candidate's current resume (PDF / Markdown / Word / pasted text)

## Output (4 files under `profile/`, overwrite on each run)

All Phase 0 artifacts live under `profile/` at the project root (gitignored).

- `profile/base_resume.md` — Markdown-ified source resume (operator's identity preserved as-is; `[REDACTED]` placeholders only if the operator explicitly opts in)
- `profile/style_profile.md` — voice + structure fingerprint + LOCKED hard facts + scale exemptions
- `profile/skill_inventory.md` — tech inventory + business problems demonstrated + coverage gaps + landing pads
- `profile/bullet_bank.md` — **reset to empty skeleton** (prior variants are invalid once the base changes)

---

## Steps

### 1. parse_resume(file)
- Parse into Markdown, split into sections: Header / Experience / Projects / Skills / Education
- Preserve `[REDACTED]` placeholders for PII only if the operator explicitly opts in; default is to keep real identity (per operator's user-profile memory)
- Write to `profile/base_resume.md`
- Verify with `python3 build_pdf.py profile/base_resume.md && python3 build_docx.py profile/base_resume.md` — output should render to a single page and visually match the source.

### 2. extract_hard_facts (LOCKED — Phase 1 never modifies these)
- `name`, `contact`, `current_location` (header city — the ONLY field Phase 1 may modify)
- `education`: `[{school, degree, dates, gpa?}]`
- `experience`: `[{company, title, dates, location}]`
- `projects`: `[{title, dates?, summary}]`
- Write into `profile/style_profile.md`'s "Hard facts (LOCKED)" section.

### 3. profile_voice — voice fingerprint
- `avg_bullet_length` (chars)
- `verb_taxonomy`: actual verbs used in the resume (compare against `resume_checklist.md`'s whitelist/blacklist)
- `metric_density`: % of bullets with numbers
- `tech_placement`: at-start / mid / end of bullet
- `impact_pattern`: e.g. `<verb> <bold tech> <feature>, <bold metric>`
- `tense` + `capitalization_style`
- bullet sentence length

### 4. profile_structure — layout fingerprint
- `sections_order`
- `bullet_format_template`
- bullet counts per role / project
- `page_count`, `header_layout`, `role_header_pattern`
- Skills section structure (number of category lines)

### 5. extract_skill_inventory — tech ammunition
- List every tech in base by category: Languages / Frameworks / Databases / Cloud / AI&ML / Messaging / Auth / Testing / Tools / Process / Domains
- List demonstrated business problems (each = role + scale + tech + outcome)
  - Each entry must be specific enough for Phase 1 retrieval — e.g., "real-time event pipeline ingesting X events/sec at Y" beats "built backend system"
- List coverage gaps (common JD tech NOT in base) — used by Phase 1's Strategy C
- List the default landing pad for each gap (which role / project / bullet slot it should inject into)
- Encode the polyglot OR-list rule: when a JD lists 4+ alternative languages, pick 1 missing one to inject into Projects (preferred order: TypeScript > Go > Java > Swift > C++)

### 6. reset bullet_bank
- Write an empty skeleton `profile/bullet_bank.md`: keep the Index table header and Slot section structure, but clear out variant snippets.
- Prior variants were based on the old base; once `profile/base_resume.md` changes, they're invalid.
- Phase 1 re-populates the bank as new JDs come in.

### 7. self_check
- [ ] All 4 output files are written and non-empty
- [ ] `profile/base_resume.pdf` renders to 1 page and visually matches the source PDF
- [ ] Hard facts are complete (no missing company / title / date / school)
- [ ] Voice profile is specific (not generic phrases like "professional, clear")
- [ ] Inventory is exhaustive (every tech in base is listed)
- [ ] business_problems are concrete (each = verb + scale + outcome)
- [ ] Coverage gaps list at least 10 common missing tech + landing pads
- [ ] On failure → re-run the failing step (max 2 retries), then surface to operator

### 8. DO NOT touch
- ❌ `master_prompt.md` — that's the rules file, independent of base content
- ❌ `resume_checklist.md` — operator-authoritative, not derived from the resume
- ❌ `linkedin_search_terms.md`
- ❌ `README.md`
- ❌ `outputs/` — historical records of past Phase 1 runs

---

## Trigger keywords

The operator says any of these → run Phase 0:
- "rerun Phase 0" / "重做 Phase 0"
- "update resume" + provides a new PDF
- "changed jobs" / "换工作了"
- "added new experience" / "加了新经历"
- "I updated my resume"

---

## After Phase 0 completes

Tell the operator: "Phase 0 done. Style fingerprint / skill inventory / bullet bank are refreshed. Ready to paste new JDs for Phase 1 tailoring."
