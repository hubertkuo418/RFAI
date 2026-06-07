from services.agents.base_agent import BaseAgent


class Agent(BaseAgent):
    name = "writing"

    def run(self, query: str) -> str:
        return f"[Writing Agent] Processing: {query}"
