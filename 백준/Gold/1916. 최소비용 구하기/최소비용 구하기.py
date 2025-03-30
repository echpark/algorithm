import heapq

def dijkstra(start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

N = int(input())
M = int(input())

graph = {i: {} for i in range(1, N+1)}

for i in range(M):
    start, end, cost = map(int, input().split())
    if end not in graph[start] or graph[start][end] > cost:
        graph[start][end] = cost

target_start, target_end = map(int, input().split())

for node, weight in dijkstra(target_start).items():
    if node == target_end:
        print(weight)