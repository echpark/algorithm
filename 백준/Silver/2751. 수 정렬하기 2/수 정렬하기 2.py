import sys
input = sys.stdin.readline

N = int(input())

mylist = []
for i in range(N):
    num = int(input())
    mylist.append(num)

mylist.sort()

for i in mylist:
    print(i)