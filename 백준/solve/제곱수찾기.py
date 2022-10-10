"""
완전탐색

1. 행의 번호 등차수열
2. 열의 번호 등차수열
3. 완전 제곱수 중 가장 큰 수

코딩순서
1. 행, 열에 대한 모든 등차수열 조합 만들기
2. 제곱수일 경우, 정답후보
"""

import sys
import math

input = sys.stdin.readline

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):
    row = list(input().strip())
    graph.append(row)

answer = -1
for i in range(n):
    for  j in range(m):
        
        for row_interval in range(-8, 9):
            if i+row_interval < 0 or i+row_interval >= n:
                continue

            for col_interval in range(-8, 9):
                if j+col_interval < 0 or j+col_interval >= m:
                    continue

                cand = graph[i][j]
                x, y = i, j
                while True:
                    if row_interval == 0 and col_interval == 0:
                        if int(math.sqrt(float(cand))) == math.sqrt(float(cand)):
                            answer = max(answer, int(cand))
                        break

                    nx, ny = x+row_interval, y+col_interval
                    if 0<=nx<n and 0<=ny<m:
                        cand += graph[nx][ny]
                        x, y = nx, ny

                        if int(math.sqrt(float(cand))) == math.sqrt(float(cand)):
                            answer = max(answer, int(cand))
                    else:
                        break

print(answer)
