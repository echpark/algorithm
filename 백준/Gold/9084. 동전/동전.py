T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    dp = [[0] * (M+1) for _ in range(N)]

    for i in range(N):
        dp[i][0] = 1

        for j in range(1, M+1):
            if i > 0:
                dp[i][j] += dp[i-1][j]

            if j >= arr[i]:
                dp[i][j] += dp[i][j - arr[i]]

    print(dp[N-1][M])