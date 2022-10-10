"""
1. 각 Node 별 자식 Node의 최대 가중치 합
2. 가장 큰 2개의 자식 Node 값을 선택
"""

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, w = list(map(int, input().split()))
    tree[a].append([b, w])

# 1. 각 Node 별 자식 Node의 최대 가중치 합
maximum_weight = [[0] for _ in range(n+1)] # left sum, right sum
def find_maximum_weight(node):
    for child, weight in tree[node]:
        now_weight = weight + find_maximum_weight(child)

        maximum_weight[node].append(now_weight)
    return max(maximum_weight[node])

find_maximum_weight(1)

# 2. 가장 큰 2개의 자식 Node 값을 선택
answer = 0
for i in range(len(maximum_weight)):
    if len(maximum_weight[i]) >= 3:
        max_weight = sorted(maximum_weight[i])
        max_1, max_2 = max_weight[-1], max_weight[-2]
        answer = max(answer, max_1+max_2)
    elif len(maximum_weight[i]) == 2:
        max_weight = sorted(maximum_weight[i])
        answer = max(answer, max_weight[-1])
print(answer)