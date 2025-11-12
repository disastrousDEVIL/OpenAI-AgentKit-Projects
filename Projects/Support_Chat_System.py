# 💬 Project 2 — Support Chat System

# Concepts
# - Manager pattern
# - Multiple agents exposed as tools

# Scenario
# - Build a Customer Support Assistant with specialized sub-agents:
#   1) Booking agent — handles bookings
#   2) Refund agent — handles refunds
# - A front-desk agent routes user queries and uses the tools.

# Build Steps
# 1) Create `booking_agent` and `refund_agent` with short, clear instructions.
# 2) Expose both as tools inside `customer_agent`.
# 3) Test with “I want to cancel my ticket” and verify it routes to `refund_agent`.
# 4) Log which tool was used in each conversation.




from agents import Agent, Runner, ModelSettings, AgentHooks
import asyncio
from pydantic import BaseModel


class LoggingHooks(AgentHooks):
    async def on_tool_start(self,run,tool,input_data):
        print(f"Tool {tool.name} started with input {input_data}")
    async def on_tool_end(self,run,input_data,output_data,result):
        print(f"Ended tool execution with result {result}")


class BookingDetails(BaseModel):
    city: str
    checkin_date: str
    checkout_date: str
    confirmation_id: str

class RefundStatus(BaseModel):
    booking_id: str
    amount: float
    status: str

booking_agent=Agent(name="Booking Agent",instructions="You are a booking agent that books hotels for the user",output_type=BookingDetails)
refund_agent=Agent(name="Refund Agent",instructions="You are a refund agent that refunds the user for the hotel booking",output_type=RefundStatus)


# Implementing LoggingHooks to log the tool execution
hooks = LoggingHooks()


customer_agent=Agent(
    name="Customer Agent",
    instructions="You check for the users request and use the approprate tools provided to you",
    tools=[booking_agent.as_tool(
        tool_name="booking_expert",
        tool_description="Handles booking requests and questions related to booking"
    ),refund_agent.as_tool(
        tool_name="refund_expert",
        tool_description="Handles refund requests and questions related to refund"
    )],
    model_settings=ModelSettings(tool_choice="required"),
    tool_use_behavior="run_llm_again",
    hooks=hooks,
)

async def main():
    result=await Runner.run(customer_agent,"I want to book a hotel for my next trip to Tokyo")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
