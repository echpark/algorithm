K = int(input())
stk = []
for _ in range(K):
    cmd = int(input())

    if cmd == 0:
        stk.pop()
    else:
        stk.append(cmd)

print(sum(stk))