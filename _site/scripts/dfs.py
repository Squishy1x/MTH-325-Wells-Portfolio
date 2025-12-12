def dfs(graph, start):
    visited = set()
    stack = [start]

    # While nodes in stack
    while stack:
        v = stack.pop()

        # If not visited
        if v not in visited:
            # Visit node
            visited.add(v)

            # Add neighbors to stack
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