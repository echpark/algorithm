def dfs(n, lst):
    global ans
    if n == N:
        differ = 0
        for i in range(0, N-1):
            differ += abs(lst[i] - lst[i + 1])
        ans = max(ans, differ)
        return
    for i in range(N):
        if not v[i]:
            v[i] = True
            dfs(n+1, lst + [A[i]])
            v[i] = False

N = int(input())
A = list(map(int, input().split(" ")))

ans = 0
v = [False] * N

dfs(0, [])
print(ans)