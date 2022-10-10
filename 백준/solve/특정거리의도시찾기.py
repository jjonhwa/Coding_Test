"""
    문제:
    어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

    이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오. 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

    예를 들어 N=4, K=2, X=1일 때 다음과 같이 그래프가 구성되어 있다고 가정하자.

    입력:
    첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다. (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N) 
    둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다. 
    이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다. (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.

    출력:
    X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.

    이 때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
"""

import heapq

import sys
input = sys.stdin.readline

n, m, k, x = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    
visited = [False for _ in range(n+1)]

# heap: tuple(해당지점까지의 거리, 해당 지점)
heap = []
heapq.heappush(heap, (0, x)) 
visited[x] = True

answer = []
while heap:
    dist, node = heapq.heappop(heap)

    # 거리가 k를 만족할 경우 다음으로 더 이상 진행할 필요 없음
    if dist == k:
        answer.append(node)
        continue

    for next_node in graph[node]:

        # 최단거리 순으로 pop을 수행하기 때문에, 이미 방문했다면 최단거리가 아니라는 것을 의미
        if visited[next_node]:
            continue
        visited[next_node] = True

        # (거리+1, node) 추가 
        heapq.heappush(heap, (dist+1, next_node))


if not answer:
    print(-1)
else:
    answer.sort()
    for i in range(len(answer)):
        print(answer[i])