N = int(input())

def isHansu(num):
    if num < 100:
        return True
    elif num == 1000:
        return False
    else:
        mystr = str(num)
        mylist = list(mystr)
        a = int(mylist[0])
        b = int(mylist[1])
        c = int(mylist[2])

        if a - b == b - c:
            return True
        else:
            return False

count = 0

for i in range(0, N):
    if isHansu(i+1):
        count += 1

print(count)