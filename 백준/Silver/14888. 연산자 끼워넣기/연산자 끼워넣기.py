def dfs(depth, total, add, sub, mul, div):
    global min_val, max_val

    if depth == N:
        min_val = min(min_val, total)
        max_val = max(max_val, total)
        return

    num = A[depth]

    if add:
        dfs(depth+1, total+num, add-1, sub, mul, div)
    if sub:
        dfs(depth+1, total-num, add, sub-1, mul, div)
    if mul:
        dfs(depth+1, total*num, add, sub, mul-1, div)
    if div:
        if total < 0:
            dfs(depth+1, -((-total)//num), add, sub, mul, div-1)
        else:
            dfs(depth+1, total//num, add, sub, mul, div-1)

N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_val = float('inf')
max_val = float('-inf')

dfs(1, A[0], add, sub, mul, div)

print(max_val)
print(min_val)