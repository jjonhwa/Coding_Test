import sys
input = sys.stdin.readline

N = int(input())
food = list(map(int, input().split()))

max_food = [0] * (len(food) + 1)
for i in range(1, len(food)):
    if i == 1 :
        max_food[i] = food[i]
        continue
    elif i == 2:
        max_food[i] = max(food[i], max_food[i-1])
        continue
    max_food[i] = max(max_food[i-1], max_food[i-2]+food[i])
print(max(max_food))