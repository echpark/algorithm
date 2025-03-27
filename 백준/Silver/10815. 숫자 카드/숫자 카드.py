N = int(input())
Ncards = set(list(map(int, input().split()))) # set: O(1)
M = int(input())
Mcards = list(map(int, input().split()))

ans = []
for target in Mcards:
    if target in Ncards:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)