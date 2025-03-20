def cutTrees(H):
    global cnt

    for i in range(N):
        if heights[i] - H > 0:
            cnt += (heights[i] - H)

N, M = map(int, input().split())
heights = list(map(int, input().split()))

left = 0
right = max(heights)

while True:
    H = (left + right) // 2

    if left > right:
        print(H)
        break

    cnt = 0
    cutTrees(H)

    if cnt == M:
        print(H)
        break
    elif cnt > M:
        left = H + 1
    else:
        right = H - 1