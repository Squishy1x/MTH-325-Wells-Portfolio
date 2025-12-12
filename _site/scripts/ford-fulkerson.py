from collections import deque

def bfs(rg, s, t, parent):
    visited = [False]*len(rg)
    queue = deque([s])
    # Root node visited
    visited[s] = True

    while queue:
        u = queue.popleft()

        # Iterate over all possible neighbors
        for v,cap in enumerate(rg[u]):
            # If not visited AND there is capacity remaining from u to v
            if not visited[v] and cap > 0:
                visited[v] = True
                parent[v] = u
                queue.append(v)

    return visited[t]


def ford_fulkerson(graph, s, t):
    n = len(graph)
    # Residual graph
    rg = [row[:] for row in graph]
    # Parent array for bfs path
    parent = [-1]*n
    max_flow = 0

    # Repeat as long as an augmenting path can be found from s to t
    while bfs(rg,s,t,parent):
        path_flow = float('inf')
        v = t

        # Move backwards
        while v != s:
            u = parent[v]
            # Find the minimum capacity in the path
            path_flow = min(path_flow, rg[u][v])
            v = parent[v]

        # Update capacities
        v = t
        # Move backwards
        while v != s:
            u = parent[v]
            # Decrease
            rg[u][v] -= path_flow
            # Increase
            rg[v][u] += path_flow
            v = parent[v]

        # Add to max flow
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