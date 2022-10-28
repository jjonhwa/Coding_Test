from collections import deque, defaultdict

import sys
input = sys.stdin.readline

n = int(input())

condition_dict = defaultdict(set)
building_time = defaultdict(int)

complete_time = [0 for _ in range(n+1)]

graph = [[] for _ in range(n+1)]

start_building = []
for i in range(n):
    about_building = list(map(int, input().split()))
    about_building = about_building[:-1]

    building_num = i+1
    building_time[building_num] = about_building[0]

    if len(about_building) == 1:
        building_condition = set()
        start_building.append(building_num)
        complete_time[building_num] = building_time[building_num]
    else:
        building_condition = set(about_building[1:])
    
    condition_dict[building_num] = building_condition
    for go in building_condition:
        graph[go].append(building_num)

queue = deque(start_building)
while queue:
    building_num = queue.popleft()

    for next_building in graph[building_num]:
        condition_dict[next_building].remove(building_num)
        complete_time[next_building] = max(complete_time[next_building], complete_time[building_num] + building_time[next_building])

        if not condition_dict[next_building]:
            queue.append(next_building)

for i in range(1, len(complete_time)):
    print(complete_time[i])

