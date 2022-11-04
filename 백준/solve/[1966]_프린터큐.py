from collections import defaultdict, deque

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = list(map(int, input().split()))
    num_list = list(map(int, input().split()))


    queue = deque()
    for i in range(len(num_list)):
        queue.append((i, num_list[i]))
        
    num_list.sort()

    answer_dict = defaultdict(int)
    count = 0
    while queue:
        idx, number = queue.popleft()

        if number == num_list[-1]:
            num_list.pop()
            count += 1
            if idx == m:
                break
        else:
            queue.append((idx, number))

    print(count)
