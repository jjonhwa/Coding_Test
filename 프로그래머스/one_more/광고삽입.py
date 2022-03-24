def solution(play_time, adv_time, logs):
    answer = ''
    # 모든 시간을 초로 변경
    hour, minute, second = play_time.split(':')
    play_time = int(hour) * 3600 + int(minute) * 60 + int(second)
    
    hour, minute, second = adv_time.split(':')
    adv_time = int(hour) * 3600 + int(minute) * 60 + int(second)
    
    # [(start 시간, 0), (end 시간, 1), ..] 
    # 시작 표시를 0, 끝 표시를 1로 tuple 형태로 묶어 새로운 리스트에 추가
    sec_logs = []
    for log in logs:
        start, end = log.split('-')
        
        hour, minute, second = start.split(':')
        start_time = int(hour) * 3600 + int(minute) * 60 + int(second)
        sec_logs.append((start_time, 0))
        
        hour, minute, second = end.split(':')
        end_time = int(hour) * 3600 + int(minute) * 60 + int(second)
        sec_logs.append((end_time, 1))
        
    # logs를 시간 순으로 정렬
    sec_logs.sort(key = lambda x: x[0], reverse = True)

    # 시작과 끝을 확인하면서 모든 playtime에 대하여 누적 재생 수 count
    prefix_count = []
    cnt = 0

    # sec_logs를 reverse형태로 가져옴으로서 뒤에서 부터 하나씩 빼주며
    # sec_logs의 마지막 값을 기준으로 비교한다.
    for i in range(play_time+1):
        if not sec_logs:                                       # 더 이상 log가 없을 경우 0추가
            prefix_count.append(0)
            continue
        
        while sec_logs and i == sec_logs[-1][0]:
            if sec_logs[-1][1] == 0:
                cnt += 1
                sec_logs.pop()
            elif sec_logs[-1][1] == 1:
                cnt -= 1
                sec_logs.pop()

        # if i == sec_logs[-1][0] and sec_logs[-1][1] == 0:      # 가장 작은 값과 맞닥뜨렸을 때
        #     cnt += 1                                           # start일 경우 cnt += 1
        #     sec_logs.pop()
        # elif i == sec_logs[-1][0] and sec_logs[-1][1] == 1:    # 가장 작은 값과 맞닥뜨렸을 때
        #     cnt -= 1                                           # end일 경우 cnt -= 1
        #     sec_logs.pop()
        prefix_count.append(cnt)                     
        # [0,0,0,0,0,1,1,1,1,1,2,2,2,2,1,1,1,0,0,0,0 ...]
    
    # 각 구간의 누적합이 가장 큰 start를 기록
    start = 0
    end = start + adv_time
    now_summation = 0
    for i in range(end):
        now_summation += prefix_count[i]    # 0부터 adv_time동안의 구간합을 
    max_summation = now_summation

    start_time = 0
    for i in range(1, play_time-adv_time+1):
        start = i
        end = start + adv_time 
        now_summation = now_summation - prefix_count[start-1] + prefix_count[end-1]
        if now_summation > max_summation:
            max_summation = now_summation
            start_time = i

    # second를 시, 분, 초로 변경
    hour = start_time // 3600
    minute = (start_time - hour*3600) // 60
    second = start_time - hour*3600 - minute*60
    hour, minute, second = str(hour), str(minute), str(second)
    
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    if len(second) == 1:
        second = '0' + second
    
    answer = hour + ':' + minute + ':' + second
    return answer