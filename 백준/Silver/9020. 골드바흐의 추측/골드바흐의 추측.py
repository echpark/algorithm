T = int(input())

def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num ** 1/2)+1):
            if num % i == 0:
                return False
        return True

for _ in range(T):
    m = int(input())
    n = m // 2

    for x in range(n, 1, -1):
        y = m - x
        if isPrime(x) and isPrime(y):
            print(x, y)
            break;