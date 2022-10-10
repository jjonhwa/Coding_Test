"""
건물 짓는 순서 x => 두 게임에서 건물을 짓는 순서가 다를 수 있다.

매 게임 시작 시 건물 짓는 순서가 주어진다.
모든 건물은 건설 시작 => 건설 완성 까지의 건축 시간이 존재한다.
동시에 건물을 지을 수 있다.

받는 화살이 두 개이상이라면 주는 화살의 건물이 전부 지어져야지 받는 건물을 지을 수 있다.

1. Graph를 통해 Root Node를 찾는다. (어떠한 화살표가 없어도 지을 수 있는 건물)
2. 각 Root Node로부터 시작해서 w개의 건물을 건설
"""

import sys
from collections import deque

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    building_count, rule_count = map(int, input().split())
    building_time = list(map(int, input().split()))
    building_time = [[i, t] for i, t in enumerate(building_time)]

    # rule_graph => 순차적으로 찾아가기 위한 Graph
    # root => 받는 화살표가 없는 Building
    give_graph = [[] for _ in range(building_count)]
    take_graph = [[] for _ in range(building_count)]
    take_compare_graph = [[] for _ in range(building_count)]
    for _ in range(rule_count):
        give, take = map(int, input().split())
        give_graph[give-1].append(take-1)
        take_graph[take-1].append(give-1)

    # find root building (받는 화살표가 없을 경우 Root Building이다.)
    building = deque([])
    for i in range(len(take_graph)):
        if take_graph[i] == []:
            building.append(building_time[i])
    
    target_number = int(input())

    total_time = 0
    while True:
        building = sorted(building, key = lambda x: x[1]) 
        print(building)
        building = deque(building)

        building_index, time = building.popleft()

        total_time += time
        for i in range(len(building)):
            building[i][1] -= time
        
        next_building = give_graph[building_index]
        for nb in next_building:
            take_compare_graph[nb].append(building_index)

            if set(take_compare_graph[nb]) == set(take_graph[nb]): # 삽입 순서 때문
                building.append(building_time[nb])

        if building_index == target_number-1:
            break

    print(total_time)

"""
sorted => TC: O(10000) + O(1000) + O(1000)
while => TC: O(1000)

Time Complexity: O(N^2 log N)
"""


import sys
import heapq

input = sys.stdin.readline
test_case = int(input())

for _ in range(test_case):
    building_count, rule_count = map(int, input().split())
    building_time = list(map(int, input().split()))
    building_time = [[t, i] for i, t in enumerate(building_time)]

    # rule_graph => 순차적으로 찾아가기 위한 Graph
    # root => 받는 화살표가 없는 Building
    give_graph = [[] for _ in range(building_count)]
    take_graph = [[] for _ in range(building_count)]
    take_compare_graph = [[] for _ in range(building_count)]
    for _ in range(rule_count):
        give, take = map(int, input().split())
        give_graph[give-1].append(take-1)
        take_graph[take-1].append(give-1)

    # find root building (받는 화살표가 없을 경우 Root Building이다.)
    building = []
    for i in range(len(take_graph)):
        if take_graph[i] == []:
            building.append(building_time[i])
    heapq.heapify(building)

    target_number = int(input())

    total_time = 0
    while building:
        # print(building)
        time, building_index = heapq.heappop(building)

        total_time += time
        for i in range(len(building)):
            building[i][0] -= time
        
        next_building = give_graph[building_index]
        for nb in next_building:
            take_compare_graph[nb].append(building_index)

            # if set(take_compare_graph[nb]) == set(take_graph[nb]): # 삽입 순서 때문
            #     heapq.heappush(building, building_time[nb])

            if len(take_compare_graph[nb]) == len(take_graph[nb]): # 삽입 순서 때문
                heapq.heappush(building, building_time[nb])
                
        if building_index == target_number-1:
            break

    print(total_time)
