# 🧠 Project 1 — Smart Weather Concierge
#
# Concepts
# - Basic agent
# - Function tools
# - Forced tool use
# - Structured output
#
# Scenario
# - Build a Weather Concierge Agent that takes natural language and returns a structured weather report.
#
# Build Steps
# 1) Write a @function_tool `get_weather(city: str)` returning fake data (temperature, humidity).
# 2) Wrap it inside an Agent that uses `run_llm_again`.
# 3) Upgrade to `output_type=WeatherReport(BaseModel)` — include city, temp, humidity, condition.
# 4) Add `ModelSettings(tool_choice="required")` so the tool must be used.
# 5) Test with “How’s Mumbai today?” and “Tell me about Goa tomorrow.”

from agents import Agent, Runner, function_tool, ModelSettings
import asyncio
from pydantic import BaseModel
import random

class WeatherReport(BaseModel):
    city: str
    weather: str
    temperature: float

@function_tool
def get_weather(city: str) -> WeatherReport:
    conditions = ["Sunny", "Rainy", "Partly Cloudy", "Humid"]
    return WeatherReport(
        city=city,
        weather=random.choice(conditions),
        temperature=round(random.uniform(20, 36), 1)
    )

weather_agent=Agent(
    name="Weather agent",
    instructions="You are a weather agent that returns weather report of the city provided by the user",
    tools=[get_weather],
    output_type=WeatherReport,
    model_settings=ModelSettings(tool_choice="required"),
    tool_use_behavior="run_llm_again"
)

async def main():
    result=await Runner.run(weather_agent,"How’s Mumbai today?")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

#Answer with keeping ModelSettings(tool_choice="required")
# (.venv) PS C:\Users\newma\Desktop\openai_agent_sdk\basics> python -m Smart_Weather_Concierge
# city='Mumbai' weather='Partly Cloudy' temperature=31.0

#Answer with keeping ModelSettings(tool_choice="none")
# (.venv) PS C:\Users\newma\Desktop\openai_agent_sdk\basics> python -m Smart_Weather_Concierge
# city='mumbai' weather='humid' temperature=35.0