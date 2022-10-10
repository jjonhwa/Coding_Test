"""
1. "모든 벡터의 합" 벡터: v = (x1(절반의 합) - x2(나머지 절반의 합), y1(절반의 합) - y2(나머지 절반의 합))
2. 길이 구하기 (sqrt(x^2 + y^2))
"""

# from itertools import combinations

# import sys
# import math


# input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
#     n = int(input())

#     space = []

#     import time
#     start_time = time.perf_counter()

#     for _ in range(n):
#         dot = list(map(int, input().split()))
#         space.append(dot)

#     x_sum = sum(list(map(lambda x: x[0], space)))
#     y_sum = sum(list(map(lambda x: x[1], space)))

#     half = n // 2 # n은 무조건 짝수
#     combination = list(combinations(space, half))
#     comb_count = len(combination) // 2
#     minimum_value = float("inf")
#     for comb in combination[:comb_count]:        
#         half_sum_x = sum(list(map(lambda x: x[0], comb)))
#         half_sum_y = sum(list(map(lambda x: x[1], comb)))
#         other_sum_x = x_sum - half_sum_x
#         other_sum_y = y_sum - half_sum_y

#         vector_summation = math.sqrt((half_sum_x - other_sum_x) ** 2 + (half_sum_y - other_sum_y) ** 2)
#         minimum_value = min(minimum_value, vector_summation)

#     print(minimum_value)
#     print(f"test2: {time.perf_counter() - start_time:.2f}초")


### 소미님
# import sys
# import math

# T = int(sys.stdin.readline())


# def sol(cnt, prev, x, y):
#     global ans
#     if cnt == N // 2:
#         cal = math.sqrt(x**2 + y**2)
#         ans = cal if ans > cal else ans
#         return
#     for i in range(prev, N):
#         print(ans)
#         sol(cnt+1, i+1, x-2*point[i][0], y-2*point[i][1])


# while T > 0:
#     ans = int(1.7*(10**308)) #double 최댓값

#     N = int(sys.stdin.readline())
#     isC = [False for _ in range(N)]
#     point = []
#     sumx = 0
#     sumy = 0
#     for n in range(N):
#         x, y = map(int, sys.stdin.readline().split())
#         point.append([x, y])
#         sumx += point[n][0]
#         sumy += point[n][1]

#     sol(0, 0, sumx, sumy);
#     print(ans)
#     T-=1

# import sys
# import math

# T = int(sys.stdin.readline())
# ans = int(1.7*(10**308)) #double 최댓값

# def sol(cnt, prev, x, y):
#     global ans
#     if cnt == N // 2:
#         cal = math.sqrt(x**2 + y**2)
#         ans = cal if ans > cal else ans
#         return
#     sol(cnt+1, prev+1, x-2*point[prev][0], y-2*point[prev][1])


# while T > 0:
#     N = int(sys.stdin.readline())
#     isC = [False for _ in range(N)]
#     point = []
#     sumx = 0
#     sumy = 0
#     for n in range(N):
#         x, y = map(int, sys.stdin.readline().split())
#         point.append([x, y])
#         sumx += point[n][0]
#         sumy += point[n][1]

#     ans = int(1.7*(10**308))
#     sol(0, 0, sumx, sumy);
#     print(ans)
#     T-=1

### 유성님
from sys import stdin, maxsize
from itertools import combinations
from math import sqrt

input = stdin.readline().rstrip()

MIN_N = 2
MAX_N = 20
comb_list = [[] for _ in range(MAX_N + 1)]
# comb_list[i]: i개의 좌표 중 앞에 부호 '-'를 붙일 좌표 i/2개를 뽑는 경우들을 미리 만들어 놓은 리스트
# comb_list[i]는 [1 or -1 for j in range(i)]를 원소로 가짐
# comb_list[i][j]: j번째 좌표 앞에 붙는 계수(부호)


# T의 값이 못해도 두 자릿수 이상은 되는 것 같네요.
# 전처리: comb_list 만들기
def init():
    for i in range(MIN_N, MAX_N + 1, 2):
        for p in combinations(range(i), i // 2):
            opr_list = [1] * i
            for pos in p:
                opr_list[pos] = -1
            comb_list[i].append(opr_list)


def solution() -> float:
    N = int(input())
    coord_list = [tuple(map(int, input().split())) for i in range(N)]

    INF = maxsize
    ans = INF
    for opr_list in comb_list[N]:
        sx, sy = 0, 0
        for (x, y), opr in zip(coord_list, opr_list):
            sx += opr * x
            sy += opr * y
        ans = min(ans, sx ** 2 + sy ** 2)
    return sqrt(ans)
    # sqrt 연산이 무겁기 때문에 마지막 정답을 반환할 때만 호출함


if __name__ == '__main__':
    init()
    print(comb_list[3])
    # T = int(input())
    # for _ in range(T):
    #     print(solution())