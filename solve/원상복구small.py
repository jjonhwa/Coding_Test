import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
S = list(map(int, input().split()))
D = list(map(int, input().split()))

# S: 4 1 3 5 2
# D: 4 3 1 2 5
# P: 3 5 1 4 2
for _ in range(K):
    P = [0] * (N+1)
    for s, d in zip(S, D):
        P[d] = s
    S = P[1:]

for element in P[1:]:
    print(element, end=' ')
