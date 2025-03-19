N = input() # N = '1'

if len(N) == 1:
    N = '0' + N

cnt = 0

def letscnt(num): # num = '1'
    global cnt

    if num == N and cnt > 0:
        return

    mysum = str(int(num[0]) + int(num[1])) # mysum = '1'
    if len(mysum) == 1:
        mysum = '0' + mysum # mysum = '01'
    newNum = num[1] + mysum[1] # newNum = '11'
    cnt += 1

    letscnt(newNum)

letscnt(N)
print(cnt)