from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


class LLMClient1:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct",
            trust_remote_code=True
        )

        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = AutoModelForCausalLM.from_pretrained(
            "microsoft/Phi-3-mini-4k-instruct",
            torch_dtype=torch.float32,
            device_map="cpu",
            trust_remote_code=True
        )

        self.model.eval()

    def generate(self, prompt: str) -> str:
        # 🔒 SAFETY CHECK
        if not isinstance(prompt, str):
            raise TypeError(f"Expected prompt to be str, got {type(prompt)}")

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            padding=True,
            truncation=True
        )

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=120,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                use_cache=True
            )

        response = self.tokenizer.decode(
            outputs[0][inputs["input_ids"].shape[-1]:],
            skip_special_tokens=True
        )

        return response.strip()




        return self.tokenizer.decode(
            outputs[0][inputs.shape[-1]:],
            skip_special_tokens=True
        ).strip()
