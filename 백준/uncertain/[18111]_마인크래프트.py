# PyPy3 통과
"""
    1. (가장 높은 높이)256 ~ 0까지 Loop
    2. 각 높이에 맞춰서 쌓는 것이 가능한지 탐색
    3. 가능하다면 걸리는 시간 갱신 
"""
# import sys
# input = sys.stdin.readline

# n, m, b = list(map(int, input().split()))

# graph = []
# max_height = float("-inf")
# for _ in range(n):
#     row = list(map(int, input().split()))
#     graph.append(row)
#     max_height = max(max_height, max(row))

# min_time = float("inf")
# answer = 0
# for height in range(max_height, -1, -1):
    
#     break_time = False
    
#     time = 0
#     block_count = b

#     for i in range(n):
#         for j in range(m):
            
#             # 제거
#             if graph[i][j] > height:
#                 difference = graph[i][j] - height
#                 block_count += difference
#                 time += 2*difference

#             # 쌓기
#             elif graph[i][j] < height:
#                 difference = height - graph[i][j]
#                 block_count -= difference
#                 time += difference

#             if time >= min_time:
#                 break_time = True
#                 break
        
#         if break_time:
#             break

#     if not break_time and block_count >= 0:
#         min_time = time
#         answer = height
    
# print(min_time, answer)

# Python3
"""
    1. (가장 높은 높이)256 ~ 0까지 Loop
    2. 각 높이에 맞춰서 쌓는 것이 가능한지 탐색
    3. 가능하다면 걸리는 시간 갱신 
"""
from collections import defaultdict
import sys

input = sys.stdin.readline

n, m, b = list(map(int, input().split()))

height_count = defaultdict(int)
for _ in range(n):
    row = list(map(int, input().split()))

    for value in row:
        height_count[value] += 1


height_count = sorted(height_count.items(), key = lambda x: -x[0])
max_height = height_count[0][0]

min_time = float("inf")
for goal_height in range(max_height, -1, -1): # 256개
    
    time = 0
    block_count = b
    for height, count in height_count:
        if height == goal_height:
            continue

        if height > goal_height:
            difference = height - goal_height
            time += 2*count*difference
            block_count += count*difference
        else:
            difference = goal_height - height
            time += count*difference
            block_count -= count*difference
    
    if block_count >= 0 and time < min_time:
        min_time = time
        answer = goal_height

print(min_time, answer)
