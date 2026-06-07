from services.agents.paper_agent import Agent as PaperAgent
from services.agents.research_agent import Agent as ResearchAgent
from services.agents.writing_agent import Agent as WritingAgent
from services.agents.course_agent import Agent as CourseAgent
from services.agents.knowledge_agent import Agent as KnowledgeAgent
from services.agents.hardware_agent import Agent as HardwareAgent
from services.agents.experiment_agent import Agent as ExperimentAgent


AGENTS = {
    "paper": PaperAgent(),
    "research": ResearchAgent(),
    "writing": WritingAgent(),
    "course": CourseAgent(),
    "knowledge": KnowledgeAgent(),
    "hardware": HardwareAgent(),
    "experiment": ExperimentAgent(),
}
