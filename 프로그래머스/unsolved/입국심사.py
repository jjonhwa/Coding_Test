def solution(n, times):
    answer = 0
    # times가 정렬된 상태로 들어온다는 보장이 없으므로 정렬
		# 최소 시간을 left, 최대 시간을 right로 정의
		# left와 right의 중간값을 mid로 정의
		# mid 시간 내에 처리할 수 있는 사람의 수
		# times를 돌면서 "처리할 수 있는 사람의 수"가 n보다 큰지, 작은지 판별
		# n보다 클경우, 이미 너무 큰 시간을 할당한 것이므로 break 후 시간을 줄인다.
		# n보다 크다면, mid를 줄이기 위해여 right를 update
		# mid가 update될 때마다 answer에 삽입되는 경우는 모두 최소
		# n보다 작다면, mid를 높이기 위하여 left를 update


    times.sort()                      # times가 정렬된 상태로 들어온다는 보장이 없으므로 정렬
    
    left, right = 1, times[-1] * n    # 최소 시간을 left, 최대 시간을 right로 정의
    while left <= right:
        mid = (left + right) // 2     # left와 right의 중간값을 mid로 정의
        
        people = 0                    # mid 시간 내에 처리할 수 있는 사람의 수
        for time in times:            # times를 돌면서 "처리할 수 있는 사람의 수"가 n보다 큰지, 작은지 판별
            people += mid // time     # 30 -> 4 / 30 -> 3 ==> 7
            
            if people >= n:           # n보다 클경우, 이미 너무 큰 시간을 할당한 것이므로 break 후 시간을 줄인다.
                break
                
        if people >= n:               # n보다 크다면, mid를 줄이기 위해여 right를 update
            right = mid - 1
            answer = mid              # mid가 update될 때마다 answer에 삽입되는 경우는 모두 최소
        else:                         # n보다 작다면, mid를 높이기 위하여 left를 update
            left = mid + 1
    return answer

