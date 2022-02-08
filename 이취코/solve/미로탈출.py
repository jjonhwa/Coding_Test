import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
# 각 지점에 도달할 수 있는 최단 경로를 삽입
shortest = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
miro = []
for _ in range(N):
    miro.append(list(map(int, input().split())))

start = [0, 0]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
x, y = start[0], start[1]
shortest[x][y] = 1
visited[x][y] = True

queue = deque()
queue.append(start)
while len(queue):
    now = queue.popleft()
    for i in range(4):
        nx = now[0] + dx[i]
        ny = now[1] + dy[i]
        if 0 <= nx < N and 0 <= ny < M and miro[nx][ny] == 1 and not visited[nx][ny]:
            queue.append([nx, ny])
            visited[nx][ny] = True
            shortest[nx][ny] = shortest[now[0]][now[1]] + 1

print(shortest[N-1][M-1])
