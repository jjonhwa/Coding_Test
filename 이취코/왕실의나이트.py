import sys
input = sys.stdin.readline

now = input()
present = []
present.append(ord(now[0]) - ord('a'))
present.append(int(now[1]) - 1)

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

cnt = 0
for i in range(8):
    x = present[0] + dx[i]
    y = present[1] + dy[i]
    if 0 <= x < 8 and 0 <= y < 8:
        cnt += 1
print(cnt)