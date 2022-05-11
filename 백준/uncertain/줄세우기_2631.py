# 가장 긴 부분수열을 이용한 줄세우기
"""
가장 긴 부분수열을 구한다.
그 부분 수열에 포함되지 않은 학생들을 옮겨주면 끝
"""
import sys
input = sys.stdin.readline

n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
    
dp = [1] * n
for i in range(len(num_list)):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))
