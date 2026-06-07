from services.agents.base_agent import BaseAgent


class Agent(BaseAgent):
    name = "paper"

    def run(self, query: str) -> str:
        return f"[Paper Agent] Processing: {query}"
