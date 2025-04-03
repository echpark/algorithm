from collections import deque

def bfs(sx, sy): # 시작 위치 인자값
    q = deque()
    q.append((sx, sy))
    graph[sx][sy] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0 # 방문 처리
                q.append((nx, ny))
                cnt += 1

    return cnt

N = int(input())

graph = []
for _ in range(N):
    arr = list(map(int, input()))
    graph.append(arr)

total = 0 # 총 단지 수
house_cnt = [] # 각 단지내 집의 수
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 방문하지 않았으면
            total += 1
            house_cnt.append(bfs(i, j))

print(total)

for num in sorted(house_cnt): # 오름차순으로 정렬
    print(num)