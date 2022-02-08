from os import X_OK
import sys
import heapq

input = sys.stdin.readline

N, M, X = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, weight = list(map(int, input().split()))
    graph[start].append([end, weight])

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, [0, start])
    while len(q):
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        # 갱신 필요
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])

shortest = [0] * (N+1)
for i in range(1, N+1):
    if i == X:
        continue

    # 시작에서 X까지 출발
    inf = 999999
    distance = [inf] * (N+1)
    dijkstra(i, distance)
    shortest[i] += distance[X] # X까지는 가는 최단거리

    # X에서 시작까지 출발
    inf = 999999
    distance = [inf] * (N+1)
    dijkstra(X, distance)
    shortest[i] += distance[i] # 2에서 오는 최단거리

print(max(shortest))