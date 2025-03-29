from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y):
    q = deque()
    q.append((start_x, start_y))
    graph[start_x][start_y] = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx == N-1 and ny == M-1:
                return graph[x][y] + 1

            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue

            if graph[nx][ny] != 1:
                continue

            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

print(bfs(0, 0))