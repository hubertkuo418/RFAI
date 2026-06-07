from services.agents.base_agent import BaseAgent


class Agent(BaseAgent):
    name = "research"

    def run(self, query: str) -> str:
        return f"[Research Agent] Processing: {query}"
