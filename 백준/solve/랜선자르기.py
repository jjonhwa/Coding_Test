import sys
input = sys.stdin.readline

K, N = list(map(int, input().split()))
lensun = []
for _ in range(K):
    lensun.append(int(input()))

# 0으로 나누었을 때의 예외처리
def count_check(cutting, lensun):
    cnt = 0
    if cutting == 0: # start = 0, end = 1일 경우
        for sun in lensun:
            cnt += sun
        return cnt
    for sun in lensun:
        cnt += sun // cutting
    return cnt

start = 0
end = max(lensun)
ans = []
while start <= end:
    mid = (start + end) // 2

    # 개수 체크
    count = count_check(mid, lensun)
    if count >= N:
        start = mid + 1
        ans.append(mid)
    elif count < N:
        end = mid - 1
print(max(ans))
