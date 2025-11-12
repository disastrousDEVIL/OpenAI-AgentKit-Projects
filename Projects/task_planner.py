# 🧩 Project 3 — Task Planner
#
# Concepts
# - Dynamic instructions
# - Context
# - Async context methods
#
# Scenario
# - A Personal Planner Agent greets the user, knows their name, and creates to-do lists based on their habits.
#
# Build Steps
# 1) Define a `UserContext` with `name`, `is_pro_user`, and `async fetch_recent_tasks()`.
# 2) Use dynamic instructions to generate prompts like: "User Krish is a pro user. Suggest tasks with time estimates."
# 3) Return a list of `TaskItem` Pydantic models.

from agents import Agent, RunContextWrapper
from pydantic import BaseModel
import asyncio
from agents import Runner

class TaskItem(BaseModel):
    task:str
    estimated_minutes:int
    priority:int

class UserContext(BaseModel):
    name:str
    is_pro_user:bool

    async def fetch_recent_tasks(self)->list[TaskItem]:
        await asyncio.sleep(0.3)
        return [TaskItem(task="Morning Workout",estimated_minutes=30,priority=1),
                TaskItem(task="Lunch with John",estimated_minutes=60,priority=2),
                TaskItem(task="Code Review",estimated_minutes=120,priority=3),
                TaskItem(task="Project Review",estimated_minutes=180,priority=4)]

def dynamic_instructions(context: RunContextWrapper[UserContext],agent:Agent[UserContext])->str:
    user=context.context
    status="a Pro user" if user.is_pro_user else "a regular user"
    return (f"The user's name is {user.name}, and they are {status}. "
        f"Use their recent tasks to plan the day efficiently. "
        "Always return a list of TaskItem objects with realistic time estimates (in minutes).")

planner_agent=Agent[UserContext](name="Task Planner",instructions=dynamic_instructions,output_type=list[TaskItem])

async def main():
    user_context=UserContext(name="John",is_pro_user=True)

    recent_tasks=await user_context.fetch_recent_tasks()
    print("Recent tasks:",recent_tasks)

    query="Plan my day with balanced work and rest"
    result=await Runner.run(planner_agent,query,context=user_context)

    print("\n Suggested To Do List:")
    for task in result.final_output:
        print(f"- {task.task} (Estimated: {task.estimated_minutes} minutes, Priority: {task.priority})")

if __name__=="__main__":
    asyncio.run(main())