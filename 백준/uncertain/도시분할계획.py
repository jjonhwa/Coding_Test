"""
    1. 스패닝 트리 생성
    2. 가장 높은 유지비를 가지는 간선 삭제

    시간복잡도: NlogN (? 헷갈림) => NlogM?
"""
from collections import deque

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

# 1. 스패닝 트리 생성
graph = []
for _ in range(m):
    a, b, weight = list(map(int, input().split()))
    graph.append((a, b, weight))
graph.sort(key = lambda x: x[2])
graph = deque(graph)

parent = [i for i in range(n+1)]

def find(x):
    if parent[x] == x:
        return x

    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

minimum_tree = []
edge_count = 0
weight_sum = 0
while True:

    # 최소 개수의 간선만을 탐색
    if edge_count == n-1:
        break

    a, b, weight = graph.popleft()

    # 사이클을 형성하지 않을 경우에만 간선을 스패닝 트리에 추가
    if find(a) != find(b):
        union(a, b)
        minimum_tree.append((a, b, weight))
        edge_count += 1

# 2. 가장 높은 유지비를 가지는 간선 삭제
minimum_tree.sort(key = lambda x: x[2])
weights = sum([node[2] for node in minimum_tree[:-1]])

print(weights)
