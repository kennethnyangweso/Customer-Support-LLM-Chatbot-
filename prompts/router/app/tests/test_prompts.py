# tests/test_prompts.py

from router.prompt_router import route_prompt


class MockLLM:
    def chat_completion(self, messages):
        user_text = messages[-1]["content"].lower()

        if "refund" in user_text or "human" in user_text:
            return "escalation"
        if "bill" in user_text or "charge" in user_text:
            return "billing"
        if "internet" in user_text or "network" in user_text:
            return "technical"
        return "fallback"


def test_billing_routing():
    route = route_prompt("Why is my bill so high?", MockLLM())
    assert route == "billing"


def test_technical_routing():
    route = route_prompt("My internet is slow", MockLLM())
    assert route == "technical"


def test_escalation_routing():
    route = route_prompt("I want a refund now", MockLLM())
    assert route == "escalation"


def test_fallback_routing():
    route = route_prompt("Help", MockLLM())
    assert route == "fallback"
