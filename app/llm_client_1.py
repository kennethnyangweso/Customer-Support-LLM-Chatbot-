from pathlib import Path
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

class LLMClient1:
    """
    Local LLM client using Phi-3 Mini Instruct with apply_chat_template.
    Produces realistic human-like responses.
    """
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        # This will download the model first time
        self.tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct", trust_remote_code=True
        ).to(self.device)

    def generate(self, messages_or_text):
        """
        messages_or_text: either string (user message) or list of {"role": ..., "content": ...}
        """
        # if string, wrap in chat message
        if isinstance(messages_or_text, str):
            messages = [{"role": "user", "content": messages_or_text}]
        else:
            messages = messages_or_text

        # Prepare input
        inputs = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_dict=True,
            return_tensors="pt",
        ).to(self.device)

        # Generate response
        outputs = self.model.generate(**inputs, max_new_tokens=150)
        # Decode response (skip the input prompt tokens)
        return self.tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:])
