"""
    DP: 인원수 DP (인원수에 대한 비용을 담는 배열 생성)
    
    1. 인원수 DP 생성
    2. c부터 최대 고객수인 100명의 범위 내에서의 최솟값 출력
"""
import sys
input = sys.stdin.readline

c, n = list(map(int, input().split()))

investment = []
for _ in range(n):
    cost, client = list(map(int, input().split()))
    investment.append((cost, client))

dp = [float("inf") for _ in range(1100)] # client수 + 최대 고객의 수 = 1100
dp[0] = 0
for cost, client in investment:
    for i in range(client, 1100):
        dp[i] = min(dp[i - client] + cost, dp[i])

print(min(dp[c:c+100]))
