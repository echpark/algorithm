def dfs(node):
    global ans

    ans += 1
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)

N = int(input())
T = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(T):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

ans = 0
visited = [False] * (N+1)
dfs(1)

print(ans-1)