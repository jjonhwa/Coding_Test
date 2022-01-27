# N = 1000, M = 500000
# 위상정렬 코드를 보며 풀이
from collections import deque
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]
answer = [0] * (N+1)
for _ in range(M):
    A, B = list(map(int, input().split()))
    indegree[B] += 1
    graph[A].append(B)


queue = deque()
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        queue.append(i)
        answer[i] = 1

for _ in range(1, len(indegree)):
    target = queue.popleft()

    for next in graph[target]:
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)
            answer[next] = answer[target] + 1

for i in range(1, len(answer)):
    print(answer[i], end=' ')