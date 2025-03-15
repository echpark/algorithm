A = int(input())
B = int(input())
C = int(input())

mylist = list(str(A*B*C))

for i in range(0, 10):
    print(mylist.count(str(i)))