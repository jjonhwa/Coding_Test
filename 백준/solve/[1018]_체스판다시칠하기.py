"""
    완전탐색

    O()
"""

import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    row = input().strip()
    row = list(row)

    graph.append(row)

start_black = []
start_white = []

for i in range(n):
    row = []
    for j in range(m):
        if (i+j) % 2 == 0:
            row.append("B")
        else:
            row.append("W")
    start_black.append(row)

for i in range(n):
    row = []
    for j in range(m):
        if (i+j) % 2 == 0:
            row.append("W")
        else:
            row.append("B")
    start_white.append(row)

def check_board(original, compare):
    count = 0
    for first_row, second_row in zip(original, compare):
        for first_col, second_col in zip(first_row, second_row):
            if first_col != second_col:
                count += 1
    return count

minimum_count = float("inf")
for i in range(len(graph) - 7):
    for j in range(len(graph[0]) - 7):
        original_graph = [graph[k][j:j+8] for k in range(i, i+8)]

        minimum_count = min(minimum_count, check_board(original_graph, start_black))
        minimum_count = min(minimum_count, check_board(original_graph, start_white))

print(minimum_count)