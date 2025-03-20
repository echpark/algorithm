# 2025-03-20 시험

def isSum(n, arr):
    global cnt

    if n == i: # 종료 조건 : arr의 길이(n)가 개수가 목표(i)와 같을 때
        if sum(arr) == N: # 순열을 모두 더한 값이 N이라면
            cnt += 1
        return

    for j in range(1, 4): # 수는 1, 2, 3만 사용 가능
        isSum(n+1, arr + [j]) # 순열 생성

T = int(input())
for _ in range(T):
    N = int(input())
    cnt = 0 # 합이 N이 되는 순열의 개수
    for i in range(1, N+1): # 사용하는 수의 개수가 1개, 2개 ... N+1개
        isSum(0, [])

    print(cnt)