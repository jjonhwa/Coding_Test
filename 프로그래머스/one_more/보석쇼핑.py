from collections import defaultdict

def solution(gems):
    answer = [100_001,0,0]
    unique_count = len(set(gems))
    left, right = 0, 0
    
    earthworm = defaultdict(int)
    earthworm[gems[0]] = 1
    
    while True:
        if len(earthworm) < unique_count: # 보석의 종이 unique개수보다 작을 경우
            if right == len(gems)-1: # right이 최대길이를 넘어갈 경우 종료
                break
            right += 1
            earthworm[gems[right]] += 1
        else: # 보석의 종이 unique 개수일 경우
            if answer[0] > (right - left): # 길이가 더 작다면 최소값 갱신
                answer = [right - left, left, right]

            earthworm[gems[left]] -= 1
            if earthworm[gems[left]] == 0:
                earthworm.pop(gems[left])
            left += 1
  
    return answer[1]+1, answer[2]+1