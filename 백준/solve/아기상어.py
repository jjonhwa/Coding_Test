"""
아기상어 크기: 2

규칙
1. 자기보다 작은 물고기는 먹고, 이동 가능
2. 자기와 크기가 같은 물고기는 이동만 가능
3. 자기보다 크기가 큰 물고기는 아무런 행동도 할 수 없음

이동 규칙
1. 먹을 수 있는 물고기가 있을 경우 이동
    1-1. 1마리일 경우, 바로 이동
    1-2. 2마리 이상일 경우, 가장 가까운 물고기로 이동
    1-3. 거리가 모두 동일할 경우, 가장 위
    1-4. 가장 위에 여려마리가 있을 경우 가장 왼쪽 물고기로 이동
2. 물고기를 먹으면 그 칸은 빈칸이 된다.
3. 자신의 크기만큼의 물고기 (개체수)를 먹으면 1 증가
4. 먹을 수 있는 물고기가 없을 경우 종료

코딩 순서
1. 먹을 수 있는 물고기 List: [(x1, y1, Dist1), (x2, y2, Dist2), ...]
    1-1. 완전 탐색
    1-2. 아기 상어보다 크기가 작은 물고기 삽입
2. 이동 규칙에 따라 이동
    2-1. 가장 가까운 물고기 (distance)
    2-2. 2마리 이상일 경우, y가 작고,  x가 작은 순으로 이동
3. 먹은 물고기 graph update
4. 아기 상어의 크기 update
5. 먹을 수 있는 물고기 List update
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

answer = 0
weight = 2
go_weight = 2

# 현재 위치 초기화
baby_shark = []
for i in range(len(graph)):
    for j in range(len(graph[0])):
        if graph[i][j] == 9:
            baby_shark.append(i)
            baby_shark.append(j)
            break
    if baby_shark:
        break

while True:
    # 최단거리 물고기 탐색
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    minimum_distance = float("inf")
    candidate_fish = []

    queue = deque([[baby_shark[0], baby_shark[1], 0]])
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[baby_shark[0]][baby_shark[1]] = True

    minimum_distance = float("inf")
    candidate_fish = []
    while queue:
        x, y, dist = queue.popleft()

        if dist > minimum_distance:
            continue

        if graph[x][y] != 0 and graph[x][y] != 9 and graph[x][y] < weight:
            candidate_fish.append([x,y,dist])
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and (graph[nx][ny]<=weight or graph[nx][ny]==9):
                visited[nx][ny] = True
                queue.append([nx, ny, dist+1])

    # 종료 조건
    if not candidate_fish:
        break

    # 가장 가까운 물고기 탐색
    candidate_fish.sort(key = lambda x: (x[2], x[0], x[1]))
    eat_x, eat_y, move = candidate_fish[0]
    answer += move

    # 먹은 물고기 graph update
    graph[baby_shark[0]][baby_shark[1]] = 0
    graph[eat_x][eat_y] = 9

    # 현재위치 update
    baby_shark = [eat_x, eat_y]
    

    # 아기 상어의 크기 update
    go_weight -= 1
    if go_weight == 0:
        weight += 1
        go_weight = weight

print(answer)
