width, height = map(int, input().split(" "))

widthlist = [0, width]
heightlist = [0, height]

T = int(input())

for _ in range(T):
    how, cut = map(int, input().split(" "))
    if how == 0:
        heightlist.append(cut)
    else:
        widthlist.append(cut)

widthlist.sort()
heightlist.sort()

max_x = 0
for i in range(len(widthlist)-1):
    max_x = max(max_x, widthlist[i+1] - widthlist[i])

max_y = 0
for i in range(len(heightlist)-1):
    max_y = max(max_y, heightlist[i+1] - heightlist[i])

print(max_x * max_y)