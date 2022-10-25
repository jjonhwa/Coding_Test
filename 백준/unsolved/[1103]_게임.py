"""
    DFS + 백트래킹(DP)

    DFS로 탐색 중에, 이미 값이 있을 경우, 그 값이 진행중인 값보다 크다면 더 이상 진행하지 않음.
"""

import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m = list(map(int, input().split()))

coin_graph = []
for _ in range(n):
    row = list(input().strip())
    coin_graph.append(row)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dp = [[float("-inf") for _ in range(m)] for _ in range(n)] # 최대값 확인
visited = [[False for _ in range(m)] for _ in range(n)] # 무한루프 확인

max_distance = float("-inf")
infinite_loof = False

def dfs(node):
    global max_distance, infinite_loof

    x, y, distance = node

    # 무한 루프가 이미 생성됬다면 종료
    if infinite_loof:
        return

    # 최대 거리값 갱신
    max_distance = max(max_distance, distance)

    coin_num = int(coin_graph[x][y]) # 동전 위치의 값
    for i in range(4):
        nx, ny = x+dx[i]*coin_num, y+dy[i]*coin_num

        if 0<=nx<n and 0<=ny<m and coin_graph[nx][ny] != "H":

            # DFS로 방문을 이미 했다면, 본인이 지나온 길을 재방문 한 것이므로 Cycle 생성
            if visited[nx][ny]:
                infinite_loof = True
                return
            
            # (nx, ny)까지 오는데 더 많은 distance를 가졌을 경우에만 추가적으로 dfs 수행
                # 작거나 같은 distance라면, 결국 (nx, ny)를 방문한다 하더라도 같은 결과값이 출력되므로
            if dp[nx][ny] <= distance:
                dp[nx][ny] = distance + 1

                visited[nx][ny] = True
                dfs((nx, ny, distance + 1))
                visited[nx][ny] = False

start = (0,0,0) # x좌표, y좌표, 움직인 거리

dfs(start)

if infinite_loof:
    print(-1)
else:
    print(max_distance+1)