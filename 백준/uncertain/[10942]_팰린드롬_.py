"""
    1. DP 
        가로: 시작 index
        세로: 길이
    
    2. 초기화 
        길이가 1인 경우는 모두 1
        길이가 2인 경우는 탐색하여 0 혹은 1 삽입

    3. 갱신 방식
        홀수는 홀수끼리, 짝수는 짝수끼리
        "이전 값이 팰린드롬인가?" + "시작과 끝이 같은가?"

        if dp[i-2][j+1] and start == end:
            dp[i][j] = 1
"""

import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
start_end_pair = []
for _ in range(m):
    s, e = list(map(int, input().split()))
    start_end_pair.append((s, e))

dp = [[-1 for _ in range(n)] for _ in range(n)]

# 초기화 - 길이가 1인 경우
for i in range(n):
    dp[0][i] = 1

# 초기화 - 길이가 2인 경우
for i in range(n-1):
    if num_list[i] == num_list[i+1]:
        dp[1][i] = 1
    else:
        dp[1][i] = 0

# 갱신
for i in range(2, n): # 길이
    for j in range(n-i): # 시작 index

        start = num_list[j]
        end = num_list[j+i]
        if dp[i-2][j+1] and start == end:
            dp[i][j] = 1
        else:
            dp[i][j] = 0

# 정답 탐색
for s, e in start_end_pair:
    length = e - s
    print(dp[length][s-1])

