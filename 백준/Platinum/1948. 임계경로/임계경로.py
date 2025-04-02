from collections import deque

def rev_topology_sort():
    times = [0] * (n+1)
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()

        for v, w in graph[now]:
            indegree[v] -= 1
            times[v] = max(times[v], times[now] + w)
            if indegree[v] == 0:
                q.append(v)

    return times

def bfs(start):
    q = deque()
    visited = [False] * (n+1)
    q.append(start)
    visited[start] = True
    cnt = 0

    while q:
        x = q.popleft()
        for u, w in rev_graph[x]:
            if times[u] + w == times[x]:
                cnt += 1
                if not visited[u]:
                    q.append(u)
                    visited[u] = True
    return cnt

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)] # 정방향 그래프
rev_graph = [[] for i in range(n+1)] # 역방향 그래프
indegree = [0] * (n + 1) # 진입차수

for _ in range(m):
    u, v, w = map(int, input().split())
    indegree[v] += 1
    graph[u].append((v, w))
    rev_graph[v].append((u, w))

start, end = map(int, input().split())


times = rev_topology_sort()
cnt = bfs(end)

print(times[end])
print(cnt)