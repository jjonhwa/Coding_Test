"""
    3차원 visited BFS

    1. visited에 지금까지 이동한 횟수에 대한 정보를 담는다.
    2. 3차원 visited로서 (x, y)좌표에 대하여 
            [[벽 부쉈을 때 이동횟수], [벽 부수지 않았을 때 이동횟수]]를 가지도록 한다.
"""

from collections import deque
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    row = list(map(int, list(input().strip())))
    graph.append(row)

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

start = (0,0,0) # x좌표, y좌표, 벽 부숨 or not 
visited[start[0]][start[1]][start[2]] = 1 # 벽을 부수지 않았을 때, (0,0)의 방문 횟수를 1로 초기화

queue = deque()
queue.append(start)

arrival = False
while queue:
    x, y, broken_wall = queue.popleft()

    # 끝 점 도달 시 종료
    if x == n-1 and y == m-1:
        arrival = True
        break

    # 단순한 BFS를 수행
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<n and 0<=ny<m:

            # 다음 이동 지점이 "벽"이고, "벽을 부수는 행위를 하지 않았을 경우"에 실행
            if graph[nx][ny] == 1 and broken_wall == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            
            # 다음 이동 지점이 "벽 x"이고, "아직 방문하지 않았을 경우"에  실행
            elif graph[nx][ny] == 0 and visited[nx][ny][broken_wall] == 0:
                visited[nx][ny][broken_wall] = visited[x][y][broken_wall] + 1
                queue.append((nx, ny, broken_wall))

            # 그 외
            ## 다음 이동지점이 "벽"인데, "벽을 부수는 행위를 이미 했을 경우"
            ## 다음 이동지점이 벽이 아닌데, 이미 방문을 했을 경우
            ### 위의 두 가지의 경우에 대해서는 아무런 실행을 하지 않는다.

if arrival:
    print(visited[x][y][broken_wall])
else:
    print(-1)