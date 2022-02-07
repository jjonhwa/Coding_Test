import sys
input = sys.stdin.readline

N, K = list(map(int, input().split()))
cnt = 0
while True:
    if N % K == 0: # N이 K로 나누어떨어지면
        N //= K # K로 나눴을 때의 몫을 N에 입력
        cnt += 1
    else:
        N -= 1
        cnt += 1
    if N == 1:
        break
print(cnt)
