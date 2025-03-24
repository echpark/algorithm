T = int(input())

for _ in range(T):
    cmd = input()

    isCollect = True

    stk = []
    for str in cmd:
        if str == "(":
            stk.append(str)
        else:
            if stk:
                stk.pop()
            else:
                stk.append(str)
                break

    if stk:
        print("NO")
    else:
        print("YES")