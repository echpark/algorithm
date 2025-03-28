from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    check[start] = True

    while q:
        x = q.popleft()
        for i in graph[x]:
            if check[i] == check[x]:
                return False
            if not visited[i]:
                visited[i] = True
                q.append(i)
                check[i] = not check[x]

    return True

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (V+1)
    check = [-1] * (V+1)

    isRight = True
    for i in range(1, V+1):
        if not visited[i]:
            if not bfs(i):
                isRight = False

    if isRight:
        print("YES")
    else:
        print("NO")