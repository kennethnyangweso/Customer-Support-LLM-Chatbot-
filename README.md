
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/395494d7-c9fc-44b1-b717-8111267abc82" />


[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()

---

## 📊 Business Understanding

Modern businesses face high volumes of customer queries daily, ranging from billing issues to technical problems. Efficient and accurate customer support is critical to ensure customer satisfaction, reduce churn, and optimize operational costs.  

This project explores how a chatbot powered by language models (LLMs) could automate customer support tasks for common intents such as **billing**, **technical issues**, and **escalations**.  

---

## ❓ Problem Statement

The challenge is to build a chatbot capable of understanding customer messages and responding appropriately based on intent. Key difficulties include:  

- Accurately identifying customer intent (billing, technical, escalation, or fallback).  
- Generating coherent and helpful responses.  
- Ensuring reliability on limited hardware resources.  
- Making the system scalable for future integration with larger models.  

---

## 🎯 Objectives

1. Develop a **customer support chatbot CLI** capable of handling user queries interactively.  
2. Implement **intent detection** to categorize queries into billing, technical, escalation, or fallback.  
3. Experiment with **LLM-based approaches** to generate dynamic responses.  
4. Provide **fallback human-like responses** when LLM responses are insufficient or hardware constraints prevent LLM usage.  

---

## 📝 Methodology

1. **Intent Detection:**  
   A lightweight rule-based or simple NLP-based method to classify user queries.  

2. **Response Generation:**  
   - Initially explored transformer-based models such as OpenAI GPT, Hugging Face Flan-T5 variants, and Microsoft Phi models.  
   - Small models were **fast but produced shallow and inaccurate responses**.  
   - Large models produced high-quality responses but **could not run smoothly on local hardware**, causing crashes or extremely slow inference.  
   - Due to these limitations, the project **relies on curated mock responses** for each intent to ensure accuracy and reliability.  

3. **CLI Interface:**  
   - Users interact with the chatbot through a simple command-line interface.  
   - The system detects intent and returns either a pre-written human-like response or (optionally) invokes an LLM if available.  

4. **Prompt Management:**  
   - Prompts are modular and stored as text files (`system.txt`, `billing.txt`, `technical.txt`, `escalation.txt`, `fallback.txt`).  
   - This design allows easy integration of LLMs in the future when hardware constraints are resolved.  

---

## 💬 Mock Responses

### 🧾 Billing
- "I’m sorry for the inconvenience this may have caused. Duplicate charges can sometimes occur due to pending transactions or billing overlaps. I recommend reviewing your latest invoice to confirm whether one charge is temporary."  

### 💻 Technical
- "I’m sorry you’re experiencing technical difficulties. Have you tried restarting your device or checking your network connection?"  

### 🔼 Escalation
- "I understand your frustration and I can escalate this to a human agent who can assist further."  

### ❔ Fallback
- "I’m here to help. Could you provide more details about the issue?"  

---

## 📈 Results

- The chatbot reliably classifies queries into intents and provides **accurate, friendly, and professional responses** using mock responses.  
- Experiments with transformer-based models demonstrated the following:  
  - Small LLMs were unable to follow prompts accurately, often returning generic or irrelevant responses.  
  - Large LLMs produced higher quality responses but were **not feasible on local hardware** due to memory and speed constraints.  
- The **fallback approach using curated responses ensures consistent performance** and prepares the system for future LLM integration.

### How to test the repo 


# Customer Support Bot (Mock Responses) Setup


# 1️⃣ Clone the repository
    git clone https://github.com/yourusername/Customer-Support-Bot.git
    cd Customer-Support-Bot

# 2️⃣ Create a virtual environment (recommended)
# Using Python's built-in venv
     python -m venv cs_bot_env

# Activate the virtual environment
# On Windows:
    cs_bot_env\Scripts\activate
# On Mac/Linux:
    source cs_bot_env/bin/activate

# 3️⃣ Install required dependencies
# (Ensure you have a requirements.txt in your repo)
    pip install --upgrade pip
    pip install -r requirements.txt

# 4️⃣ Run the Customer Support Bot CLI
# The bot uses human-like mock responses
    python -m app.cli

##### What to expect:

``` (cs_llm) C:\Users\PC\OneDrive\Desktop\Data Science\PERSONAL PROJECTS\Customer-Support-LLM-Chatbot->python -m app.cli
Customer Support Bot (type 'exit' to quit)
User: i was charged twice
Bot: I’m sorry for the inconvenience this may have caused. Duplicate charges can sometimes occur due to pending transactions or billing overlaps. I recommend reviewing your latest invoice to confirm whether one charge is temporary. If you’d like, I can guide you on how to check this.
User: my connection is poor
Bot: I’m sorry you’re experiencing technical difficulties. Have you tried restarting your device or checking your network connection?
User: who can help
Bot: I’m here to help. Could you provide more details about the issue?
User: the internet is slow could you send a team to asses the issue
Bot: Thank you for reporting this. A quick first step is to restart the device and see if the problem persists.
User: Can I speak to an agent please
Bot: I understand your frustration and I can escalate this to a human agent who can assist further.
```


---

## ✅ Conclusion

This project demonstrates a practical approach to building a customer support chatbot under **hardware constraints**. By combining **intent detection** with **curated human-like responses**, the system provides reliable support while remaining modular and future-ready for LLM integration.  

Once more powerful hardware becomes available, the prompts and architecture allow easy replacement of mock responses with transformer-based models to generate dynamic and contextually rich responses.  

---

## 🔮 Future Work

- Integrate **medium to large LLMs** for dynamic response generation.  
- Improve intent detection using a trained NLP model for higher accuracy.  
- Expand response database with richer context and conversation handling.  
- Add multi-turn conversation handling and memory for complex support scenarios.  
