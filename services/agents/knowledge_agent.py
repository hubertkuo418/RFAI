from services.agents.base_agent import BaseAgent


class Agent(BaseAgent):
    name = "knowledge"

    def run(self, query: str) -> str:
        return f"[Knowledge Agent] Processing: {query}"
