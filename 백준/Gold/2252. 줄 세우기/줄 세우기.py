from collections import deque

def topology_sort():
    result = []
    q = deque()

    # 진입차수가 없는 노드 찾기
    for i in range(1, N+1):
        if indegree[i] == 0: # 진입차수가 없으면
            q.append(i) # q에 추가

    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1 # 간선 삭제
            if indegree[i] == 0: # 진입차수가 없으면
                q.append(i) # q에 추가

    for i in result:
        print(i, end = " ")


N, M = map(int, input().split())

indegree = [0] * (N + 1)  # 진입 차수
graph = [[] for i in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

topology_sort()