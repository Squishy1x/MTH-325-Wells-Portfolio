class UnionFind:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        self.p[ra] = rb


def kruskal(edges, n):
    edges.sort()
    uf = UnionFind(n)
    mst = []

    for w,u,v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
            mst.append((u,v,w))

    return mst


edges = [(1,0,1),(4,0,2),(2,1,2),(5,1,3),(1,2,3)]

print(kruskal(edges, 4))