"""
    주사위의 이동
    1. 이동방향으로 한 칸 이동.
        1-1. 만약 칸이 없다면, 이동 방향을 반대로 전환 후 한 칸 이동
    2. 도착한 칸의 "점수"를 획득
        2-1. 점수: 도착한 칸의 "정수"와 같은 값으로 이어져 있는 칸의 개수 x "정수"
    3. 주사위 아랫면 (A)  vs  현재 칸의 "정수" (B)
        3-1. A > B: 90도 시계방향으로 회전
        3-2. A < B: 90도 반시계방향 회전
        3-3. A = B: 이동방향 그대로
"""
from collections import deque

import sys
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 방향 및 주사위 초기화
direction = 1 # 1: 동쪽, 2: 남쪽, 3: 서쪽, 4: 북쪽
dice = [6, 3, 2, 4, 5, 1] # [아래, 동, 남, 서, 북 , 위]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def move(x, y, direction):
    """ 1. 이동방향으로 한 칸 이동"""
    if direction == 1:
        nx, ny = x, y+1
    elif direction == 2:
        nx, ny = x+1, y
    elif direction == 3:
        nx, ny = x, y-1
    else:
        nx, ny = x-1, y

    if 0<=nx<n and 0<=ny<m:
        return nx, ny, direction
    else:
        if direction == 1 or direction == 2:
            direction += 2
        else:
            direction -= 2
        
        return move(x, y, direction)

def move_dice(dice, direction):
    """ 주사위 굴리기 """
    if direction == 1: # 동쪽으로 굴림
        dice[0], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[0]
    elif direction == 3: # 서쪽으로 굴림
        dice[0], dice[3], dice[5], dice[1] = dice[3], dice[5], dice[1], dice[0]
    elif direction == 4: # 남쪽으로 굴림
        dice[0], dice[2], dice[5], dice[4] = dice[2], dice[5], dice[4], dice[0]
    else: # 북쪽으로 굴림
        dice[0], dice[4], dice[5], dice[2] = dice[4], dice[5], dice[2], dice[0]
    return dice

def get_score(x, y):
    """ 점수 획득 """
    integer = graph[x][y]
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 1

    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] == integer:
                visited[nx][ny] = True
                queue.append((nx, ny))
                count += 1

    return integer * count

def turnabout(x, y, dice, direction):
    """ 방향 전환 """
    a = dice[0]
    b = graph[x][y]

    if a > b:
        direction += 1
        if direction == 4:
            direction = 1
    elif a < b:
        direction -= 1
        if direction == 0:
            direction = 4
    return direction
        

answer = 0
x, y = 0, 0

# 1: 동쪽, 2: 남쪽, 3: 서쪽, 4: 북쪽
for _ in range(k):

    # 위치 이동
    nx, ny, direction = move(x, y, direction)

    # 점수 획득
    answer += get_score(nx, ny)
    
    # 주사위 이동
    dice = move_dice(dice, direction)  

    
    # 방향 전환
    direction = turnabout(nx, ny, dice, direction)
    x, y = nx, ny

    print("주사위:", dice)
    print("방향:", direction)
    print("-" * 50)
print(answer)
