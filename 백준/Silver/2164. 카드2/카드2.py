from collections import deque

N = int(input())
q = deque()
for i in range(N, 0, -1):
    q.append(i)

while len(q) != 1:
    q.pop()
    last = q.pop()
    q.appendleft(last)

print(*q)