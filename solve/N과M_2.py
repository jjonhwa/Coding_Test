import sys
from itertools import combinations
input = sys.stdin.readline

N, M = list(map(int, input().split()))

number_list = [i+1 for i in range(N)]
for comb in combinations(number_list, M):
    for c in comb:
        print(c, end = ' ')
    print()