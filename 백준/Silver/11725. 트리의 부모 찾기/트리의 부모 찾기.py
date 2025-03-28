from collections import deque

N = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = [0] * (N+1)
visited = [False] * (N+1)
q = deque()

visited[1] = True
q.append(1)

while q:
    x = q.popleft()
    for i in graph[x]:
        if not visited[i]:
            visited[i] = True
            ans[i] = x
            q.append(i)

for i in range(2, N+1):
    print(ans[i])