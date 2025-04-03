N = int(input())

if N == 1:
    print(1)

else:
    dp = [0] * (N+1)

    num = 15746

    dp[1] = 1
    dp[2] = 2

    for i in range(3, N+1):
        dp[i] = ((dp[i-1] % num) + (dp[i-2] % num)) % num

    print(dp[N] % num)