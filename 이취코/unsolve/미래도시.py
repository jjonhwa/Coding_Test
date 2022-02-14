import sys
import heapq
input = sys.stdin.readline

# 양방향
# 가중치의 값이 전부 동일
# 1번에서 K번, K번에서 X번 까지의 최단거리
N, M = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append((b,1))
    graph[b].append((a,1))

X, K = list(map(int, input().split()))

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

distance = [1e9] * (N+1)
dijkstra(1)
start_to_k = distance[K]

distance = [1e9] * (N+1)
dijkstra(K)
k_to_x = distance[X]

if start_to_k == 1e9 or k_to_x == 1e9:
    print(-1)
else:
    print(start_to_k + k_to_x)