"""
현재 활성화 되어있음
활성화 앱           : A1, A2, A3, A4, A5
메모리 (M)          : 30  10  20  35  40
비활성화 후 실행 (C) : 3   0   3   5   4

C를 최소화하면서 M을 목적값에 도달하도록 하는 함수


2차원 DP 문제 (Knapsack 문제)
    NS("ABCD", weight) = Max(NS("ABC", weight - weight[D]), NS("ABC", weight))
    즉, ABCD를 고려할 경우 =  최대값 ( ABC에서 D가 있다, ABC에서 D가 없다)

    DP[i][j] = Max( DP[i-1][j - i행의 cost] + i행의 메모리, DP[i-1][j])
"""
import sys

n, target = list(map(int, input().split()))
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 10000 = C X N
dp = [[0] * (10001) for _ in range(n+1)]

for i in range(1, len(dp)):
    c = cost[i-1]
    m = memory[i-1]
    for j in range(len(dp[0])):
        if j < c:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j - c]+m, dp[i-1][j])

find_target = False
for j in range(len(dp[0])):
    for i in range(len(dp)):
        if dp[i][j] >= target:
            find_target = True
            answer = j
            break
    if find_target:
        break
print(answer)

