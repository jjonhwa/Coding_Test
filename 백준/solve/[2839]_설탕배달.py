import sys
input = sys.stdin.readline

n = int(input())
sugars = [3, 5]

INF = float("inf")
dp = [INF for _ in range(n+1)]
for sugar in sugars:
    
    for i in range(sugar, len(dp)):
        if dp[i-sugar] != INF:
            dp[i] = min(dp[i-sugar] + 1, dp[i])
        elif i % sugar == 0:
            dp[i] = 1

if dp[n] == INF:
    print(-1)
else:
    print(dp[n])