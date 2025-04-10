N = int(input())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

dp[0][0] = 1

for x in range(N):
    for y in range(N):

        if x == N-1 and y == N-1: # 마지막에 도착하면
            print(dp[N-1][N-1])
            exit()

        if dp[x][y] == 0:
            continue

        dx = [arr[x][y], 0]
        dy = [0, arr[x][y]]

        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                dp[nx][ny] += dp[x][y]