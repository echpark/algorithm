from collections import deque

N = int(input()) # 보드 크기
K = int(input()) # 사과 개수

apples = set() # 사과의 위치 저장 (set으로 빠른 탐색)
for _ in range(K):
    row, col = map(int, input().split())
    apples.add((row, col))

L = int(input())
moves = deque() # 방향 전환
for _ in range(L):
    X, C = input().split()
    moves.append((int(X), C))

# 초기 상태
snake = deque([(1, 1)]) # 뱀의 몸
i = 1 # 시작 방향
# 시계 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

second = 0

while True:
    second += 1

    # 현재 방향으로 이동
    x, y = snake[-1]
    nx = x + dx[i]
    ny = y + dy[i]
    head = (nx, ny)

    # 종료 조건: 벽 또는 자기 몸과 충돌
    if not (1 <= nx <= N and 1 <= ny <= N) or head in snake:
        break

    # 머리를 앞으로 이동
    snake.append(head)

    # 사과가 있다면 꼬리는 그대로 (길이 증가)
    if head in apples:
        apples.remove(head)
    else:
        snake.popleft() # 사과 없으면 꼬리 제거

    # 방향 전환
    if moves and second == moves[0][0]:
        _, c = moves.popleft()
        if c == 'L':
            i = (i - 1) % 4 # 왼쪽 회전
        else:
            i = (i + 1) % 4

print(second)