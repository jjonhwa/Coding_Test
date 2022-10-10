"""
보드의 크기 N x N, 사과의 개수 K
사과의 위치를 [행, 열]로 입력 (1x1에는 존재하지 않는다.)
1x1에서 뱀은 움직이기 시작. 오른쪽을 보고 있다.

뱀의 방향 변환
X초 후 L or D로 90도 회전

종료조건 
    1. 벽에 부딪힘. 
    2. 자신의 몸과 부딪힘.
이동조건
    1. 몸을 늘려 이동. 
    2. 사과가 있다면 Stop.
    3. 사과가 없다면 몸을 줄임.
"""

import sys

from collections import deque
from typing import List
input = sys.stdin.readline

# 보드 작성 => 0으로 가득채워진 N x N 보드
n = int(input())
graph = [[0] * n for _ in range(n)]

# 사과 입력
apple = int(input())
for _ in range(apple):
    r, c = list(map(int, input().split()))
    graph[r-1][c-1] = 2

# 변환지점 입력
move = int(input())
move_point = []
for _ in range(move):
    move_point.append(list(input().split()))
move_point = [[int(mp[0]), str(mp[1])]for mp in move_point]
move_point.sort(key = lambda x: x[0]) # X(초)를 기준으로 오름차순 정렬
move_point = deque(move_point)

# 이동 시작
now = [0, 0]
graph[now[0]][now[1]] = 1
go = 0 # 진행방향 (0: 오, 1: 아, 2: 왼, 3: 위)
time = 0

def rotate(direction: int, rotation: str) -> int:
    if rotation == 'D': # 오른쪽 회전
        direction += 1
        if direction == 4:
            direction = 0
    else: # 왼쪽 회전
        direction -= 1
        if direction == -1:
            direction = 3
    return direction    

turning_point = move_point.popleft()
snake = deque([[0, 0]])
while True:
    time += 1 # 1초 증가

    r, c = now
    # 머리 위치 이동
    if go == 0:
        now = [r, c+1] 
    elif go == 1:
        now = [r+1, c]
    elif go == 2:
        now = [r, c-1]
    else:
        now = [r-1, c]
    snake.append(now)

    # 머리가 벽에 부딪히거나 자기 몸에 부딪힐 경우 break
    if now[0] < 0 or now[0] >= n or now[1] < 0 or now[1] >= n or graph[now[0]][now[1]] == 1:
        break

    # 사과 여부 판단 (O) 
    if graph[now[0]][now[1]] == 2:
        graph[now[0]][now[1]] = 1
        pass
    else:
        # 사과 여부 판단 (X) ===> 맨 뒤의 꼬리를 0으로 변환
        graph[now[0]][now[1]] = 1
        tail = snake.popleft()
        graph[tail[0]][tail[1]] = 0

    # 방향 전환
    if time == turning_point[0]:
        go = rotate(go, turning_point[1])
        if move_point:
            turning_point = move_point.popleft()

print(time)

