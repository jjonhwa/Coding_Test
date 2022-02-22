import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
original = []
for _ in range(N):
    original.append(input())

answer = 0
for _ in range(M):
    check = input()
    if check in original:
        answer += 1
print(answer)