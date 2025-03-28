from collections import deque

def dfs(node):
    visited[node] = True
    print(node, end = " ")
    for i in sorted(graph[node]):
        if not visited[i]:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        print(x, end = " ")
        for i in sorted(graph[x]):
            if not visited[i]:
                visited[i] = True
                q.append(i)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)