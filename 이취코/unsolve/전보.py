import sys
import heapq
input = sys.stdin.readline

N, M, C = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, w = list(map(int, input().split()))
    graph[a].append((b,w))

INF = int(1e9)
distance = [INF] * (N+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(C)
cnt = 0
time = 0
for dist in distance:
    if dist == INF or dist == 0:
        continue
    cnt += 1
    time = max(time, dist)
print(cnt, time)