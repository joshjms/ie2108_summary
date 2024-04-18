# A disjoint set is a data structure used in Kruskal MST algorithm.

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)

def MST():
    # Number of vertices
    n = 4
    # Number of edges
    m = 5
    # Initialize a disjoint set
    dsu = DisjointSet(n)
    # Initialize the edges
    # edge = (node1, node2, weight)
    edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)] 
    # Sort the edges by weight (i.e. the third element of the tuple)
    edges.sort(key=lambda x: x[2]) 
    # Initialize the minimum spanning tree
    mst = []

    # Initially, assume all vertices belong in different sets
    # Each set has a parent (or representative) of that group
    # If two vertices are connected, they belong in the same set and has the same parent
    # We can find the parent of a vertex by calling dsu.find(u)
    # Initially, all vertices' parents are themselves (par[1] = 1, par[2] = 2, ...)
    # When we join two sets, we let the parent of one set to be the parent of the other set
    # (i.e. par[find(u)] = find(v))
    # If two vertices are in the same set, dsu.find(u) == dsu.find(v)
    # If two vertices are in different sets, dsu.find(u) != dsu.find(v)
    # We can join two sets by calling dsu.union(u, v)
    # If for edge (u, v) we have dsu.find(u) == dsu.find(v), we don't add the edge to the MST
    # because they are already connected and adding the edge will create a cycle

    for edge in edges:
        # If u and v are not connected yet, we connect them using a new edge that has the
        # smallest weight to connect both sets
        u, v, w = edge
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            mst.append(edge)
    return mst