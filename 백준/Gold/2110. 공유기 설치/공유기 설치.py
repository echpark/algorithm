def canMake(d):
    last = arr[0]
    cnt = 1

    for i in range(1, N):
        if arr[i] - last >= d:
            cnt += 1
            last = arr[i]

        if cnt >= C:
            return True

    return False

def binarySearch():
    left = 1
    right = arr[-1] - arr[0]
    answer = 0

    while left <= right:
        mid = (left + right) // 2

        if canMake(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

N, C = map(int, input().split())
arr = []
for i in range(N):
    arr.append(int(input()))

arr.sort()

print(binarySearch())