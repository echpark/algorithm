from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    documents = list(map(int, input().split()))
    idxQ = deque()
    valQ = deque()

    for i in range(N):
        idxQ.append(i)
        valQ.append(documents[i])

    cnt = 0
    while idxQ:
        maxVal = max(valQ)

        idx = idxQ.popleft()
        val = valQ.popleft()

        if val == maxVal:
            cnt += 1
            if idx == M:
                break
        else:
            idxQ.append(idx)
            valQ.append(val)

    print(cnt)