import heapq
import sys
input = sys.stdin.readline

left_heap = []
right_heap = []

answer_check = []
n = int(input())

# n이 1 또는 2인 경우
if n == 1 or n == 2:
    value_list = []
    for _ in range(n):
        value = int(input())
        value_list.append(value)
        print(min(value_list))
# n이 3 이상인 경우
else:
    n1 = int(input())
    print(n1)
    n2 = int(input())

    if n1 > n2:
        left_heap.append((-n2, n2))
        right_heap.append(n1)
    else:
        left_heap.append((-n1, n1))
        right_heap.append(n2)
    print(left_heap[0][1])

    for i in range(2, n):
        value = int(input())

        max_left = heapq.heappop(left_heap)[1]
        min_right = heapq.heappop(right_heap)

        if len(left_heap) == len(right_heap): # left에 2개, right에 1개 삽입
            if value > min_right: # value를 right에 삽입
                heapq.heappush(left_heap, (-max_left, max_left))
                heapq.heappush(left_heap, (-min_right, min_right))
                heapq.heappush(right_heap, value)
            else: # value를 left에 삽입
                heapq.heappush(left_heap, (-max_left, max_left))
                heapq.heappush(left_heap, (-value, value))
                heapq.heappush(right_heap, min_right)
        else: # right에 2개, left에 1개 삽입
            if value < max_left: # value를 left에 삽입
                heapq.heappush(left_heap, (-value, value))
                heapq.heappush(right_heap, max_left)
                heapq.heappush(right_heap, min_right)
            else: # value를 right에 삽입
                heapq.heappush(left_heap, (-max_left, max_left))
                heapq.heappush(right_heap, min_right)
                heapq.heappush(right_heap, value)
        
        print((left_heap[0][1]))