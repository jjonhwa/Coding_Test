import sys
input = sys.stdin.readline

N = int(input())
grade = []
for _ in range(N):
    name, score = map(str, input().split())
    grade.append([name, int(score)])
grade.sort(key = lambda x: x[1])

for g in grade:
    print(g[0], end = ' ')