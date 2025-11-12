# 🕹 Project 5 — Multi-Persona Chat System

# Concepts
# - Cloning agents
# - Handoffs
# - Lifecycle hooks

# Scenario
# - A user chats with three personas:
#   1) PhilosopherAgent — reflective
#   2) ComedianAgent — humorous
#   3) TeacherAgent — educational
# - A TriageAgent routes messages based on tone.

# Build Steps
# 1) Create a base agent.
# 2) Clone it three times with .clone() and unique instructions.
# 3) Implement a TriageAgent to select the responding persona.
# 4) Add AgentHooks to log which persona handled the message.



from agents import Agent, Runner, RunHooks
import asyncio


class LoggingHooks(RunHooks):
    async def on_agent_start(self, context, agent):
        print(f"Starting agent: {agent.name}")

    async def on_agent_end(self, context, agent, output):
        print(f"[LOG] Agent {agent.name} finished. Output: {output}")

    async def on_handoff(self, context, from_agent, to_agent):
        print(f"[LOG] Handoff from {from_agent.name} → {to_agent.name}")



hooks = LoggingHooks()

base_agent=Agent(
    name="Base Agent",
    instructions="You are a base agent that can answer questions and help with tasks",
)
philosopher_agent=base_agent.clone(
    name="Philosopher Agent",
    instructions="You answers the philosophical questions with a tone of a philosopher in 20 words",
)
comedian_agent=base_agent.clone(
    name="Comedian Agent",
    instructions="You answers the questions with a tone of a comedian in 20 words",
)
teacher_agent=base_agent.clone(
    name="Teacher Agent",
    instructions="You answers the questions with a tone of a teacher in 20 words",
)



triage_agent=Agent(
    name="Triage Agent",
    instructions=(
        "Read the user's message and decide who should respond:\n"
        "- If it sounds reflective or about life, hand off to the Philosopher Agent.\n"
        "- If it asks for a joke or fun, hand off to the Comedian Agent.\n"
        "- If it asks for help learning or explaining, hand off to the Teacher Agent."
    ),
    handoffs=[philosopher_agent,comedian_agent,teacher_agent],
)
async def main():
    messages = [
        "Why do people fear death?",
        "Tell me a joke about AI.",
        "Can you explain how black holes form?"
    ]

    for msg in messages:
        print(f"\n💬 User: {msg}")
        result = await Runner.run(triage_agent, msg, hooks=hooks)
        print(f"🤖 Response: {result.final_output}")
if __name__ == "__main__":
    asyncio.run(main())
