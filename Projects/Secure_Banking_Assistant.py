# 🏦 Project 9 — Secure Banking Assistant
#
# Concepts
# - Input guardrails
# - Context-based access controls
# - Structured outputs
#
# Scenario
# - Build an AI banking support agent that helps users check balances, report lost cards, and explain policies while enforcing strict security rules.
#
# The Agent Must
# 1) Block any sensitive or confidential input (PINs, passwords, account numbers) using input guardrails.
# 2) Prevent unverified users from seeing balances via context-based checks.
# 3) Return structured outputs showing both the message and action (e.g., "show_balance", "blocked").
# 4) Use the Agent SDK guardrail system (`InputGuardrail`, `GuardrailFunctionOutput`) for pre-execution safety.
#
# In short: a context-aware, verified-access banking chatbot with automatic guardrails that trip and stop unsafe queries.


from logging import info
from agents import Agent,Runner, GuardrailFunctionOutput, InputGuardrail, InputGuardrailTripwireTriggered
from dataclasses import dataclass
import asyncio


@dataclass
class UserContext:
    user_id:str
    is_verified:bool
    account_balance:str


guardrail_agent=Agent(name="Guardrail agent",instructions="""You are a guardrail that checks if a user's message contains sensitive or restricted requests.
        If the message asks for PINs, passwords, account numbers, or confidential details, return True. 
        If the message asks for balance and the user is not verified, return True. 
        Otherwise, return False. Respond with only True or False.""",output_type=bool)

banking_agent=Agent(name="Banking agent",instructions="""You are a banking agent that can help users with following tasks:-
1) Check balance
2) Report Lost/Stolen Card
3) Explain Account policies
Any other task asked by the user, refuse politely that it isnt capable by you at the moment""",handoff_description="A helpful agent that handles verified banking tasks",output_type=str)

async def guardrail_function(context,agent,input_data:str)->GuardrailFunctionOutput:
    result=await Runner.run(guardrail_agent,input_data,context=context)
    final_output=result.final_output
    if final_output:
        return GuardrailFunctionOutput(output_info="trip wire triggered",tripwire_triggered=True)
    else:
        return GuardrailFunctionOutput(output_info="trip wire not triggered",tripwire_triggered=False)

Customer_Agent=Agent[UserContext](
    name="Customer Agent",
    instructions="""
You are a banking assistant.
You greet the user, collect their request, and hand off to the Bank Data Agent.
""",
    handoffs=[banking_agent],
    input_guardrails=[InputGuardrail(guardrail_function=guardrail_function)]

)

async def main():
    ctx = UserContext(user_id="1234567890", is_verified=False, account_balance="1000")

    print("\n--- Safe Query ---")
    safe_result = await Runner.run(Customer_Agent, "Tell me about your loan policy", context=ctx)
    print("✅", safe_result.final_output)

    print("\n--- Unsafe Query ---")
    try:
        unsafe_result = await Runner.run(Customer_Agent, "My password is 1234, please check my account", context=ctx)
        print("❌ Should not have passed:", unsafe_result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("🚫 Input blocked by guardrail.")
        print("Reason:", e)

if __name__ == "__main__":
    asyncio.run(main())