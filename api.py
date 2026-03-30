"""FastAPI HTTP layer exposing lead-related endpoints for the tea/chai agent."""

from fastapi import FastAPI
from agent import chai_ai_agent

app = FastAPI()


@app.get("/leads")
def get_leads(city: str):
    """Return leads for the given city by delegating to the chai AI agent."""
    return chai_ai_agent(city)
