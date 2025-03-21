def binarySearch():
    global answer

    left = 0
    right = max(budget)

    while left <= right:
        mid = (left + right) // 2  # 상한가

        if ispossible(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1


def ispossible(H):
    total = 0
    for i in range(N):
        if budget[i] >= H:
            total += H
        else:
            total += budget[i]

    if total <= M:
        return True

    return False

N = int(input())
budget = list(map(int, input().split()))
M = int(input())
answer = 0
binarySearch()

print(answer)