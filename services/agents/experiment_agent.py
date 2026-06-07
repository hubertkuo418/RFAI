from services.agents.base_agent import BaseAgent


class Agent(BaseAgent):
    name = "experiment"

    def run(self, query: str) -> str:
        return f"[Experiment Agent] Processing: {query}"
