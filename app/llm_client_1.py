from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LLMClient1:
    def __init__(self):
        model_name = "microsoft/Phi-3-mini-4k-instruct"

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_name,
            trust_remote_code=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype=torch.float32,
            device_map="cpu",
            trust_remote_code=True,
            attn_implementation="eager",  # IMPORTANT
            use_cache=False               # CRITICAL FIX
        )

        self.model.eval()

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt"
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                use_cache=False   # MUST match model
            )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

