# Project 6 — Guarded Knowledge Bot
#
# Concepts
# - Guardrails
# - Context
# - Validation
#
# Scenario
# - Create a Knowledge Bot that searches uploaded company data and filters anything inappropriate or irrelevant.
#
# Tasks
# 1) Implement a guardrail that flags outputs containing banned words.
# 2) Wrap it around an agent that answers company policy questions.
# 3) Add a simple context like `UserRoleContext(role: "HR" | "Engineer")` that adjusts allowed information.

from agents import Agent, Runner, guardrail
from dataclasses import dataclass
import asyncio
from pydantic import BaseModel
@dataclass
class CompanyContext:
    company_data:str
    role:str

class OutputCheck(BaseModel):
    is_safe:bool
    reason:str

guarded_words = ["salary", "confidential", "leak", "fired"]

guardrail_agent = Agent(
    name="Output Guardrail Agent",
    instructions=(
        "You are a content auditor. Examine the given text and decide whether it "
        "includes any banned or confidential words: "
        f"{', '.join(guarded_words)}. "
        "If any appear, return a short JSON-like verdict explaining the reason and set is_safe=False. "
        "If none appear, set is_safe=True and include a brief reasoning line."
    ),
    output_type=OutputCheck,
)

def knowledge_instrcutions(context,agent):
    info=context.context.company_data
    role=context.context.role
    return (
        f"You are a company knowledge assistant for role={role}.\n\n"
        "Use the following internal company info to answer questions precisely. "
        "If the answer is not contained in the company info, say you do not know and do NOT invent numbers like salary.\n\n"
        f"--- COMPANY INFO START ---\n{info}\n--- COMPANY INFO END ---\n\n"
        "Answer concisely and factually."
    )


knowledge_agent=Agent[CompanyContext](
    name="Knowledge agent",
    instructions=knowledge_instrcutions,
)

async def run_query(user_question:str,compnay_ctx:CompanyContext):
    gen_result=await Runner.run(knowledge_agent,user_question,context=compnay_ctx)
    generated_answer=gen_result.final_output
    # print(f"Generated answer: {generated_answer}")

    check_result=await Runner.run(guardrail_agent,generated_answer)
    check: OutputCheck=check_result.final_output

    if not check.is_safe:
        print(check.reason)
        return
    

    print("\n✅ Final Answer (safe):\n", generated_answer)

async def main():
    company_info_text = """
    Company X internal policies:
    - Annual leave: 18 days per year.
    - Sick leave: up to 10 days per year.
    - CEO compensation is confidential and not publicly disclosed.
    - Filing HR complaints goes to hr@companyx.example with ticket number.
    """

    ctx_hr = CompanyContext(company_data=company_info_text, role="HR")

    await run_query("What is the leave policy for employees?", ctx_hr)
    await run_query("What is the CEO's salary?", ctx_hr)
if __name__=="__main__":
    asyncio.run(main())