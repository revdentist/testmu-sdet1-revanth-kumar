import pytest
import os
from dotenv import load_dotenv
from utils.llmexplainer import explain_failure

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://the-internet.herokuapp.com")

@pytest.fixture(scope="session")
def api_url():
    return os.getenv("BASE_URL", "https://the-internet.herokuapp.com")

@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("TEST_USERNAME", "tomsmith"),
        "password": os.getenv("TEST_PASSWORD", "SuperSecretPassword!")
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Capture failure details
        failure_info = {
            "test_name": item.name,
            "error": str(report.longrepr),
            "file": str(item.fspath)
        }

        # Send to LLM and get explanation
        explanation = explain_failure(failure_info)

        # Attach explanation to report
        if explanation:
            report.sections.append((
                "🤖 AI Failure Analysis",
                explanation
            ))