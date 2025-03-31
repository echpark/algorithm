import heapq

def dijkstra():
    dist = [[float('inf')] * n for _ in range(n)]

    dist[0][0] = 0 # 시작 지점 0으로 초기화

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    pq = [(0, 0, 0)] # 비용, x, y

    while pq:
        cost, x, y = heapq.heappop(pq)

        if dist[x][y] < cost: # 더 작은 비용이 있으면 스킵
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 다음 방이 흰 방이면 0, 검은 방이면 1
            next_cost = cost + (1 if rooms[nx][ny] == 0 else 0)

            if dist[nx][ny] > next_cost:
                dist[nx][ny] = next_cost
                heapq.heappush(pq, (next_cost, nx, ny))

    return dist[n - 1][n - 1]

n = int(input())

rooms = []
for _ in range(n):
    rooms.append(list(map(int, input())))

print(dijkstra())