def Z(N, r, c):

    if N == 0:
        return 0

    half = 2 ** (N-1)

    if r < half and c < half: # 1사분면
        return Z(N-1, r, c)
    elif r < half and c >= half: # 2사분면
        return half * half + Z(N-1, r, c - half)
    elif r >= half and c < half: # 3사분면
        return 2 * half * half + Z(N-1, r - half, c)
    elif r >= half and c >= half: # 4사분면
        return 3 * half * half + Z(N-1, r - half, c - half)
    
N, r, c = map(int, input().split())

print(Z(N, r, c))