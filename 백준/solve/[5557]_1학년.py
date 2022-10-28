"""
    DP
    
       0  1  2  3  4 ... 20 (연산 결과값)
    0
    1
    2
    3
    ...
    98
    (부호의 개수)

    => 0으로 초기화.
    => 각 값이 등장할 때마다 1씩 추가 (서로 다른 부호로부터 결과값이 생성)
    => DP[n-2][target]을 return
"""

import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

dp = [[0 for _ in range(21)] for _ in range(n-1)]

for i in range(len(num_list)-1):
    if i == 0:
        number = num_list[i]
        dp[i][number] += 1
    else:
        for j in range(21):
            if dp[i-1][j]:
                plus_number = j + num_list[i]
                minus_number = j - num_list[i]

                if 0<=plus_number<=20:
                    dp[i][plus_number] += dp[i-1][j]

                if 0<=minus_number<=20:
                    dp[i][minus_number] += dp[i-1][j]

target = num_list[-1]
print(dp[-1][target])
