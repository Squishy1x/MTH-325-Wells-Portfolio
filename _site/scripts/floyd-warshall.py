INF = float('inf')

graph = [
    [0,3,INF,7],
    [8,0,2,INF],
    [5,INF,0,1],
    [2,INF,INF,0]
]

def floyd_warshall(dist):
    n = len(dist)

    # Intermediate vertices
    for k in range(n):
        # Starting vertex
        for i in range(n):
            # Ending vertex
            for j in range(n):
                # Relaxation
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist


print(floyd_warshall(graph))