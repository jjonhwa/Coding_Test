# 현재 처리 중인 job의 종료 시점을 기준으로 이보다 먼저 수행하는 값들을 비교한다.
# (0 - 7), (3 - 8), (4 - 6), (9 - 3)
    # 작업소요시간이 가장 짧은 job을 먼저 수행한다.
    # 만약, 종료 시점보다 먼저 수행하는 값이 없다면, 새로운 값으로 다시 시작


# 황유성
import heapq

def solution(jobs):
    jobs.sort() # 요청시간 - 작업소요시간 순으로 정렬
    # [[0,7], [3,8], [4,6], [9,3]]
    wait_heap = []
    end_times = []  # 종료 시간
    curr_time = 0   # 현재 시간

    i = 0
    # "i가 jobs의 길이보다 작다" 혹은 "wait_heap이 존재한다"일 경우 반복
    while i < len(jobs) or wait_heap:
        if i < len(jobs) and jobs[i][0] > curr_time and len(wait_heap) == 0:
            # i가 jobs의 길이를 넘어가지 않으면서
            # "jobs[i][0]: i번째 일처리의 요청시간"이 현재시간보다 크고
            # wait_heap이 없을 경우
            #     ==> 현재시간을 "i번쨰 일처리의 요청시간"으로 update
            curr_time = jobs[i][0]
        
        while i < len(jobs) and jobs[i][0] <= curr_time:
            heapq.heappush(wait_heap, jobs[i][1])
            i += 1
           
        cost = heapq.heappop(wait_heap)
        curr_time += cost
        end_times.append(curr_time)
    
    answer = 0
    for job, end_time in zip(jobs, end_times):
        answer += end_time - job[0]

    return answer // len(jobs)

# 이시현
from collections import deque
import heapq

def solution(jobs):
    jobs.sort()               # 요청시간 - 작업소요시간 순으로 정렬
    waiting = []              # 현재 처리 중인 job의 종료 시점을 기준으로 이보다 먼저 수행하는 값들을 담는다.
    MAXTIME = 1000 + 500*1000 # 요청시간 1000 + 작업처리시간 500*1000
    dq_jobs = deque(jobs)
    hard_is_working = False
    end_time = 0              # 종료 시간
    time_count = 0            

    for sec in range(0, MAXTIME):
        # 남은 job이 없고, 현재 시간보다 앞서서 시작한 요청도 없으면 종료
        if not dq_jobs and not waiting:
            break

        # 모든 second를 확인한다. => 요청이 종료되면 hard는 멈춘다.
        if sec == end_time:
            hard_is_working = False
        
        if not hard_is_working: # 요청이 종료됬다.
            if waiting: 
                working_time, start = heapq.heappop(waiting)
                end_time += working_time
            else:
                if dq_jobs:
                    start, working_time = dq_jobs.popleft()
                    end_time = start + working_time
            
            time_count += end_time-start
            hard_is_working = True

        else:
            if dq_jobs and dq_jobs[0][0] <= end_time:
                start, working_time = dq_jobs.popleft()
                heapq.heappush(waiting, [working_time, start])

    return time_count // len(jobs)

# 김동영

import heapq

def solution(jobs):
    jobs.sort()
    original_length = len(jobs)

    heap = []
    step = 0
    now = 0
    answer = 0
    while step < original_length:
        count = 0

        ################################
        # 현재 처리 중인 job의 종료 시점을 기준으로 이보다 먼저 수행하는 값들을 비교한다.
        for i in range(len(jobs)):
            if jobs[i][0] > now:
                break
            else:
                heapq.heappush(heap, [jobs[i][1], jobs[i][0]])
                count += 1

        for i in range(count):
            jobs.pop(0)
        ####################################
        
        ########################################
        i = 0
        while jobs and jobs[0][0] <= now:
            start, time = jobs.pop(0)
            heapq.heappush(heap, [time, start])
        ########################################   

        if heap:
            process = heapq.heappop(heap)
            now += process[0]
            answer += now - process[1]
            step += 1
        else:
            now += 1
    
    return answer // original_length