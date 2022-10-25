"""
    BFS + 꺽은선의 개수 확인

    1. BFS를 활용하여 C에서 C로 가는 방법 탐색
    2. visited 대신 꺽은 선의 개수를 입력하여 재방문을 허락
"""

from collections import deque

import sys
input = sys.stdin.readline

W, H = list(map(int, input().split()))

graph = []
point = []
for i in range(H):
    row = input().strip()
    row = [v for v in row]

    for j in range(W):
        if row[j] == "C":
            point.append((i, j))

    graph.append(row)

start = point[0]
end = point[1]

visited = [[-1 for _ in range(W)] for _ in range(H)]

# 동, 서, 남, 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 온 방향 (0: 동, 1:서, 2: 남, 3: 북)
queue = deque()
queue.append((start, 0, -1)) # (좌표, 꺽은선의 개수, 온 방향)
visited[start[0]][start[1]] = 0

while queue:

    axis, polygonal, come = queue.popleft()
    x, y = axis

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        
        next_polygonal = polygonal
        next_come = i

        if come != -1 and come != i: # 처음 칸에서 오지 않았으면서, 온 방향과 갈 방향이 다르다면
            next_polygonal += 1

        if 0<=nx<H and 0<=ny<W and graph[nx][ny] != "*" and (visited[nx][ny] == -1 or visited[nx][ny] >= next_polygonal):
            visited[nx][ny] = next_polygonal
            queue.append(((nx, ny), next_polygonal, next_come))

print(visited[end[0]][end[1]])