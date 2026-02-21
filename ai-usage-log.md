# AI Usage Log
## TestMu SDET-1 Hackathon Assignment

> This log documents every AI tool used, the task it helped with,
> what it produced, and critically — what I had to change and why.
> Logged in real time as work progressed.

---

## Tool 1: Claude (claude.ai — free tier)
**Role in project:** Strategist, architect, content generator

---

### Entry 1 — Project Strategy
**Task:** Breaking down the assignment into executable steps
**Prompt approach:** Shared the full assignment PDF and asked for
a phased execution plan prioritizing reviewer impact over speed
**What Claude produced:** 5-phase plan with time estimates and
smart decisions (why Playwright over Selenium, why Option A over B)
**What I changed:** Adjusted time estimates based on my actual
Python/API experience from Genfox.ai work
**Why it mattered:** Prevented me from jumping into code without
thinking about what reviewers actually evaluate

---

### Entry 2 — Target App Decision
**Task:** Choosing which app to run tests against
**Prompt approach:** Asked Claude to recommend a demo app with
real login, dynamic content, and form elements
**What Claude produced:** Recommended the-internet.herokuapp.com
with reasoning (real login page, form elements, QA community recognition)
**What I changed:** Nothing — reasoning was solid
**Why it mattered:** Tests needed to actually pass/fail realistically,
not just be syntactically correct

---

### Entry 3 — Project Scaffold
**Task:** Folder structure and config files
**Prompt approach:** Asked for Python + Playwright structure
that mirrors production QA frameworks
**What Claude produced:** Full folder tree with tests/, utils/,
reports/, test-cases/ separation
**What I changed:** Added reports/ to .gitignore since generated
HTML reports shouldn't be version controlled
**Why it mattered:** Clean structure signals engineering maturity
to reviewers before they read a single line of code

---

### Entry 4 — Login Test Cases (Prompt Iteration)
**Task:** Generating Gherkin scenarios for Login module
**Attempt 1 prompt:** "Write test cases for a login page"
**Problem:** Too generic, only happy path, no edge cases
**Attempt 2 prompt:** Added specific scenarios but missed
brute force and session expiry
**Problem:** Error messages not specific enough for assertions
**Attempt 3 prompt:** Added role context (senior QA engineer),
listed all 7 scenarios explicitly, specified error message text
requirement, asked for Background block
**What finally worked:** All 7 scenarios with assertable Then steps
**Time spent iterating:** ~15 minutes

---

### Entry 5 — Dashboard Test Cases (Prompt Iteration)
**Task:** Generating Gherkin scenarios for Dashboard module
**Attempt 1 prompt:** "Generate test cases for a dashboard page"
**Problem:** Only 3 shallow scenarios generated
**Attempt 2 prompt:** Added widget/table/filter context
**Problem:** Then steps too vague to automate
**Attempt 3 prompt:** Listed all 8 scenarios explicitly, added
"specific assertable Then steps" requirement, specified viewport size
**What finally worked:** 8 scenarios all directly mappable to code
**Time spent iterating:** ~10 minutes

---

### Entry 6 — API Test Cases (Prompt Iteration)
**Task:** Generating Gherkin scenarios for REST API module
**Attempt 1 prompt:** "Write API test cases for a REST API"
**Problem:** Only GET and POST generated, no schema validation
**Attempt 2 prompt:** Added CRUD + error handling requirement
**Problem:** Schema validation and response time missing
**Attempt 3 prompt:** Specified base URL, listed all 9 scenarios,
required status codes and schema field names in assertions
**What finally worked:** Complete coverage with assertable steps
**Time spent iterating:** ~10 minutes

---

### Entry 7 — LLM Integration Design
**Task:** Deciding between Option A and Option B
**Prompt approach:** Asked Claude to compare both options
against my existing Genfox.ai workflow experience
**What Claude produced:** Analysis showing Option A integrates
into test lifecycle natively vs Option B being post-processing
**What I changed:** Nothing — matched my instinct from
building the incident detection backend at Genfox.ai
**Why it mattered:** The choice needed to be defensible
in the VP/CEO conversation, not just convenient

---

### Entry 8 — conftest.py Failure Hook
**Task:** Wiring LLM call into pytest failure lifecycle
**Prompt approach:** Asked for pytest hook that captures
failure details and attaches LLM response to HTML report
**What Claude produced:** pytest_runtest_makereport hook
with report.sections.append for inline report attachment
**What I changed:** Added failure_info dict structure to
pass structured data rather than raw string to LLM
**Why it mattered:** Structured input = better LLM output

---

## Tool 2: Cursor (claude-4.6-opus-high-thinking)
**Role in project:** Code executor, error fixer, refiner

---

### Entry 9 — PowerShell Compatibility Fix
**Task:** mkdir command failed on Windows PowerShell
**What Cursor fixed:** Rewrote to New-Item with array syntax
and -Force flag for Windows compatibility
**What I learned:** Unix commands don't translate directly
to PowerShell — Cursor caught this immediately

---

### Entry 10 — Import Resolution
**Task:** utils module not found error in conftest.py
**What Cursor fixed:** Added __init__.py files to make
Python treat directories as modules
**What I learned:** Cursor is faster than me at catching
Python module structure issues

---

### Entry 11 — Test Refinements
**Task:** Playwright selector fine-tuning
**What Cursor fixed:** Adjusted CSS selectors to match
actual DOM structure of the-internet.herokuapp.com
**What I changed:** Kept Cursor's selector fixes but
reviewed each one to understand why it changed

---

## Summary

| Tool | Tasks | Most Valuable For |
|------|-------|-------------------|
| Claude (claude.ai) | Strategy, prompts, architecture, docs | Thinking and planning |
| Cursor (claude-4.6-opus) | Code execution, error fixing, refinement | Building and debugging |

**Key insight:** Claude handled the "why" and "what",
Cursor handled the "how" and "fix it". Neither alone
would have produced this quality of output.