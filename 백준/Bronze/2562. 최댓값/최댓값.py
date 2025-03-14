mylist = {}

maxNum = 0
for i in range(9):
    num = int(input())
    maxNum = max(maxNum, num)
    mylist[num] = i+1

print(maxNum)
print(mylist[maxNum])