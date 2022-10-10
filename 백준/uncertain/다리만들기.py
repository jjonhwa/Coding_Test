"""
1. 섬 구분
2. 섬 간의 이동
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 1. 섬 구분: TC(100(x축) x 100(y축) x 200x4(while문))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False for _ in range(n)] for _ in range(n)]

island_number = 1
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 1 and not visited[i][j]:
            position = deque([[i, j]])
            visited[i][j] = True
            graph[i][j] = island_number

            while position:
                x, y = position.popleft()
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]

                    if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        position.append([nx, ny])

                        graph[nx][ny] = island_number
            
            island_number += 1

# 2. 다른 섬으로 이동: TC(100(x축) x 100(y축) x 200x4(while문))
minimum_length = float("inf")
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] != 0:
            mine = graph[i][j]
            position = deque([[i, j, 0]])

            visited = [[True for _ in range(n)] for _ in range(n)]
            meet = False
            while position:
                x, y, leng= position.popleft()

                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]

                    if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=0 and graph[nx][ny]!=mine:
                        meet=True
                        minimum_length = min(minimum_length, leng)
                        break

                    if 0<=nx<n and 0<=ny<n and graph[nx][ny]==0 and visited[nx][ny]:
                        visited[nx][ny] = False
                        position.append([nx, ny, leng+1])

                if meet:
                    break
print(minimum_length)

"""
Time Complexity: O(N^3)

O(N x N x 2Nx4) => O(8,000,000)
"""