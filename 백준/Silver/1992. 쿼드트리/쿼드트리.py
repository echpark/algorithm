N = int(input())

arr = []
for i in range(N):
    arr.append(list((map(int, input()))))

def devide(N, a, b, c, d):

    half = N//2

    allwhite = True
    allblack = True

    for i in range(a, b):
        for j in range(c, d):
            if arr[i][j] == 1:
                allwhite = False
            else:
                allblack = False

    if allwhite:
        print(0, end = "")
        return
    elif allblack:
        print(1, end = "")
        return
    else:
        print("(", end = "")
        devide(half, a, a+half, c, c+half)
        devide(half, a, a+half, c+half, d)
        devide(half, a+half, b, c, c+half)
        devide(half, a+half, b, c+half, d)
        print(")", end = "")
        
devide(N, 0, N, 0, N)