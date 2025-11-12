## OpenAI AgentKit — Hands‑on Learning Projects

This repository is a learning base for people who want to practice building with OpenAI AgentKit. Each file in `Projects/` is a small, focused project with a short “study brief” in comments at the top. Read the brief, try the tasks, and run the script to see results.

If you share this repo on GitHub and LinkedIn, others can follow the same study path and build the projects alongside you.

### Prerequisites
- Python 3.10+ recommended
- An Agent SDK providing `Agent`, `Runner`, guardrails, and related APIs (imported as `agents`). If you use a different package name, update imports accordingly.

### Documentation
- Official OpenAI Agents SDK docs: `https://openai.github.io/openai-agents-python/`

### How to use this repo to learn
1) Pick a file in `Projects/`.
2) Read the header comments (Concepts, Scenario, Build Steps).
3) Implement or extend the steps in the code.
4) Run the script and iterate.
5) Repeat for the next project.

### Learning path (projects)
- 1) Smart Weather Concierge — tools, structured outputs, forced tool use
- 2) Support Chat System — manager pattern, agents as tools
- 3) Task Planner — dynamic instructions, async context
- 4) Cinema Chat — StopAtTools, custom tool handler
- 5) Multi‑Persona Chat System — cloning, handoffs, hooks
- 6) Guarded Knowledge Bot — guardrails over company context
- 7) Ethical Support Assistant — role‑aware responses with guardrails
- 8) Safe Tech Support Assistant — safety checks and sanitization
- 9) Secure Banking Assistant — context verification + guardrails

### 🧭 Learning Path

Each project builds on the previous one — from foundational agent design to complex orchestration.

Start from Project 1 and move sequentially for a guided learning experience.

### Setup (Windows PowerShell)
```pwsh
cd C:\Users\newma\Desktop\openai_agent_sdk
python -m venv .venv
.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
# Install the OpenAI Agents SDK
pip install openai-agents
# (If you use a different SDK distribution, install that package instead.)
```

### Project structure
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

### How to run examples
- From the repo root (recommended, after `Projects/__init__.py` is present):
```pwsh
python -m Projects.Smart_Weather_Concierge
python -m Projects.Support_Chat_System
python -m Projects.Cinema_Chat
python -m Projects.task_planner
python -m Projects.Multi_Persona_Chat_System
python -m Projects.basic_guardrail_implementation
python -m Projects.Guarded_Knowledge_Bot
python -m Projects.Ethical_Support_Assistant
python -m Projects.Secure_Banking_Assistant
python -m Projects.Safe_Tech_Support_Assistant
```

If you prefer running from inside the `Projects` folder:
```pwsh
cd Projects
python Smart_Weather_Concierge.py
```

### 🧑‍💻 Author

Krish Batra — AI Engineer & Agentic Systems Developer  
🌐 vybecode.in  
• 🧠 Building AI frameworks with reasoning, safety, and personality.

### Share on LinkedIn (template)
Feel free to copy and tweak:

```text
I’m learning OpenAI AgentKit using this hands‑on repo of mini‑projects.
Each script includes a short study brief (Concepts, Scenario, Build Steps) and runs locally.
Repo: <your GitHub URL>

If you’re exploring agents (tools, guardrails, handoffs, context), try these projects and share your progress!
```

### Notes
- These examples expect an available `agents` library. If your SDK uses another module name, adjust imports (e.g., `from agents import Agent, Runner, ...`).
- All scripts print to stdout and are designed for quick, local experimentation.

### License
See `LICENSE`.


