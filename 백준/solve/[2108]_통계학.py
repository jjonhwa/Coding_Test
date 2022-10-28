from collections import Counter

import sys
input = sys.stdin.readline

def mean_func(num_list):
    return sum(num_list) / len(num_list)

def median_func(num_list):
    median_index = (len(num_list)+1) // 2 - 1
    num_list.sort()

    return num_list[median_index]

def mode_func(num_list):
    count_dict = Counter(num_list)

    max_count = max([v for v in count_dict.values()])
    mode_candidate = [num for num in count_dict.keys() if count_dict[num] == max_count]

    if len(mode_candidate) > 1:
        mode_candidate.sort()
        return mode_candidate[1]
    else:
        return mode_candidate[0]

def range_func(num_list):
    max_num = max(num_list)
    min_num = min(num_list)
    return max_num - min_num

n = int(input())

num_list = []
for _ in range(n):
    num = int(input())
    num_list.append(num)

print(int(round(mean_func(num_list), 0)))
print(median_func(num_list))
print(mode_func(num_list))
print(range_func(num_list))