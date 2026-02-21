import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

# Why Option A (Failure Explainer) over Option B (Flaky Test Classifier):
# Our current Genfox.ai-style workflow prioritizes immediate, actionable feedback.
# When a test fails, developers need to know WHY instantly — not after a batch run.
# Option A integrates directly into the test lifecycle, making AI assistance
# feel native to the framework rather than a post-processing step.

def explain_failure(failure_info: dict) -> str:
    """
    Takes test failure details and returns a plain English explanation
    with suggested fix using Claude API.
    """
    api_key = os.getenv("ANTHROPIC_API_KEY")
    
    if not api_key:
        return "⚠️ ANTHROPIC_API_KEY not set. Skipping AI analysis."

    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""You are a QA engineer assistant. A Playwright test has failed.
Analyze the failure and provide:
1. Plain English explanation of what broke
2. Most likely root cause
3. Specific suggested fix

Test Name: {failure_info.get('test_name')}
Error Details:
{failure_info.get('error')}
File: {failure_info.get('file')}

Keep your response concise and actionable. Max 150 words."""

    try:
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=300,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text

    except Exception as e:
        return f"⚠️ AI analysis failed: {str(e)}"