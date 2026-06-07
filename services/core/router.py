def route(workspace: str):

    if workspace == "research":
        return "paper_agent"

    elif workspace == "course":
        return "course_agent"

    elif workspace == "hardware":
        return "hardware_agent"

    return "unknown"