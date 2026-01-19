from router.prompt_router import route_prompt


class MockLLM:
    def chat_completion(self, messages):
        text = messages[-1]["content"].lower()

        if "refund" in text:
            return "escalation"
        if "bill" in text:
            return "billing"
        if "internet" in text:
            return "technical"
        return "fallback"


def test_billing():
    assert route_prompt("Why is my bill high?", MockLLM()) == "billing"


def test_technical():
    assert route_prompt("My internet is slow", MockLLM()) == "technical"


def test_escalation():
    assert route_prompt("I want a refund", MockLLM()) == "escalation"


def test_fallback():
    assert route_prompt("Help", MockLLM()) == "fallback"
