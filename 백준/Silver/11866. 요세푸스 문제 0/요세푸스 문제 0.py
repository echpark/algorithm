from collections import deque

N, K = map(int, input().split())

q = deque([i+1 for i in range(N)])
ans = []
cnt = 1

while q:
    num = q.popleft()
    if cnt == K:
        ans.append(num)
        cnt = 1
    else:
        q.append(num)
        cnt += 1

print("<", end = "")
for i in range(N-1):
    print(ans[i], end = ", ")
print(f"{ans[-1]}>")