def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            for neighbor in graph[v]:
                stack.append(neighbor)

    return visited


graph = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A'],
    'D': ['B']
}

print(dfs(graph, 'A'))