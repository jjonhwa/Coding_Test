import sys
import heapq
input = sys.stdin.readline

N = int(input())
number_list = []
for _ in range(N):
    insert = int(input())
    if insert == 0:
        if number_list:
            pop_number = heapq.heappop(number_list)[1]
            print(pop_number)
        else:
            print(0)
    else:
        heapq.heappush(number_list, (-insert, insert))
