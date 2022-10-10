"""
1. 중간을 기준으로 left와 right으로 나눔
2. left, right에서의 수열의 합 계산.
3. s를 만족하는 값을 찾기 위한 pointer 이동
"""
from itertools import combinations

import sys
input = sys.stdin.readline

n, s = list(map(int, input().split()))
num_list = list(map(int, input().split()))

# 중간을 기준으로 left와 right으로 나눔
center = n // 2
left_side = num_list[:center]
right_side = num_list[center:]

# left, right에서의 수열의 합 계산
left_summation = []
for i in range(len(left_side)+1):
    for comb in combinations(left_side, i):
        left_summation.append(sum(comb))

right_summation = []
for i in range(len(right_side)+1):
    for comb in combinations(right_side, i):
        right_summation.append(sum(comb))

left_summation.sort()
right_summation.sort()

# s를 만족하는 값을 찾기 위한 pointer 이동
left_pointer = 0
right_pointer = len(right_summation) - 1

cnt = 0
while left_pointer < len(left_summation) and 0 <= right_pointer :
    left_value = left_summation[left_pointer]
    right_value = right_summation[right_pointer]
 
    if left_value + right_value == s: 

        # 같을 경우가 중복으로 나타날 수 있음.
        dup_left = 1
        while True:
            if left_pointer + dup_left >= len(left_summation) or left_value != left_summation[left_pointer + dup_left]:
                break
            dup_left += 1

        dup_right = 1
        while True:
            if right_pointer - dup_right < 0 or right_value != right_summation[right_pointer - dup_right]:
                break
            dup_right += 1

        cnt += (dup_left * dup_right)

        left_pointer += dup_left
        right_pointer -= dup_right

    elif left_value + right_value > s:
        right_pointer -= 1
    else:
        left_pointer += 1

if s == 0:
    cnt -= 1

print(cnt)
