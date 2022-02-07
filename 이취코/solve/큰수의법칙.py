# 시간 효율 100억 이상일 경우 시간초과
N, M, K = list(map(int, input().split()))
number = [num for num in map(int, input().split())]

# 결국, 가장 큰 2개의 숫자만 사용
ans = 0
number.sort(reverse=True)
first, second = number[:2]
divide_check = K+1
for i in range(M):
    if i % divide_check == 3:
        ans += second
    else:
        ans += first
print(ans)
