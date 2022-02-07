import sys
from collections import deque
input = sys.stdin.readline

N, M = list(map(int, input().split()))
icecream = []
for _ in range(N):
    icecream.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N)]

cnt = 0
now = [0,0]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    while len(queue):
        now = queue.popleft()
        x, y = now[0], now[1]
        visited[x][y] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visited[nx][ny]:
                queue.append([nx, ny])

for i in range(N):
    for j in range(M):
        if icecream[i][j] != 1 and visited[i][j] == False:
            cnt += 1
            bfs(icecream, [i, j], visited)

print(cnt)
