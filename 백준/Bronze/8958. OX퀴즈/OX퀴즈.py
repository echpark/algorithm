T = int(input())

for i in range(T):
    mylist = list(input())
    count = 0
    score = 0
    for j in mylist:
        if j == 'O':
            count += 1
            score += count
        else:
            count = 0
    print(score)