# ⚙️ Project 8 — Safe Tech Support Assistant
#
# Concepts
# - Guardrails, context, sanitization
#
# Scenario
# - Tech support for install/troubleshoot/bugs with safety constraints.
#
# Build Steps
# 1) Define `UserContext` (experience_level, platform).
# 2) `tech_support_agent` uses dynamic instructions from context.
# 3) Input guardrail blocks dangerous commands/credentials.
# 4) Optional cleaner replaces unsafe commands with placeholders.

from agents import Agent,Runner, InputGuardrail, GuardrailFunctionOutput
import asyncio
from dataclasses import dataclass
from typing_extensions import Literal

@dataclass
class UserContext:
    experience_level:Literal["beginner","intermediate","advanced"]
    platform:Literal["windows","mac","linux"]

def dynamic_instructions(context:UserContext,agent:Agent):
    experience_level=context.context.experience_level
    platform=context.context.platform
    return (f"You are a tech support assistant that can help with {experience_level} users with {platform} platform."
    "For beginner users, provide simple explanations and step-by-step guides."
    "For intermediate users, provide more detailed explanations and troubleshooting tips."
    "For advanced users, provide technical solutions and advanced troubleshooting tips."
    "Asnwer only for the experience level and platform of the user specified."
    )


BANNED_PHRASES = ["rm -rf", "sudo", "format", "shutdown", "delete system32", "password", "API key", "token"]


def output_guardrail(context,agent,input_data:str)->GuardrailFunctionOutput:
    text=input_data.lower()
    for phrase in BANNED_PHRASES:
        if phrase in text:
            return GuardrailFunctionOutput(output_info=False,tripwire_triggered=True)
    return GuardrailFunctionOutput(output_info=True,tripwire_triggered=False)


tech_support_agent=Agent[UserContext](name="tech support agent",instructions=dynamic_instructions,output_type=str,input_guardrails=[InputGuardrail(guardrail_function=output_guardrail)])

async def main():
    ctx=UserContext(experience_level="beginner",platform="windows")
    result=await Runner.run(tech_support_agent,"How do I make laptop dark mode?",context=ctx)
    if result.final_output:
        print("Safe output",result.final_output)
    else:
        print("Output blocked by guardrail")

if __name__ == "__main__":
    asyncio.run(main())