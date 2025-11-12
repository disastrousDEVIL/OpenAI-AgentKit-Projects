# 🧠 Project (Essential) — Academic Guardrail System
#
# Concepts
# - Input guardrails
# - Handoffs
# - Guardrail functions
#
# Scenario
# - A homework assistant validates if a question is academic, then routes to:
#   1) MathAgent — math
#   2) HistoryAgent — history
#   3) ScienceAgent — science
# - A GuardrailAgent checks academic-ness and can trip a stop if not academic.
#
# Build Steps
# 1) Define a Pydantic model `Homework` with: `isHomework: bool`, `reading: str`.
# 2) Create `math_agent`, `history_agent`, and `science_agent` with names, handoff descriptions, and clear subject instructions.
# 3) Add `guardrail_agent` that evaluates the question and returns a `Homework` object.
# 4) Implement `check_homework(ctx, agent, input_data)` to run the guardrail and return `GuardrailFunctionOutput` with `tripwire_triggered = not final_output.isHomework`.
# 5) Build `main_agent` that can hand off to the three subject agents and uses `InputGuardrail(check_homework)`.
# 6) Test with a non-academic input (e.g., "how are you going on") and handle `InputGuardrailTripwireTriggered` to print "Guardrail triggered".

from agents import Agent, GuardrailFunctionOutput,InputGuardrail,Runner,InputGuardrailTripwireTriggered
import asyncio
from pydantic import BaseModel

class Homework(BaseModel):
    isHomework:bool
    reading:str

math_agent=Agent(name="Math guide",handoff_description="A helpful assistant that can answer questions and help with math problems",instructions="A helpful assistant that can answer questions and help with math problems")
history_agent=Agent(name="History guide",handoff_description="A helpful assistant that can answer questions and help with history problems",instructions="A helpful assistant that can answer questions and help with history problems")
science_agent=Agent(name="Science guide",handoff_description="A helpful assistant that can answer questions and help with science problems",instructions="A helpful assistant that can answer questions and help with science problems")

guardrail_agent=Agent(name="Guardrail agent",instructions="A helpful assistant that can check if the user is asking academic reateds questions only",output_type=Homework)
#Adding a guardrail function to the main agent
async def check_homework(ctx,agent,input_data):
    result=await Runner.run(guardrail_agent,input_data,context=ctx.context)
    final_output=result.final_output
    return GuardrailFunctionOutput(output_info=final_output,tripwire_triggered=not final_output.isHomework)


main_agent=Agent(name="Main agent",instructions="A helpful assistant that can answer questions and help with math, history, and science problems",handoffs=[math_agent,history_agent,science_agent],input_guardrails=[InputGuardrail(guardrail_function=check_homework)])


async def main():
    try:
        result=await Runner.run(main_agent,"how are you goin on")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("Guardrail triggered:",e)

if __name__ == "__main__":
    asyncio.run(main())