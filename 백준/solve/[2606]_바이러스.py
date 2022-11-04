"""
    BFS
"""
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
count = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(count):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def solution(graph):
    start = 1

    queue = deque()
    queue.append(start)

    visited = [False for _ in range(n+1)]
    visited[start] = True
    while queue:
        node = queue.popleft()

        for next_node in graph[node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
    
    return sum(visited) - 1

print(solution(graph))
