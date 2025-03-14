C = int(input())
for i in range(C):
    mylist = list(map(int, input().split()))

    N = mylist.pop(0)

    average = sum(mylist)/N

    count = 0
    for score in mylist:
        if score > average:
            count += 1

    answer = count/N * 100

    print('{:.3f}'.format(answer), "%")