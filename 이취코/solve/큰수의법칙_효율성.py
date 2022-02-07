# 시간 효율 100억 이상일 경우 통과
N, M, K = list(map(int, input().split()))
number = [num for num in map(int, input().split())]

# 결국, 가장 큰 2개의 숫자만 사용
ans = 0
number.sort(reverse=True)
first, second = number[:2]
total_count = M // (K+1) # K+1로 M을 나눴을 때의 몫

ans = (first*K + second) * total_count + first * (M%(K+1))
print(ans)