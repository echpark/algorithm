N = int(input())

stk = []

for _ in range(N):
    cmd = input()
    if cmd == "pop":
        if stk:
            print(stk.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(stk))
    elif cmd == "empty":
        if stk:
            print(0)
        else:
            print(1)
    elif cmd == "top":
        if stk:
            print(stk[-1])
        else:
            print(-1)
    else:
        _, num = cmd.split()
        stk.append(num)