"""
    목적
        지나갈 수 있는 길의 개수 출력 (처음부터 끝까지 이동 가능해야함)

    이동 방식
        1. 길에 속한 모든 칸의 높이가 모두 같아야 한다.
        2. 경사로를 삽입하여 이동 가능.
            2-1. 경사로의 높이는 1, 길이는 L이다.
            2-2. 길이 L만큼, 바닥이 존재해야 한다.
            2-3. 높이 차이는 단지 1이어야 한다.

    풀이
        N <= 100이므로 완전 탐색 수행

        1. 길을 기준으로 List 생성
        2. 조건을 순서대로 수행
"""

from collections import Counter
import sys
input = sys.stdin.readline

n, l = list(map(int, input().split()))
graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 1. 길을 기준으로 List 생성
roads = []
for i in range(len(graph)):
    roads.append(graph[i])

transpose_graph = list(map(list, zip(*graph)))
for i in range(len(transpose_graph)):
    roads.append(transpose_graph[i])

# 2. 조건을 순서대로 수행
def same_label(road):
    """ 모든 칸의 높이가 모두 같을 경우 """
    road_dict = Counter(road)
    if len(road_dict.items()) == 1:
        return True
    else:
        return False

def install_slope(road, L):
    """ 경사로를 설치하면서 지나갈 수 있는가? """

    idx, length = 0, 1
    while idx < len(road)-1:
        
        # 높이가 2이상 차이난다면 지나갈 수 없는 길
        if abs(road[idx] - road[idx+1]) > 1:
            return False
        
        # 높이가 같다면, idx, length를 높여주고 continue
        if road[idx] == road[idx+1]:
            idx += 1
            length += 1
        
        # 다음 칸이 현재 칸보다 1칸 높다면 => 앞에 경사로 설치 가능한지 판단
        elif road[idx] == road[idx+1] - 1:
            if length >= L:
                length = 1
                idx += 1 # 올라갔을 떄는 올라간 다음 위치로 지정
            else:
                return False
        
        # 다음 칸이 현재 칸보다 1칸 낮다면 => 이후에 경사로 설치가 가능한지 판단
        else:
            # 길이 초기화 및 idx를 다음 칸으로 이동
            length = 1
            idx += 1

            # 경사로의 가로 길이만큼 이동 가능한지 판단
            while True:
                if length == L: # 설치 했다! break
                    length = 0 # 내려갔을 때는 idx를 내려온 위치로 지정
                    break
                elif idx >= len(road)-1: # 설치 못했는데 길이 넘어갔다! => False
                    return False
                
                if road[idx] == road[idx + 1]:
                    idx += 1
                    length += 1
                else:
                    return False

    return True

answer = 0
for road in roads:
    if same_label(road):
        answer += 1
    else:
        if install_slope(road, l):
            answer += 1
    
print(answer)