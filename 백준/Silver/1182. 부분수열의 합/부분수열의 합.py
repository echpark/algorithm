def dfs(n, idx, lst):
    global cnt

    if n == i:
        if sum(lst) == S:
            cnt += 1
        return

    for j in range(idx, N):
        dfs(n+1, j+1, lst + [arr[j]])

N, S = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
for i in range(1, N+1):
    dfs(0, 0,[])

print(cnt)