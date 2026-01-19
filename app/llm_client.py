class LLMClient:
    def generate(self, prompt: str) -> str:
        """
        Mock LLM response for testing.
        It just echoes the prompt so you can see routing working.
        """
        return f"[MOCK RESPONSE]\n{prompt}"
