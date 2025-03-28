import sys
sys.setrecursionlimit(10**5)

# 유니온파인드 알고리즘
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size+1))

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

# 크루스칼 알고리즘
def kruskal(edges, num_nodes):
    uf = UnionFind(num_nodes)
    mst_weight = 0
    edges.sort(key=lambda x: x[2])  # 가중치로 정렬

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += weight

    return mst_weight

# 입력
V, E = map(int, sys.stdin.readline().split())
edges = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A, B, C))

print(kruskal(edges, V))