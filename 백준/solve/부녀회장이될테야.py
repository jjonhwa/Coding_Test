import sys
input = sys.stdin.readline

T = int(input())

house = [[0] * 16 for _ in range(16)]
for i in range(1, 16):
    for j in range(1, 16):
        if i == 1:
            house[i][j] = j
        else:
            house[i][j] = sum(house[i-1][:j+1])

for _ in range(T):
    k = int(input())
    n = int(input())
    print(house[k+1][n])
