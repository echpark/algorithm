mylist = []

for _ in range(9):
    mylist.append(int(input()))

total = sum(mylist)

for i in range(9):
    for j in range(i+1, 9):
        one = mylist[i]
        two = mylist[j]
        if one + two == total - 100:
            mylist.remove(one)
            mylist.remove(two)

            mylist.sort()

            for i in mylist:
                print(i)
            exit()