import os
os.environ["TRANSFORMERS_NO_TORCHVISION"] = "1"

import torch
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ------------------------
# Paths & Model
# ------------------------

PROMPT_DIR = Path(__file__).resolve().parent.parent / "prompts"
MODEL_NAME = "google/flan-t5-base"

print("Loading LLM (CPU)...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

model.eval()

print("Model loaded successfully.")

# ------------------------
# Prompt Loader
# ------------------------

def load_prompt(name: str) -> str:
    file_path = PROMPT_DIR / f"{name}.txt"
    if not file_path.exists():
        raise FileNotFoundError(f"Missing prompt file: {file_path}")
    return file_path.read_text(encoding="utf-8").strip()

# ------------------------
# LLM Response Generator
# ------------------------

def generate_llm_response(user_message: str, intent: str) -> str:
    try:
        system_prompt = load_prompt("system")
        intent_prompt = load_prompt(intent)

        # Strong instruction-based prompt for FLAN-T5
        prompt = f"""
You are a professional customer support assistant for a telecom company.

SYSTEM INSTRUCTIONS:
{system_prompt}

TASK INSTRUCTIONS:
{intent_prompt}

RESPONSE RULES:
- Be polite, calm, and professional
- Apologize when the customer reports a problem
- Do NOT mention internal systems or policies unless necessary
- Do NOT say you are an AI
- Give clear next steps if possible
- Keep the response under 5 sentences

CUSTOMER MESSAGE:
{user_message}

AGENT RESPONSE:
""".strip()

        inputs = tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=120,
                temperature=0.3,          # lower = more stable
                do_sample=False,          # important for T5
                repetition_penalty=1.2
            )

        response = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.strip()

    except Exception as e:
        return f"⚠️ LLM Error: {str(e)}"





