n = int(input())

num = 100001
dp = [0] * num
dp[2], dp[4] = 1, 2
dp[5], dp[6], dp[7], dp[8], dp[9] = 1, 3, 2, 4, 3

for i in range(10, num):
    dp[i] = dp[i-5] + 1

if dp[n] == 0:
    print(-1)
else:
    print(dp[n])