def solution(nums):
    len1 = len(nums)//2   # 선택 가능한 수
    len2 = len(list(set(nums))) # 폰켓몬의 종류 수
    
    if len1 > len2:
        ans = len2
    else:
        ans = len1
    return ans