from router import route_task


task = {
    "workspace": "research",
    "query": "Find Transformer quantization papers"
}

result = route_task(task)

print(result)