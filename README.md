# 🤖 OpenAI AgentKit — Hands-On Learning Projects

A practical learning repository to **master OpenAI’s AgentKit** through 10 focused projects.  
Each file in `Projects/` includes a short **study brief** (Concepts, Scenario, Build Steps) to help you learn by doing.  
Read the brief, run the code, and experiment — each project is designed to be quick, modular, and fun.

---

## 🧠 Why this repo
This repo is a guided playground for developers who want to explore **Agentic AI** using **OpenAI’s AgentKit** — a new SDK for creating tool-using, context-aware, and safety-controlled AI agents.

If you share this repo on GitHub or LinkedIn, others can follow the same study path and learn alongside you.

---

## ⚙️ Prerequisites
- Python 3.10+  
- An Agent SDK that provides `Agent`, `Runner`, and guardrail APIs (imported as `agents`)  
  *(If your SDK uses a different module name, update the imports.)*

📘 Official docs: [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)

---

## 🧩 How to Learn
1. Open any file inside `Projects/`  
2. Read the **study brief** at the top  
3. Follow the implementation steps  
4. Run the script and test results  
5. Move on to the next project — each one adds new concepts

---

## 🧭 Learning Path (Projects)

| # | Project | Concept |
|---|----------|----------|
| 1 | Smart Weather Concierge | Tool use, structured outputs |
| 2 | Support Chat System | Manager pattern, agents as tools |
| 3 | Task Planner | Dynamic instructions, async context |
| 4 | Cinema Chat | Custom tool handler, StopAtTools |
| 5 | Multi-Persona Chat System | Cloning, handoffs, hooks |
| 6 | Academic Guardrail System | Input guardrails, handoffs |
| 7 | Guarded Knowledge Bot | Guardrails over company data |
| 8 | Ethical Support Assistant | Role-aware guardrails |
| 9 | Safe Tech Support Assistant | Sanitization, safety checks |
| 10 | Secure Banking Assistant | Context verification |

Start from Project 1 and progress sequentially — you’ll move from foundational design to advanced orchestration.

---

## 🧰 Setup (Windows PowerShell)

```pwsh
cd C:\Users\newma\Desktop\openai_agent_sdk
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install openai-agents
# If using another SDK distribution, install that instead
````

---

## 📁 Project Structure

```
openai_agent_sdk/
  Projects/
    Smart_Weather_Concierge.py
    Support_Chat_System.py
    Cinema_Chat.py
    task_planner.py
    Multi_Persona_Chat_System.py
    basic_guardrail_implementation.py
    Guarded_Knowledge_Bot.py
    Ethical_Support_Assistant.py
    Secure_Banking_Assistant.py
    Safe_Tech_Support_Assistant.py
```

---

## ▶️ Running Examples

From repo root (recommended):

```pwsh
python -m Projects.Smart_Weather_Concierge
python -m Projects.Support_Chat_System
# ...and so on
```

Or from inside `Projects/`:

```pwsh
cd Projects
python Smart_Weather_Concierge.py
```

---

## 👨‍💻 Author

**Krish Batra**

AI Engineer & Agentic Systems Developer

🌐 [vybecode.in](https://vybecode.in) 

🧠 Building AI frameworks with reasoning, safety, and personality.

---

## 💬 Share on LinkedIn

If you post about your learning journey, mention me so I can connect and reshare!  
Tag: [@Krish Batra on LinkedIn](https://www.linkedin.com/in/krish-batra/)

```text
🤖 Getting hands-on with OpenAI AgentKit!

This repo by @Krish Batra (https://www.linkedin.com/in/krish-batra/) 
collects 10 mini-projects to help you learn Agentic AI through practice.  
Each one focuses on a specific concept — tools, guardrails, reasoning, or collaboration — 
with a short “study brief” and runnable code.

Check it out 👇  
https://github.com/disastrousDEVIL/OpenAI-AgentKit-Projects

Try a project, post your results, and tag Krish to join the learning thread!
```

## 📝 Notes

* These examples assume `agents` library availability.
  Adjust imports if your SDK uses a different name (e.g. `from agents import Agent, Runner, ...`).
* All scripts print to stdout and are designed for quick, local experimentation.

---

## 🪪 License

MIT License — free for learning, modification, and sharing.
