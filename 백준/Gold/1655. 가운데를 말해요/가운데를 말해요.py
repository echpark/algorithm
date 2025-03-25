import heapq
import sys
input = sys.stdin.readline

N = int(input())

maxHeap = [] # 최대 힙, 중간값과 같거나 중간값보다 작은 숫자들을 저장
minHeap = [] # 최소 힙, 중간값보다 큰 숫자들을 저장

for i in range(N):
    num = int(input())

    # 1. 우선 최대 힙에 넣음 (작은 쪽에 넣음)
    heapq.heappush(maxHeap, -num)

    # 2. 최대 힙의 루트보다 더 큰 값은 최소 힙으로 이동
    if minHeap and -maxHeap[0] > minHeap[0]:
        val = -heapq.heappop(maxHeap)
        heapq.heappush(minHeap, val)

    # 3. 힙 크기 균형 맞추기
    if len(maxHeap) > len(minHeap) + 1:
        val = -heapq.heappop(maxHeap)
        heapq.heappush(minHeap, val)
    elif len(minHeap) > len(maxHeap):
        val = heapq.heappop(minHeap)
        heapq.heappush(maxHeap, -val)

    print(-maxHeap[0])