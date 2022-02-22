import sys
input = sys.stdin.readline

N = int(input())
balloon = list(map(int, input().split()))
balloon_index = [i for i in range(1,N+1)]

now = 0
explode = []
number = balloon.pop(now)
explode.append(balloon_index.pop(now))

while len(balloon):
    if number > 0:
        next = (now+number-1) % len(balloon)
    else:
        next = (now+number) % len(balloon)

    number = balloon.pop(next)
    explode.append(balloon_index.pop(next))
    now = next

for e in explode:
    print(e, end=' ')