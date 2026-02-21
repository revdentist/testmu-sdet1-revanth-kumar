# TestMu SDET-1 Assignment — Revanth Kumar

AI-Native QA Framework | Python · Playwright · Claude API  
**LLM Integration:** Option A — Failure Explainer

---

## Project Structure
```
testmu-sdet1-revanth-kumar/
├── tests/
│   ├── login/
│   │   └── test_login.py          # Login module tests (6 scenarios)
│   ├── dashboard/
│   │   └── test_dashboard.py      # Dashboard module tests (8 scenarios)
│   └── api/
│       └── test_api.py            # REST API tests (9 scenarios)
├── test-cases/
│   ├── login_test_cases.feature   # Gherkin — Login
│   ├── dashboard_test_cases.feature # Gherkin — Dashboard
│   └── api_test_cases.feature     # Gherkin — REST API
├── utils/
│   └── llm_explainer.py           # Claude API failure explainer
├── reports/                        # Generated HTML reports
├── prompts.md                      # Raw prompts used for Task 2
├── ai-usage-log.md                 # Every AI tool, task, and output
├── conftest.py                     # Pytest fixtures + failure hook
├── pytest.ini                      # Pytest configuration
└── requirements.txt
```

---

## Setup

### Prerequisites
- Python 3.10+
- Git
- Anthropic API key (free tier works)

### Install
```bash
git clone https://github.com/revdentist/testmu-sdet1-revanth-kumar.git
cd testmu-sdet1-revanth-kumar

python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
playwright install chromium
```

### Configure

Create a `.env` file in the root:
```env
ANTHROPIC_API_KEY=sk-ant-your-key-here
BASE_URL=https://the-internet.herokuapp.com
TEST_USERNAME=tomsmith
TEST_PASSWORD=SuperSecretPassword!
```

---

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific module
```bash
pytest tests/login/ -v
pytest tests/dashboard/ -v
pytest tests/api/ -v
```

### View HTML report
After running, open:
```
reports/report.html
```

The report includes **AI failure analysis** for every failed test —
Claude explains what broke and suggests a fix in plain English.

---

## LLM Integration — How It Works

**Option A: Failure Explainer**

When any test fails:
1. `conftest.py` captures the test name, error, and file path
2. Sends it to Claude API via `utils/llm_explainer.py`
3. Claude returns a plain English explanation + suggested fix
4. This is attached directly inside the HTML test report
```
Test Failed: test_invalid_username
─────────────────────────────────
🤖 AI Failure Analysis:
The test failed because the error message selector '.flash.error'
was not found within the timeout period. This likely means the
login form submission is not triggering the error state.

Suggested fix: Check if the button selector 'button[type=submit]'
is correct and that the page has fully loaded before asserting.
─────────────────────────────────
```

---

## Why Option A Over Option B

Option B (Flaky Test Classifier) requires a completed batch run
before it produces value. Option A gives immediate, actionable
feedback inside the test lifecycle — the moment a test fails,
the developer knows why. This mirrors the real-time alerting
architecture I built at Genfox.ai for incident detection.

---

## Test Coverage

| Module | Scenarios | App Under Test |
|--------|-----------|----------------|
| Login | 6 | the-internet.herokuapp.com/login |
| Dashboard | 8 | the-internet.herokuapp.com |
| REST API | 9 | jsonplaceholder.typicode.com |

---

## What I'd Build Next

1. **Screenshot capture on failure** — attach visual evidence
alongside the LLM explanation in the report

2. **Flaky test detection** — run failed tests 3x automatically,
feed results to LLM to distinguish real bugs from flakiness

3. **Auto-healing selectors** — when a selector fails, ask LLM
to suggest alternative selectors from the page DOM

4. **Slack integration** — pipe AI failure summaries directly
to the team Slack channel on CI/CD failure

5. **Test generation from user stories** — feed Jira tickets
directly to LLM, auto-generate Gherkin scenarios

---

## AI Tools Used

| Tool | Used For |
|------|----------|
| Claude (claude.ai) | Strategy, prompts, architecture, documentation |
| Cursor (claude-4.6-opus) | Code execution, error fixing, refinement |

Full details in `ai-usage-log.md`