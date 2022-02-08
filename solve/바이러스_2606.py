import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # n <= 100
m = int(input()) # pair

graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
# graph = [[], [2,5], [1,3,5], [2], [7], [1,2,6], [5], [4]]

queue = deque()
road = [1]
visited[1] = True
for s in graph[1]:
    queue.append(s)

while len(queue):
    now = queue.popleft()
    if now not in road:
        road.append(now)

    for s in graph[now]:
        if not visited[s]:
            queue.append(s)
            visited[s] = True

print(len(road)-1)
