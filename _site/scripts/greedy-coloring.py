def greedy_coloring(graph, order):
    color = {}

    # Iterate through the vertices in the specified order
    for v in order:
        # Create a set of colors already used by the neighbors of v that are already colored
        used = {color[n] for n in graph[v] if n in color}
        c = 0
        # Find the smallest color that is not in the used set
        while c in used:
            c += 1

        # Assign the first available smallest color to the current vertex
        color[v] = c

    return color


graph = {
    'A':['B','C'],
    'B':['A','C'],
    'C':['A','B','D'],
    'D':['C']
}

print(greedy_coloring(graph, ['A','B','C','D']))