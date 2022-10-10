"""
1. gem과 bag을 정렬
2. gem과 bag을 비교하면서 gem의 무게가 bag의 무게를 초과할 경우, 이전 gem을 bag에 삽입
3. bag이 남아있고, gem의 무게가 bag보다 작을 경우, bag에 gem을 삽입
"""
import sys
import heapq

from collections import deque

input = sys.stdin.readline

n, k = list(map(int, input().split()))

gem = []
for _ in range(n):
    m, v = list(map(int, input().split()))
    gem.append((m, v))
gem.sort(key = lambda x: (x[0], -x[1]))
gem = deque(gem)

bags = []
for _ in range(k):
    bags.append(int(input()))
bags.sort()
bags = deque(bags)


max_value = []
answer = 0
while gem and bags:
    weight, value = gem.popleft()

    if max_value:
        _, before_value, before_weight = max_value[0]

        if (before_weight <= bags[0] and weight > bags[0]) or (before_weight == weight == bags[0]):
            answer += before_value
            bags.popleft()
            heapq.heappop(max_value)
    heapq.heappush(max_value, [-value, value, weight])

while bags and max_value:
    bag = bags.popleft()
    _, value, weight = max_value[0]
    if weight <= bag:
        heapq.heappop(max_value)
        answer += value

print(answer)