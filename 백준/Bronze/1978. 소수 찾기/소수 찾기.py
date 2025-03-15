N = int(input())
mylist = list(map(int, input().split()))

def isPrime(number):
    if number < 2:
        return 0
    else:
        for i in range(2, number):
            if number % i == 0:
                return 0
        return 1

count = 0
for number in mylist:
    count += isPrime(number)

print(count)