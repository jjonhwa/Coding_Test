import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # list to heap
    
    first = heapq.heappop(scoville)
    second = heapq.heappop(scoville)
    while first < K or second < K:
        answer += 1
        
        mixed = first + second * 2
        heapq.heappush(scoville, mixed)
        
        if len(scoville) == 1: # scoville이 1개밖에 없다면 break
            break
            
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
    
    if len(scoville) == 1 and scoville[0] < K:
        return -1
    else:
        return answer