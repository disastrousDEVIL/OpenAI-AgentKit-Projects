# Project 8 — Ethical Support Assistant
#
# Concepts
# - Guardrails
# - Context
# - Multi-role validation
#
# Scenario
# - Build an HR Support Assistant to help with workplace issues (harassment policy, leave, complaint escalation) while following ethical boundaries:
#   1) It cannot give legal advice.
#   2) It must not comment on personal relationships.
#   3) It should tailor tone and permissions by user role (Employee vs Manager, etc.).

from agents import Agent, Runner
from dataclasses import dataclass
import asyncio

@dataclass
class UserRoleContext:
    role:str
    department:str

def dynamic_instructions(context,agent):
    role=context.context.role
    department=context.context.department

    return (f"""
You are an HR support assistant. Adjust your tone based on the user's role and department.

- Employee → friendly and helpful tone.
- Manager → professional and authoritative tone.
- HR → neutral and informative tone.
- CEO → confident and directive tone.

User role: {role}
Department: {department}

Answer questions only about HR policies like leave, behavior, and internal process.
""")

knowledge_agent=Agent[UserRoleContext](
    name="Knowledge agent",
    instructions=dynamic_instructions
)
banned_words=["legal advice","personal relationship","terminate","fire","performance","complaint","escalation"]

guardrail_agent=Agent(
    name="Guardrail agent",
    instructions=(
        f"You are a guardrail agent that checks if the answer contains any of the following words: {', '.join(banned_words)}"
        "If it does, you should return False"
        "If it doesn't, you should return True"
    ),
    output_type=bool
)

banned_words_remover=Agent(
    name="Banned words remover",
    instructions=(
        f"You are a banned words remover that removes the banned words from the answer"
        "Banned words are: {', '.join(banned_words)}, you should remove them"
    ),
    output_type=str
)
async def main():
    result=await Runner.run(knowledge_agent,"What is the leave policy for employees?",context=UserRoleContext(role="Employee",department="HR"))

    result2=await Runner.run(guardrail_agent,result.final_output)

    if result2.final_output:
        print("No banned words found")
        print(result.final_output)
    else:
        print("Banned words found")
        result3=await Runner.run(banned_words_remover,result.final_output)
        print(result3.final_output)


if __name__=="__main__":
    asyncio.run(main())