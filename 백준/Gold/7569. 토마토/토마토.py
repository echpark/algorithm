from collections import deque

def bfs():
    global tomatos, q

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]

    while q:
        x, y, z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or ny < 0 or nz < 0 or nx >= H or ny >= M or nz >= N:
                continue

            if tomatos[nx][ny][nz] == 0:
                tomatos[nx][ny][nz] = tomatos[x][y][z] + 1
                q.append((nx, ny, nz))

N, M, H = map(int, input().split())

tomatos = []
for i in range(H):
    arr = []
    for j in range(M):
        row = list(map(int, input().split()))
        arr.append(row)
    tomatos.append(arr)

q = deque()
for i in range(H):
    for j in range(M):
        for k in range(N):
            if tomatos[i][j][k] == 1: # 토마토가 익었으면
                q.append((i, j, k))

bfs()

isRipe = True
day = 0

for i in range(H):
    for j in range(M):
        for k in range(N):
            if tomatos[i][j][k] == 0:
                isRipe = False
            day = max(day, tomatos[i][j][k])

if isRipe:
    print(day - 1)
else:
    print(-1)