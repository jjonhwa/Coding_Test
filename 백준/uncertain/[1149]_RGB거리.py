"""
    문제
        1. (1,2), (N, N-1) 집의 색은 서로 달라야 햔다. 
        2. 1 < i < N인 i에 대하여, (i-1, i), (i, i+1) 집의 색은 서로 달라야 한다.
        3. 목적은 단순히 "비용"이라는 것에 초점

    풀이
        1. 내 색깔을 기준으로 DP를 생성한다. (다은 색은 오로지 "내 색"에만 의존하기 때문에)
        2. "비용"을 구해야 하므로, 각 집이 "특정 색"이 될 때의 "최소 비용"을 저장하도록 한다. 
"""

import sys
input = sys.stdin.readline

n = int(input())

house = []
for _ in range(n):
    r, g, b = list(map(int, input().split()))
    house.append((r, g, b))

dp = [[float("inf") for _ in range(3)] for _ in range(n)]
for i in range(n):
    r, g, b = house[i]

    if i == 0:
        dp[i][0] = r
        dp[i][1] = g
        dp[i][2] = b
    else:
        dp[i][0] = min(dp[i-1][1] + r, dp[i-1][2] + r)
        dp[i][1] = min(dp[i-1][0] + g, dp[i-1][2] + g)
        dp[i][2] = min(dp[i-1][0] + b, dp[i-1][1] + b)

print(min(dp[-1]))