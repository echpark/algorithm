N = int(input())

stk = []
for _ in range(N-1):
    h = int(input())
    stk.append(h)

cnt = 1
mynum = int(input())
for i in range(N-2, -1, -1):
    if stk[i] > mynum:
        mynum = stk[i]
        cnt += 1
    stk.pop()
print(cnt)