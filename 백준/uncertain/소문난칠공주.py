"""
    완전탐색 + BFS + 백트래킹
"""
from collections import deque
from itertools import combinations

import sys
input = sys.stdin.readline

graph = []
for _ in range(5):
    row = list(input().strip())
    graph.append(row)

overall_node = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        overall_node.append((i, j, graph[i][j]))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0
for comb in combinations(overall_node, 7):

    # S가 4개보다 작을 경우 제외
    s_count = sum([1 for c in comb if c[2] == "S"])
    if s_count < 4:
        continue

    # S가 4개 이상일 경우 => 전부 붙어있는 지 확인
    candidate = [(c[0], c[1]) for c in comb]
    visited = [[False for _ in range(5)] for _ in range(5)]
    
    queue = deque([candidate[0]])
    visited[candidate[0][0]][candidate[0][1]] = True

    count = 1
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<5 and 0<=ny<5 and not visited[nx][ny] and (nx, ny) in candidate:
                count += 1
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    if count == 7:
        answer += 1

print(answer)