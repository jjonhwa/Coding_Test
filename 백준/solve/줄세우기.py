import sys
input = sys.stdin.readline

n = int(input())

children = []
for _ in range(n):
    children.append(int(input()))

children = children + children
dp = [1] * (2*n)
for i in range(len(children)):
    for j in range(i):
        if children[i] > children[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)