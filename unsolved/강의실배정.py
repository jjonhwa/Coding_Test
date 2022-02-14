import sys
import heapq
input = sys.stdin.readline

# 1000000000
N = int(input())
studying = []
for _ in range(N):
    studying.append(list(map(int, input().split())))

studying.sort(key = lambda x: x[0])
heap = []
heapq.heappush(heap, studying[0][1])
for i in range(1, len(studying)):
    # 가장 빨리 종료되는 강의실의 시간이 그 다음 시작 시간보다
    # 늦을 경우, heap에 추가
    if heap[0] > studying[i][0]: 
        heapq.heappush(heap, studying[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, studying[i][1])

print(len(heap))
