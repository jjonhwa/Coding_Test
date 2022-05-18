import sys

from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())

graph = []
for _ in range(2**N):
    row = list(map(int, input().split()))
    graph.append(row)

magic = list(map(int, input().split()))


dim = len(graph)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for L in magic:
    # 격자점의 시작 위치 찾기
    grid_start = []
    loop = dim // (2**L)
    if loop == 1:
        grid_start = [(0,0)]
    else:
        for i in range(loop):
            row = (2**L) * i
            for j in range(loop):
                col = (2**L) * j
                grid_start.append((row, col))
 
    # graph 회전 시키기
    for grid in grid_start:
        r1, c1 = grid
        r2, c2 = r1 + (2**L) - 1, c1 + (2**L) - 1
        tmp = []
        tmp_dim = r1+r2
        for c in range(c1, c2+1):
            temp = []
            for r in range(r1, r2+1):
                temp.append(graph[tmp_dim-r][c])
            tmp.append(temp)

        for grid_r, tmp_r in zip(range(r1,r2+1), range(len(tmp))):
            for grid_c, tmp_c in zip(range(c1, c2+1), range(len(tmp[0]))):
                graph[grid_r][grid_c] = tmp[tmp_r][tmp_c]

    # 주변 얼음 탐색
    melting_point = []
    for x in range(len(graph)):
        for y in range(len(graph[0])):
            count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                    if graph[nx][ny] >= 1:
                        count += 1
            
            if count < 3 and graph[x][y] != 0:
                melting_point.append((x,y))
                # graph[x][y] -= 1
    
    for x, y in melting_point:
        graph[x][y] -= 1

# 남은 얼음들의 합
print(sum([sum(row) for row in graph]))

# 남아 있는 얼음 중 가장 큰 덩어리가 차지하는 칸 수
visited = [[False for _ in range(len(graph[0]))] for _ in range(len(graph))]
max_count = 0
for x in range(len(graph)):
    for y in range(len(graph[0])):
        if graph[x][y] == 0:
            continue

        count = 1
        queue = deque([(x,y)])
        visited[x][y] = True

        while queue:
            now = queue.popleft()
            
            for i in range(4):
                nx, ny = now[0]+dx[i], now[1]+dy[i]

                if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]) and not visited[nx][ny] and graph[nx][ny] != 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
                    max_count = max(max_count, count)
print(max_count)