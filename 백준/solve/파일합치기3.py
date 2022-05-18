import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    num_list = list(map(int, input().split()))

    answer = 0
    heapq.heapify(num_list)
    while len(num_list) != 1:
        first_min = heapq.heappop(num_list)
        second_min = heapq.heappop(num_list)

        answer += first_min + second_min
        heapq.heappush(num_list, first_min + second_min)
    print(answer)
