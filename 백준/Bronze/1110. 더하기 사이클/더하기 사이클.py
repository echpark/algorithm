# 2025-03-20 시험

def findcycle(num):
    global cnt

    # 종료조건 : 처음 주어진 수와 재귀로 들어온 수가 같으면 종료 (첫 호출 제외)
    if cnt > 0 and int(N) == int(num):
        return

    # 들어온 수의 자리수를 모두 더한 수
    plusnum = 0
    for i in range(len(num)): # 자리수만큼 돌리면서 합을 구함
        plusnum += int(num[i])

    newnum = str(int(num) % 10) + str(plusnum % 10) # 문자열로 만들어 단순 합침
    cnt += 1 # 사이클이 한 번 도므로 cnt += 1
    findcycle(newnum) # 종료조건을 만족하지 못했으므로 재귀 호출

N = input() # 문자열로 수를 받음
cnt = 0

findcycle(N)
print(cnt)