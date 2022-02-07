import sys
input = sys.stdin.readline

N = int(input())
moving = map(str, input().split())
now = [0, 0]
for m in moving:
    if m == 'R' and now[1]+1 < N:
        now[1] += 1
    elif m == 'L' and 0 <= now[1]-1:
        now[1] -= 1
    elif m == 'D' and now[0]+1 < N:
        now[0] += 1
    elif m == 'U' and 0 <= now[0]-1:
        now[0] -= 1

for n in now:
    print(n+1, end = ' ') 