# Detect cycles
class UnionFind:
    def __init__(self, n):
        # Each node is its own parent
        self.p = list(range(n))

    # Finds the root of the set containing element
    def find(self, x):
        # If x is not the root, recursively find the root
        if self.p[x] != x:
            # Set x's parent directly to the root
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        # Find root of a and b
        ra = self.find(a)
        rb = self.find(b)
        # If they are not already in the same set, merge them
        self.p[ra] = rb


def kruskal(edges, n):
    edges.sort()
    #Init
    uf = UnionFind(n)
    # Store MST edges
    mst = []

    # Iterate through all edges in increasing order of weight
    for w,u,v in edges:
        # Check cycle
        if uf.find(u) != uf.find(v):
            uf.union(u,v)
            mst.append((u,v,w))

    return mst


edges = [(1,0,1),(4,0,2),(2,1,2),(5,1,3),(1,2,3)]

print(kruskal(edges, 4))