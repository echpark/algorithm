import sys
input = sys.stdin.readline

N = int(input())

mylist = [0] * 10001

for _ in range(N):
    num = int(input())
    mylist[num] += 1

for i in range(10001):
    if mylist[i] != 0:
        for j in range(mylist[i]):
            print(i)