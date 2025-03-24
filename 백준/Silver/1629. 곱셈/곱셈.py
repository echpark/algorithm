# 모듈로 계산하는 함수
def mod_cal(x, y, z):
    return (x % z) * (y % z) % z

# a ** b % c를 구하는 함수
def power_mod(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        my = power_mod(a, b // 2, c)
        return mod_cal(my, my, c)
    else:
        nb = power_mod(a, b-1, c)
        return mod_cal(a, nb, c)

A, B, C = map(int, input().split())
result = power_mod(A, B, C)
print(result)