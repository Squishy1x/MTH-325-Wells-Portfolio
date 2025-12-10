def greedy_coloring(graph, order):
    color = {}

    for v in order:
        used = {color[n] for n in graph[v] if n in color}
        c = 0
        while c in used:
            c += 1
        color[v] = c

    return color


graph = {
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B','D'],
    'D':['C']
}

print(greedy_coloring(graph, ['A','B','C','D']))