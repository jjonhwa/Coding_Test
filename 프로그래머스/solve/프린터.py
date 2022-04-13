def solution(priorities, location):
    answer = 0
    out = []
    loc_list = [0]*len(priorities)
    loc_list[location] = 1
    while True :
        if len(priorities) == 1 :
            break
        if priorities[0] == max(priorities) :
            priorities = priorities[1:]
            out.append(loc_list[0])
            loc_list = loc_list[1:]
        else :
            append_pri = priorities[0]
            append_loc = loc_list[0]
            priorities = priorities[1:]
            priorities.append(append_pri)
            loc_list = loc_list[1:]
            loc_list.append(append_loc)
    out.append(loc_list[0])
    answer = out.index(1)+1
    return answer
  
  
from collections import deque

def solution(priorities, location):
    answer = []
    
    # index와 함께 값을 저장 (index는 최종 return 값)
    prior_with_index = deque([])
    for i, priority in enumerate(priorities):
        prior_with_index.append((priority, i))

    while prior_with_index:
        pop_prior, idx = prior_with_index.popleft()
        
        # 남아있지 않다면 마지막 값을 추가하고 break
        if not prior_with_index:
            answer.append(idx)
            break
        
        # 가장 큰 값일 경우 출력, 그렇지 않을 경우 다시 삽입
        max_value = max(prior_with_index)
        
        if pop_prior >= max_value[0]:
            answer.append(idx)
        else:
            prior_with_index.append((pop_prior, idx))
        
    return answer.index(location)+1  
