def binarySearch(target):
    left = 0
    right = N-1

    while left <= right:
        middle = (left + right) // 2
        if Nlist[middle] == target:
            return 1
        elif Nlist[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return 0

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))

Nlist.sort()

for card in Mlist:
    print(binarySearch(card))