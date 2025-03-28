class UnionFind:
    def __init__(self, size):
        self.parent = list(range(N+1))

    def find(self, u):
        root = u
        while self.parent[root] != root:
            root = self.parent[root]

        while self.parent[u] != u:
            parent_a = self.parent[u]
            self.parent[u] = root
            u = self.parent[u]

        return root

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_u] = root_v

N, M = map(int, input().split())
my = UnionFind(N)
for _ in range(M):
    u, v = map(int, input().split())
    my.union(u, v)

roots = set()
for i in range(1, N+1):
    roots.add(my.find(i))

print(len(roots))