from collections import deque

def bfs(sx, sy):
    visited = [[-1] * C for _ in range(R)]
    visited[sx][sy] = 0

    q = deque() # 고슴도치의 이동
    q.append((sx, sy))
    map[sx][sy] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        # 물 퍼트리기
        for _ in range(len(q2)):
            x2, y2 = q2.popleft()

            for i in range(4):
                nx2 = x2 + dx[i]
                ny2 = y2 + dy[i]

                if 0 <= nx2 < R and 0 <= ny2 < C and map[nx2][ny2] == '.':
                    map[nx2][ny2] = '*'
                    q2.append((nx2, ny2))
        
        # 고슴도치 이동
        for _ in range(len(q)):
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < R and 0 <= ny < C:
                    if map[nx][ny] == 'D': # 비버의 굴을 찾음
                        return visited[x][y] + 1

                    if map[nx][ny] == '.' and visited[nx][ny] == -1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))

    return "KAKTUS"

R, C = map(int, input().split())
map = []
q2 = deque() # 물 위치 저장
mx, my = 0, 0 # 고슴도치 위치
for i in range(R):
    row = list(input())
    for j in range(C):
        if row[j] == "S":
            mx, my = i, j
            row[j] = '.'
        elif row[j] == '*':
            q2.append((i, j))
    map.append(row)

print(bfs(mx, my))