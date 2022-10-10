"""
1. 연결관계를 통해 묶음 확인
2. 가장 많은 선을 가진 Node 확인 (x) -> 의사전달 시간 최댓값이 최소 (o)
"""
from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())


## 플로이드 워셜 - 의사전달 시간 최댓값이 최소를 구하기 위해
INF = int(1e9)
floid = [[INF for _ in  range(n+1)]   for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            floid[i][j] = 0

graph = [[] for _  in range(n+1)]

for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

    floid[a][b] = 1
    floid[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            floid[i][j] = min(floid[i][j], floid[i][k] + floid[k][j])
###############



# 연결관계를 통해 묶음 확인
visited = [False for _ in range(n+1)]

groups = []
for i in range(1, n+1):

    group = []
    if not visited[i]:
        group.append(i)
        visited[i] = True

        queue = deque(graph[i])
        while queue:
            current = queue.popleft()
 
            if not visited[current]:
                visited[current] = True
                group.append(current)

                for child in graph[current]:
                    if not visited[child]:
                        queue.append(child)

    if group:
        groups.append(group)

# 의사전달 시간 최댓값이 최소 (o)
group_master = []
for group in groups:
    
    minimum_distance = float("inf")
    for i in group:
        distance = float("-inf")
        for j in group:
            if i == j:
                continue

            distance = max(distance, floid[i][j])

        if distance < minimum_distance:
            master = i
            minimum_distance = distance

    group_master.append(master)

group_master.sort()

print(len(group_master))
for i in range(len(group_master)):
    print(group_master[i])


