N = int(input())
heights = list(map(int, input().split()))
stk = []
answer = [0] * N

for i in range(N):
    while stk and stk[-1][1] < heights[i]:
        stk.pop()
    if stk:
        answer[i] = stk[-1][0]
    stk.append([i+1, heights[i]])

print(*answer)