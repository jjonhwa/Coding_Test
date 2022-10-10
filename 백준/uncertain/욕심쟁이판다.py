"""
    다음 지역에 더 많은 대나무
    어떤 지점에서 출발해야지 최대한 많은 대나무를 먹을 수 있을 것인가?

    이동할 수 있는 칸의 개수를 출력

    N = 500 => O(N^2)으로 해결
    N^2 = 50,000
    N^3 = 125,000,000
    모든 지점에서 출발 => 500 x 500 => BFS (500^4) => X

    DP => 특정 지점에서 이동 할 수 있는 지점의 개수를 저장
    1. 모든 지점에서 출발
    2. 각 지점에서 이동할 수 있는 최대 칸의 개수를 DP에 입력
    3. DP에 값이 있을 경우, 값을 더해준 후 종료
"""

"""
    BFS + DP: 시간초과
"""
from collections import deque

import sys
input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

dp = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 모든 지점에서 출발
for i in range(len(graph)):
    for j in range(len(graph[0])):
        queue = deque([[i, j, 1]]) # [x좌표, y좌표, count]

        max_count = 1
        while queue:
            x, y, count = queue.popleft()

            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]

                if 0<=nx<n and 0<=ny<n and graph[nx][ny] > graph[x][y]:

                    # 2. 각 지점에서 이동할 수 있는 최대 칸의 개수를 DP에 입력
                    if not dp[nx][ny]:
                        max_count = max(max_count, count+1)
                        queue.append([nx, ny, count+1])

                    # 3. DP에 값이 있을 경우, 값을 더해준 후 종료
                    else: 
                        max_count = max(max_count, count+dp[nx][ny])
        dp[i][j] = max_count



answer = float("-inf")
for i in range(len(dp)):
    answer = max(answer, max(dp[i]))
print(answer)


"""
    DFS: 통과
"""
from collections import deque

import sys
sys.setrecursionlimit(250000)

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

dp = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 모든 지점에서 출발
def dfs(x, y):
    if dp[x][y]:
        return dp[x][y]

    dp[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny] > graph[x][y]:
            dp[x][y] = max(dp[x][y], dfs(nx, ny)+1)
    return dp[x][y]

for i in range(len(graph)):
    for j in range(len(graph[0])):
        dfs(i, j)

answer = float("-inf")
for i in range(len(dp)):
    answer = max(answer, max(dp[i]))
print(answer)

"""
BFS + DP로 풀었는데 시간초과가 발생했습니다.

    중복 경로가 발생해서 생기는 시간초과 문제인데, 이를 어떻게 해결할 수 있을까?
    
    예를 들어, 1 -> 2 -> 3 -> 4가 주어졌을 때, 1에 4만 입력이 되는 형태. (4, 3, 2, 1)로 전부 입력이 들어가야지
    중복 문제가 해결. 

    DFS가 해결 방법 중 하나!

왜 풀이가 전부 DFS밖에 없나 했는데, 위 부분을 DFS로 해결이 가능한 것 같습니다.y

BFS로 풀 수 있는 방법은 없을까요?
"""