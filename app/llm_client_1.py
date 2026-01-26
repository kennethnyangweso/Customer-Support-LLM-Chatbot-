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
            low_cpu_mem_usage=True,
            device_map=None,
            trust_remote_code=True
        )

    def generate(self, messages):
        inputs = self.tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            tokenize=True,
            return_tensors="pt"
        )

        outputs = self.model.generate(
            inputs,
            max_new_tokens=120,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )

        return self.tokenizer.decode(
            outputs[0][inputs.shape[-1]:],
            skip_special_tokens=True
        ).strip()


        return self.tokenizer.decode(
            outputs[0][inputs.shape[-1]:],
            skip_special_tokens=True
        ).strip()
