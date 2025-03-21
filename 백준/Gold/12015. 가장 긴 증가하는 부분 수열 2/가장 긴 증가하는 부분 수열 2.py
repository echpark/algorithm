import bisect

# mid 길이의 증가하는 부분 수열이 존재하는지 확인
def canMake(mid):
    lst = []

    for x in A:
        pos = bisect.bisect_left(lst, x)

        if pos == len(lst):
            lst.append(x)
        else:
            lst[pos] = x

        if len(lst) == mid:
            return True

    return False

# 가장 긴 증가하는 부분 수열의 길이를 이진탐색으로 찾음
def binarySearch():
    left = 1
    right = len(A)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if canMake(mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    return answer

N = int(input())
A = list(map(int, input().split()))
print(binarySearch())