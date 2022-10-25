"""
    문제
        1. (1,2), (1,N)  집의 색은 서로 다르다
        2. (N,N-1), (N,1) 집의 색은 서로 다르다
        3. (i-1, i), (i, i+1) 집의 색은 서로 다르다.

    풀이
        1. 시작지점 고정
        2. 2~N-1에 대하여 규칙에 맞게 최소값을 넣는다.
        3. 시작지점과 다른 끝지점에 대하여 규칙에 맞게 최소값 갱신
"""

import sys
input = sys.stdin.readline

n = int(input())

house = []
for _ in range(n):
    r, g, b = list(map(int, input().split()))
    house.append((r,g,b))

start = house[0]
end = house[-1]

minimum_cost = float("inf")
for col in range(3):
    start_color = col # col(0): Red, col(1): Green, col(2): Blue

    
    dp = [[float("inf") for _ in range(3)] for _ in range(n-1)]
    for i in range(n-1):
        r, g, b = house[i]

        # 1. 시작지점 고정
        if i == 0:
            dp[i][start_color] = start[start_color]

        # 2. 2~N-1에 대하여, 규칙에 맞게 최소값 삽입
        else:
            dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + r
            dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + g
            dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + b
    
    # 3. 시작지점과 다른 끝지점에 대하여 규칙에 맞게 최소값 갱신
    another_color = [i for i in range(3) if i != start_color]
    
    for color in another_color:
        for i in range(3):
            if i == color:
                continue

            minimum_cost = min(minimum_cost, dp[-1][i] + end[color])

print(minimum_cost)


            

