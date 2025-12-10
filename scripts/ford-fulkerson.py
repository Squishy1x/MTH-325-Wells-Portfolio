from collections import deque

def bfs(rg, s, t, parent):
    visited = [False]*len(rg)
    queue = deque([s])
    visited[s] = True

    while queue:
        u = queue.popleft()
        for v,cap in enumerate(rg[u]):
            if not visited[v] and cap > 0:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    return visited[t]


def ford_fulkerson(graph, s, t):
    n = len(graph)
    rg = [row[:] for row in graph]
    parent = [-1]*n
    max_flow = 0

    while bfs(rg,s,t,parent):
        path_flow = float('inf')
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, rg[u][v])
            v = parent[v]

        v = t
        while v != s:
            u = parent[v]
            rg[u][v] -= path_flow
            rg[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow


graph = [
    [0,16,13,0,0,0],
    [0,0,10,12,0,0],
    [0,4,0,0,14,0],
    [0,0,9,0,0,20],
    [0,0,0,7,0,4],
    [0,0,0,0,0,0]
]

print(ford_fulkerson(graph, 0, 5))