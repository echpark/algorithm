N = int(input())

if N == 1:
    print(1)

else:
    a, b = 1, 2

    for i in range(3, N+1):
        a, b = b, (a+b) % 15746

    print(b)