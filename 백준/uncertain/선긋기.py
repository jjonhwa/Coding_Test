from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
lines = []
for i in range(n):
    a, b = list(map(int, input().split()))
    lines.append([a,b])   
lines.sort()

queue = deque(lines)
now = queue.popleft()

ans = 0
while len(queue):
    next = queue.popleft()
    if now[1] >= next[0]: 
        now = [min(now[0], next[0]), max(now[1], next[1])]
    else:
        ans += now[1] - now[0]
        now = next
ans += now[1] - now[0]
print(ans)
