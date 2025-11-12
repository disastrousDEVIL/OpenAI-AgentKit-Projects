# 🎟 Project 4 — Cinema Chat
#
# Concepts
# - Structured outputs
# - StopAtTools
# - Custom tool handler
#
# Scenario
# - Build a Movie Ticket Agent that:
#   1) Searches movies (`get_movies` tool)
#   2) Books tickets (`book_ticket` tool)
# - If the movie is found, stop immediately with that tool result.
#
# Steps
# 1) Create both tools.
# 2) Use `StopAtTools(stop_at_tool_names=["get_movies"])`.
# 3) Optionally add `custom_tool_handler` to block genre “Horror” with: "Not available at this time".

from agents import Agent,Runner, function_tool
from pydantic import BaseModel
import random
import asyncio

class Movie(BaseModel):
    title:str
    genre:str
    rating:float
    showtimes:list[str]

class TicketConfirmation(BaseModel):
    movie:str
    showtime:str
    seat:str
    price:float
    status:str

@function_tool
def get_movies(name:str)->Movie:
    fake_db={
        "Inception": ("Sci-Fi", 9.0, ["1:00 PM", "4:00 PM", "9:00 PM"]),
        "Interstellar": ("Sci-Fi", 8.7, ["12:00 PM", "6:00 PM"]),
        "The Conjuring": ("Horror", 7.5, ["2:00 PM", "8:00 PM"]),
        "The Dark Knight": ("Action", 9.0, ["1:00 PM", "4:00 PM", "9:00 PM"]),
        "The Godfather": ("Crime", 9.2, ["12:00 PM", "6:00 PM"]),
        "The Lord of the Rings": ("Fantasy", 8.8, ["2:00 PM", "8:00 PM"]),
        "The Hobbit": ("Fantasy", 8.5, ["1:00 PM", "4:00 PM", "9:00 PM"]),
        "The Matrix": ("Sci-Fi", 8.9, ["12:00 PM", "6:00 PM"]),
        "The Matrix Reloaded": ("Sci-Fi", 8.8, ["2:00 PM", "8:00 PM"]),
        "The Matrix Revolutions": ("Sci-Fi", 8.7, ["1:00 PM", "4:00 PM", "9:00 PM"]),
        }
    if name not in fake_db:
        raise ValueError(f"Movie {name} not found")
    genre,rating,showtimes=fake_db[name]
    return Movie(title=name,genre=genre,rating=rating,showtimes=showtimes)

@function_tool
def book_ticket(movie: str, showtime: str) -> TicketConfirmation:
    """Book a ticket for a given movie and showtime."""
    return TicketConfirmation(
        movie=movie,
        showtime=showtime,
        seat=random.choice(["A1", "B2", "C3", "D4"]),
        price=250.0,
        status="Confirmed"
    )

movie_agent=Agent(name="Movie Agent",instructions="You are a movie agent that returns the movie details",tools=[get_movies],output_type=Movie)
ticket_agent=Agent(name="Ticket Agent",instructions="You are a ticket agent that books the ticket for the user",tools=[book_ticket],output_type=TicketConfirmation)


async def main():
    print("🎬 Searching for movie...")
    result = await Runner.run(movie_agent, "I want to book a ticket for Inception")
    print("\n🎥 Movie found:")
    print(result.final_output)

    print("\n🎟 Booking ticket...")
    ticket = await Runner.run(ticket_agent, "Book a 4:00 PM ticket for Inception")
    print("\n✅ Ticket confirmed:")
    print(ticket.final_output)


if __name__ == "__main__":
    asyncio.run(main())