N = int(input())

pos = [0] * N
flag_a = set()
flag_b = set()
flag_c = set()

count = 0

def put():
    global count
    count += 1

def set_queen(i):
    for j in range(N):
        if j not in flag_a and (i + j) not in flag_b and (i - j) not in flag_c:
            pos[i] = j
            if i == N - 1:
                put()
            else:
                flag_a.add(j)
                flag_b.add(i + j)
                flag_c.add(i - j)

                set_queen(i + 1)

                flag_a.remove(j)
                flag_b.remove(i + j)
                flag_c.remove(i - j)

set_queen(0)
print(count)