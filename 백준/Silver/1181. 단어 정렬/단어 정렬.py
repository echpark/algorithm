N = int(input())

mylist = []
for i in range(N):
    word = input()

    if [len(word), word] not in mylist:
        mylist.append([len(word), word])

mylist.sort()

for a, b in mylist:
    print(b)