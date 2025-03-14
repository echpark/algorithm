N, X = map(int, input().split())
A = list(map(int, input().split()))

mylist = []

for i in A:
    if i < X:
        mylist.append(i)

for i in mylist:
    print(i, end=" ")