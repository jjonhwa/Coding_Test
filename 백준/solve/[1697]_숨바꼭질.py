"""
    BFS
"""
from collections import deque
import sys
input = sys.stdin.readline

n, k = list(map(int, input().split()))


def find_k(start, k):
    queue = deque()
    queue.append((start, 0)) # 시작지점, 이동횟수
    visited = [False for _ in range(100001)]
    visited[start] = True

    while queue:
        now, dist = queue.popleft()

        if now == k:
            return dist
        
        if now-1 >= 0 and not visited[now-1]:
            queue.append((now-1, dist+1))
            visited[now-1] = True

        if now+1 <= 100000 and not visited[now+1]:
            queue.append((now+1, dist+1))
            visited[now+1] = True

        if now*2 <= 100000 and not visited[now*2]:
            queue.append((now*2, dist+1))
            visited[now*2] = True


print(find_k(n, k))