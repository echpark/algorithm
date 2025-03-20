def findx(target):
    left = 0
    right = N-1

    while True:
        if left > right:
            break

        middle = (left + right) // 2

        if A[middle] == target:
            return 1
        elif A[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return 0

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for i in range(M):
    target = B[i]
    print(findx(target))