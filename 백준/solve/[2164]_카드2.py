from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
num_list = [i+1 for i in range(n)]

queue = deque(num_list)
insert = False
while queue:
    num = queue.popleft()

    if insert:
        queue.append(num)
        insert = False
    else:
        insert = True

print(num)