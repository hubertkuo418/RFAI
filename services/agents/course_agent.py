from services.agents.base_agent import BaseAgent


class Agent(BaseAgent):
    name = "course"

    def run(self, query: str) -> str:
        return f"[Course Agent] Processing: {query}"
