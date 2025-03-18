def hanoi(n, start, end, via):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, via, end)
    print(start, end)
    hanoi(n-1, via, end, start)

n = int(input())

print(2 ** n - 1)

if (n <= 20):
    hanoi(n, 1, 3, 2)