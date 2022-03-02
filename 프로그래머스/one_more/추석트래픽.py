def check_date(time):
    # day
    if int(str(time)[-9:]) >= 240000000:
        time = str(time)[:-9] + '23' + str(time)[-7:]
        time = int(time)

    # hour
    if int(str(time)[-7:]) >= 6000000:
        time = str(time)[:-7] + '59' + str(time)[-5:]
        time = int(time)

    # minute
    if int(str(time)[-5:]) >= 60000:
        time = str(time)[:-5] + '5' + str(time)[-4:]
        time = int(time)
    return time

def solution(lines):
    answer = 0

    points = []
    for line in lines:
        date, time, t = line.split()[0], line.split()[1], line.split()[2]
        mili_second = time.split('.')[1]
        
        date_int = int(date.split('-')[0])*10000000000 + int(date.split('-')[1]) * 100000000  + int(date.split('-')[2]) * 1000000 
        time_int = int(time.split(':')[0]) * 10000000 + int(time.split(':')[1]) * 100000 + int(time.split(':')[2].split('.')[0]) * 1000 + int(mili_second)
        date_int = date_int * 1000
        
        end = date_int + time_int
        start = check_date(end - int(float(t[:-1]) * 1000))
        
        points.append((start+1, end))
        
    points.sort(key = lambda x: x[1]) # 끝점기준 정렬
    max_count = 0
    for i, point in enumerate(points):
        _, check_start = point
        check_end = check_date(check_start + 999)
        count = 0
        for p in points[i:]:
            start, end = p

            if check_end >= start and check_end <= end: # 큼
                count += 1
            elif check_start >= start and check_start <= end: # 작음
                count += 1
            elif check_start >= start and check_end <= end: # 포함함
                count += 1
            elif check_start <= start and check_end >= end: # 포함됨
                count += 1
        
        max_count = max(count, max_count)
    return max_count