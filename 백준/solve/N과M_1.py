import sys
from itertools import permutations
input = sys.stdin.readline

N, M = list(map(int, input().split()))
number_list = [i+1 for i in range(N)]
perm = list(permutations(number_list, M))

for p in perm:
    for i in range(len(p)-1):
        print(p[i], end = ' ')
    print(p[-1])