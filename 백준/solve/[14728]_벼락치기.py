import sys
input = sys.stdin.readline

n, t = list(map(int, input().split()))

classes = []
for _ in range(n):
    study_time, score = list(map(int, input().split()))
    classes.append((study_time, score))

dp = [[0 for _ in range(t+1)] for _ in range(n)]

classes.sort(key = lambda x: x[0])

max_score = float("-inf")
for i, (study_time, score) in enumerate(classes):
    if i == 0:
        for j in range(study_time, t+1):
            dp[i][j] = score
    else:
        for j in range(t+1):
            if j < study_time:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j - study_time] + score, dp[i-1][j])
print(dp[-1][-1])