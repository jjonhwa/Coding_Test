"""
    양 끝 열/행에서 첫 열/행으로 이동 가능하다.

    비바라기 생성시
        1. (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름 생성
        2. 각각의 구름이 M번 이동
            2-1. 방향으로 이동 : ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 으로 이동 가능 (순서대로 1~8)
            2-2. 거리만큼 이동

    행동 순서
        1. 모든 구름이 "방향 + 거리"만큼 이동 (맨 처음 이동이 우선)
        2. 도착 위치의 바구니에 물이 1만큼 증가
        3. 구름 제거
        4. 물복사 버그
            4-1. 2에서 물이 증가한 칸에 대하여, 대각선 방향으로 이동
            4-2. 단, 물복사의 경우 격자를 벗어나는 경우는 취급하지 않음.
        5. 물의 양이 2이상일 경우 구름이 생성하고, 물이 2 줄어든다. 
            5-1. 단, 3에서 구름이 제거된 경우는 취급하지 않는다.
        6. 위를 M번 반복 후 물의 양의 합을 구한다.
"""
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

def moving(direction, size, x, y):
    """ 1. 모든 구름이 "방향 + 거리"만큼 이동 (맨 처음 이동이 우선) """
    if direction == 1: nx, ny = x, y-size
    elif direction == 2: nx, ny = x-size, y-size
    elif direction == 3: nx, ny = x-size, y
    elif direction == 4: nx, ny = x-size, y+size
    elif direction == 5: nx, ny = x, y+size
    elif direction == 6: nx, ny = x+size, y+size
    elif direction == 7: nx, ny = x+size, y
    else: nx, ny = x+size, y-size

    nx %= n
    ny %= n
        
    return nx, ny

def water_copy(x, y):
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]

    count = 0
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0<=nx<n and 0<=ny<n and graph[nx][ny]:
            count += 1

    return count

# (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름 생성
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

for _ in range(m):
    d, s = list(map(int, input().split()))

    # 1. 모든 구름이 "방향 + 거리"만큼 이동 (맨 처음 이동이 우선)
    increasing_water = set()
    while clouds: # 3. 구름 제거
        x, y = clouds.pop()
        nx, ny = moving(d, s, x, y)

        # 2. 도착 위치의 바구니에 물이 1만큼 증가
        graph[nx][ny] += 1
        increasing_water.add((nx, ny))

    # 4. 물복사 버그
    for water in increasing_water:
        x, y = water
        graph[x][y] += water_copy(x, y)

    # 5. 물의 양이 2이상일 경우 구름이 생성하고, 물이 2 줄어든다. 
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] >= 2 and (i, j) not in increasing_water:
                clouds.append((i, j))
                graph[i][j] -= 2

answer = sum([sum(row) for row in graph])
print(answer)
