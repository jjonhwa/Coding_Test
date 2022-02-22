import sys
from collections import deque
input = sys.stdin.readline

N, M, V = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

stack = []
visited = [False] * (N+1)
def dfs(graph, node):
    print(node, end = ' ')
    visited[node] = True
    graph[node].sort()
    for next in graph[node]:
        if not visited[next]:
            dfs(graph, next)
dfs(graph, V)
print()

queue = deque()
visited = [False] * (N+1)
def bfs(graph, node):
    queue.append(node)
    visited[node] = True
    while len(queue):
        now = queue.popleft()
        print(now, end = ' ')
        graph[now].sort()
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
bfs(graph, V)
