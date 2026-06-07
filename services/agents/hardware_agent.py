from services.agents.base_agent import BaseAgent


class Agent(BaseAgent):
    name = "hardware"

    def run(self, query: str) -> str:
        return f"[Hardware Agent] Processing: {query}"
