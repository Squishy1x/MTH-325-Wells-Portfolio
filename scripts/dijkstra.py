import heapq

def dijkstra(graph, start):
    dist = {v: float('inf') for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        curr_dist, u = heapq.heappop(pq)

        for v, w in graph[u]:
            new_dist = curr_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


graph = {
    'A':[('B',1),('C',4)],
    'B':[('C',2),('D',5)],
    'C':[('D',1)],
    'D':[]
}

print(dijkstra(graph, 'A'))