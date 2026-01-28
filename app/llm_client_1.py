from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

class LLMClient1:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct",
            trust_remote_code=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct",
            torch_dtype=torch.float32,
            device_map="cpu",
            trust_remote_code=True
        )

        # 🔴 CRITICAL FIX
        self.model.config.use_cache = False

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt"
        )

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=120,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            use_cache=False,   # 🔴 CRITICAL FIX
        )

        return self.tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[-1]:],
            skip_special_tokens=True
        ).strip()





        return self.tokenizer.decode(
            outputs[0][inputs.shape[-1]:],
            skip_special_tokens=True
        ).strip()
