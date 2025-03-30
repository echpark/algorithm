from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                if ans[i]:
                    ans[i] = min(ans[i], ans[x] + 1)
                else:
                    ans[i] = ans[x] + 1

                visited[i] = True
                q.append(i)

N, M, K, X = map(int, input().split())

graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
ans = [0] * (N+1)
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)

bfs(X)

haveMin = False
for i in range(1, N+1):
    if ans[i] == K:
        print(i)
        haveMin = True

if not haveMin:
    print(-1)