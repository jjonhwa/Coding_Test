"""
    다음 수 찾기

    6543
    6544 -> 6550 -> 6600 -> 7000
    7100 -> 7110 -> 7200 -> ...
"""

import sys
input = sys.stdin.readline

n = int(input())
def find_next_num(num):
    num += 1

    if num >= 9876543210:
        return num
        
    while True:
        num_list = list(str(num))
        place_num = 0
        for i, (first, second) in enumerate(zip(num_list, num_list[1:])):
            if first <= second:
                place_num = len(num_list) - i - 1
                break
        
        if place_num:
            num += 10**place_num
            num = int(str(num)[:-place_num] + '0'*place_num)
        else:
            return num

start = 0
for _ in range(n):
    start = find_next_num(start)

    if start > 9876543210:
        break

if start > 9876543210:
    print(-1)
else:
    print(start)



"""
    Combinations 활용
"""
import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
string = "9876543210"
string_comb = []
for i in range(1, 11):
    for comb in combinations(string, i):
        string_comb.append(int(''.join(list(comb))))

string_comb.sort()

if n >= len(string_comb):
    print(-1)
else:
    print(string_comb[n])
