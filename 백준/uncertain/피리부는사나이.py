"""
1. 모든 점에서 시작
2. visited 했을 경우 방문 x
3. 시작지점의 개수 count
"""
from collections import deque

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    row = input().strip()
    graph.append(list(row))

def go_direction(x, y, direction):
    if direction == 'D':
        return x+1, y
    elif direction == "L":
        return x, y-1
    elif direction == "R":
        return x, y+1
    else:
        return x-1, y

visited = [[0 for _ in range(m)] for _ in range(n)]

connection = []
num = 0
for i in range(len(graph)):
    for j in range(len(graph[0])):

        if visited[i][j] != 0:
            continue

        # BFS
        num += 1
        go = [[i, j]]
        visited[i][j] = num

        while go:
            x, y = go.pop()
            direction = graph[x][y]

            nx, ny = go_direction(x, y, direction)

            if visited[nx][ny] != num and visited[nx][ny] != 0:
                # 연결 관계 추가 후 종료
                connection.append([visited[nx][ny], num])
            elif visited[nx][ny] == 0:
                go.append([nx, ny])
                visited[nx][ny] = num

# 전체 node 생성
candidate = set()
for r in visited:
    for c in r:
        candidate.add(c)
candidate = [0] + list(candidate)

# 분리집합을 활용하여 연결 관계에 따른 node 번호 갱신
def find(x):
    if candidate[x] == x:
        return x

    candidate[x] = find(candidate[x])
    return candidate[x]

def union(a, b):
    if a < b:
        candidate[b] = a
    else:
        candidate[b] = b

for a, b in connection:
    parent_a = find(a)
    parent_b = find(b)

    union(parent_a, parent_b)

print(len(set(candidate)) - 1)

