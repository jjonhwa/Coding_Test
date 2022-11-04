"""
    3차원 visited 활용 문제
"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    row = list(map(int, list(input().rstrip())))
    graph.append(row)

def solution(n, m, graph):
    queue = deque()
    queue.append((0, 0, 0, 0)) # x좌표, y좌표, distance, wall_break

    visited = [[[False, False] for _ in range(m)] for _ in range(n)] # [벽 안부숨, 벽 한 번 부숨]
    visited[0][0][0] = True
    visited[0][0][1] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y, dist, is_break = queue.popleft()

        if x == n-1 and y == m-1:
            return dist+1

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 벽을 부수고 지나갈 때
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1 and not visited[nx][ny][1] and is_break == 0:
                visited[nx][ny][1] = True
                queue.append((nx, ny, dist+1, 1))

            # 벽을 부수지 않고 지나갈 때
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny][is_break] and graph[nx][ny] == 0:
                visited[nx][ny][is_break] = True
                queue.append((nx, ny, dist+1, is_break))
    
    return -1

print(solution(n, m, graph))