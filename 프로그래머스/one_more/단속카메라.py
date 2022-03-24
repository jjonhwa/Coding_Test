from collections import deque

def solution(routes):
    answer = 0
    routes.sort(key = lambda x: x[0]) # start를 기준으로 정렬
    
    queue = deque(routes)
    while queue:
        start, end = queue.popleft()
        
        while queue:
            if queue[0][0] > end:     # 다음 start가 현재 end보다 클 경우 break => 새로 시작
                break
            elif queue[0][1] < end:   # 다음 end가 현재 end보다 작을 경우 현재 end를 다음 end로 update 후 반복 (즉, 포함되어 있을 경우 더 작은 end로 update) 
                end = queue[0][1]
                queue.popleft()
                continue
            else:
                queue.popleft()       # 아무 곳에도 해당하지 않을 경우, 뺴주기만 한 후 반복
        
        answer += 1
    
    return answer