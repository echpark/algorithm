from collections import deque

def topology_sort():
    q = deque()
    count = [[0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            count[i][i] = 1

    while q:
        now = q.popleft()

        for next_loc, next_cnt in graph[now]:
            for i in range(1, N+1):
                count[next_loc][i] += count[now][i] * next_cnt

            indegree[next_loc] -= 1
            if indegree[next_loc] == 0:
                q.append(next_loc)

    for i in range(1, N):
        if count[N][i] > 0:
            print(i, count[N][i])

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N + 1)

for _ in range(M):
    X, Y, K = map(int, input().split())
    indegree[X] += 1
    graph[Y].append((X, K))

topology_sort()