T = int(input())

def isPrime(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num ** 1/2)+1):
            if num % i == 0:
                return False
        return True

primelist = []
for i in range(2, 10000):
    if isPrime(i):
        primelist.append(i)

for _ in range(T):

    n = int(input())

    difference = 10000
    answer1 = answer2 = 0
    for prime in primelist:
        if prime > n/2:
            break

        if (n - prime) in primelist:
            if abs(n - 2 * prime) < difference:
                difference = abs(n - 2 * prime)
                answer1 = min(prime, n - prime)
                answer2 = max(prime, n - prime)

    print(answer1, answer2)