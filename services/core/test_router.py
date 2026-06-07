from services.core.router import route


task = {
    "workspace": "research",
    "query": "Find Transformer quantization papers"
}

result = route(task)

print(result)
