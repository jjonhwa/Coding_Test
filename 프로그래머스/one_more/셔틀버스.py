def solution(n, t, m, timetable):
    answer = ''
    
    def make_minute(time):
        hour, minute = time.split(':')
        minute = int(minute) + int(hour) * 60
        return minute
    
    def make_time(minute):
        hour = str(minute // 60)
        minute = str(minute - 60*int(hour))
        
        if len(hour) == 1:
            hour = '0' + hour
        if len(minute) == 1:
            minute = '0' + minute
        return hour + ':' + minute
    
    time_table = []
    for ti in timetable:
        time_table.append(make_minute(ti))
    time_table.sort(reverse = True)
    
    start_time = make_minute("09:00")
    all_riding = False
    empty_space = n*m
    riding = []
    for i in range(n):
        if i == 0:
            pass
        else:
            start_time += t
            
        for _ in range(m):
            if not time_table:
                all_riding = True
                break
            if time_table[-1] <= start_time:
                last = time_table.pop()
                riding.append(last)
                empty_space -= 1
                continue
            if i != n-1:
                empty_space -= 1

            
    # all_riding => 다 탔는데도 자리가 남았다.
    # riding => 탄사람이 있나 없나
    # empty_space => 몇명은 타고 몇명을 못탈 때, 자리가 남아있는지 
    if all_riding or not riding or empty_space: 
        answer = start_time
    else:
        answer = last-1
    
    answer = make_time(answer)
    return answer