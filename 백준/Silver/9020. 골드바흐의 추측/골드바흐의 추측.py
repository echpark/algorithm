T = int(input())

def isPrime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 1/2) + 1):
        if num % i == 0:
            return False
    return True

for i in range(T):
    M = int(input())
    N = M//2
    for j in range(N, 1, -1):
        if isPrime(j) and isPrime(M-j):
            print(j, M-j)
            break