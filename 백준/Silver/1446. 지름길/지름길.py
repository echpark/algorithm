import heapq
from collections import defaultdict

def dijkstra():
    dist = [float('inf')] * (D + 1)
    dist[0] = 0
    pq = [(0, 0)] # (비용, 위치)

    while pq:
        curr_cost, curr_loc = heapq.heappop(pq)

        # 종점에 도달
        if curr_loc >= D:
            continue

        # 이미 더 낮은 비용이 적용되어 있음
        if dist[curr_loc] < curr_cost:
            continue

        # 일반 도로
        if dist[curr_loc + 1] > dist[curr_loc] + 1:
            dist[curr_loc + 1] = dist[curr_loc] + 1
            heapq.heappush(pq, (dist[curr_loc + 1], curr_loc + 1))

        # 지름길
        for end, length in fast_road[curr_loc]:
            if end <= D and dist[end] > dist[curr_loc] + length:
                dist[end] = dist[curr_loc] + length
                heapq.heappush(pq, (dist[end], end))

    return dist[D]

N, D = map(int, input().split())

fast_road = defaultdict(list)
for _ in range(N):
    start, end, length = map(int, input().split())
    fast_road[start].append((end, length))

print(dijkstra())