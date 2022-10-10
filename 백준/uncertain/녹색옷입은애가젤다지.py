"""
    BFS 탐색

    Python: 시간초과
    Pypy: 통과
"""
# from collections import deque
# import sys
# input = sys.stdin.readline

# problem_num = 1
# while True:
#     n = int(input())

#     if n == 0:
#         break

#     graph = []
#     for _ in range(n):
#         row = list(map(int, input().split()))
#         graph.append(row)

#     INF = float("inf")
#     dp = [[INF for _ in range(n)] for _ in range(n)]

#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]

#     queue = deque([[0, 0, graph[0][0]]])
#     dp[0][0] = graph[0][0]
#     while queue:
#         x, y, rupee = queue.popleft()

#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]

#             if 0<=nx<n and 0<=ny<n and dp[nx][ny] > rupee + graph[nx][ny]:
#                 dp[nx][ny] = rupee + graph[nx][ny]
#                 queue.append([nx, ny, dp[nx][ny]])

#     print(f"Problem {problem_num}: {dp[n-1][n-1]}")
#     problem_num += 1


from collections import deque
import sys
input = sys.stdin.readline

problem_num = 1
while True:
    n = int(input())

    if n == 0:
        break

    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    INF = float("inf")
    dp = [[INF for _ in range(n)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([[0, 0]])
    dp[0][0] = graph[0][0]
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n and dp[nx][ny] > dp[x][y] + graph[nx][ny]:
                dp[nx][ny] = dp[x][y] + graph[nx][ny]
                queue.append([nx, ny])

    print(f"Problem {problem_num}: {dp[n-1][n-1]}")
    problem_num += 1
