from itertools import permutations
from collections import deque

import sys
input = sys.stdin.readline

original_graph = []
for _ in range(4):
    row = list(input().strip())
    original_graph.append(row)

compare_graph = []
while True:
    row = input().strip()
    if row:
        compare_graph.append(list(row))
        break

for _ in range(3):
    row = list(input().strip())
    compare_graph.append(row)

mismatch_P = []
mismatch_L = []
for i, (o_row, c_row) in enumerate(zip(original_graph, compare_graph)):
    for j, (o, c) in enumerate(zip(o_row, c_row)):
        if o != c:
            if o == "P":
                mismatch_P.append((i, j))
            else:
                mismatch_L.append((i, j))

comb_list = []
for perm in permutations(mismatch_P, len(mismatch_L)):
    comb_list.append(list(zip(perm, mismatch_L)))

def count_distance(px, py, lx, ly):
    """ 
        P에서 L로 갈 때, 최소 교체 횟수 

        최소 교체 횟수 = 최대 교체 횟수 - max(P개수, L개수)
    """
    if px <= lx and py < ly:
        dx = [1, 0]
        dy = [0, 1]
    elif lx <= px and ly < py:
        dx = [-1, 0]
        dy = [0, -1]
    elif px > lx and py <= ly:
        dx = [-1, 0]
        dy = [0, 1]
    else:
        dx = [1, 0]
        dy = [0, -1]

    limit_x = (min(px, lx), max(px, lx))
    limit_y = (min(py, ly), max(py, ly))

    queue = deque()
    queue.append((px, py, 0, 0, 0)) # x좌표, y좌표, P개수, L개수, distance

    distance = abs(px - lx) + abs(py - ly)
    max_count = float("-inf")
    while queue:
        x, y, p_count, l_count, dist = queue.popleft()  

        if dist > distance:
            continue

        if (x, y) == (lx, ly):
            max_count = max(max_count, p_count, l_count-1)
            continue

        for i in range(2):
            nx, ny = x+dx[i], y+dy[i]

            if limit_x[0]<=nx<=limit_x[1] and limit_y[0]<=ny<=limit_y[1]:
                if original_graph[nx][ny] == "P":
                    queue.append((nx, ny, p_count + 1, l_count, dist +1))
                else:
                    queue.append((nx, ny, p_count, l_count + 1, dist +1))
    
    return (2*distance - 1) - max_count

min_count = float("inf")
for comb in comb_list:
    count = 0

    for P, L in comb:
        px, py = P
        lx, ly = L

        count += count_distance(px, py, lx, ly)

    min_count = min(min_count, count)

print(min_count)