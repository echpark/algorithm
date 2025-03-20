N = int(input())
arr = list(map(int, input().split()))

arr.sort()

left, right = 0, N - 1
min_diff = float('inf')
ans1, ans2 = 0, 0

while right > left:
    mix = arr[left] + arr[right]

    if min_diff > abs(mix):
        ans1, ans2 = arr[left], arr[right]
        min_diff = abs(mix)

    if mix < 0:
        left += 1
    else:
        right -= 1

print(ans1, ans2)