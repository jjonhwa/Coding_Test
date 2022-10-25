from collections import deque

import sys
input = sys.stdin.readline

k = int(input())
w, h = list(map(int, input().split()))

graph = []
for _ in range(h):
    row = list(map(int, input().split()))
    graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dx_horse = [-2, -1, 1, 2, 2, 1, -1, -2]
dy_horse = [1, 2, 2, 1, -1, -2, -2, -1]

start = (0,0,0) # x좌표, y좌표, horse 사용 횟수

queue = deque()
queue.append(start)

# (x, y)에서의 [horse 0번 사용 거리, horse 1번 사용 거리, horse 2번 사용 거리, ...]
visited = [[[0 for _ in range(k+1)] for _ in range(w)] for _ in range(h)]
visited[start[0]][start[1]][start[2]] = 1 # horse 사용 x일 때, 0,0의 값은 1

arrival = False
while queue:
    x, y, horse_count = queue.popleft()

    # 도착지점에 가장 먼저 도착했다면, 그 즉시 종료
    if x == h-1 and y == w-1:
        arrival = True
        break

    # 단순히 상하좌우로만 움직일 경우
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<h and 0<=ny<w and graph[nx][ny] != 1 and visited[nx][ny][horse_count] == 0:
            visited[nx][ny][horse_count] = visited[x][y][horse_count] + 1
            queue.append((nx, ny, horse_count))
    
    # 말의 움직임을 활용할 경우
    if horse_count < k: # 말의 움직임은 최대 k번 활용할 수 있음
        for i in range(len(dx_horse)):
            nx, ny = x+dx_horse[i], y+dy_horse[i]

            if 0<=nx<h and 0<=ny<w and graph[nx][ny] != 1 and visited[nx][ny][horse_count+1] == 0:
                visited[nx][ny][horse_count + 1] = visited[x][y][horse_count] + 1
                queue.append((nx, ny, horse_count+1))

if arrival:
    print(visited[x][y][horse_count] - 1) # 시작지점의 이동거리를 1로 시작하였으므로 1 차감
else:
    print(-1)

