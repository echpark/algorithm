from collections import Counter
from functools import reduce 

def solution(clothes):
    cnt = Counter([type for name, type in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1)
    return answer - 1