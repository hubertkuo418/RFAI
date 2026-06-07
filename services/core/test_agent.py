from services.core.agent_registry import AGENTS

agent = AGENTS["paper"]

result = agent.run(
    "Find papers about transformer quantization"
)

print(result)
