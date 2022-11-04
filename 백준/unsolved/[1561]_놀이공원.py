"""
    1. 처음 탈 때는 순서대로 진행
    2. 시간을 기준으로 모든 아이들이 놀이기구를 탈 수 있는 시간을 탐색
    3. "time"에 모든 아이들이 탑승할 수 있다면, "time-1"시간에 탈 수 있는 인원을 제외
    4. "time"에 탑승하는 아이들을 순차적으로 돌면서 n이 되었을 때의 index를 출력
"""
import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
rides = list(map(int, input().split()))

# 1. 맨 첫 바퀴는 없앤다.
if n <= m:
    print(n)
# 2. 두 번째 바퀴부터 시작
else:
   
    left, right = 0, n*30
    while left <= right:
        mid = (left + right) // 2

        cnt = m
        for i in range(len(rides)):
            cnt += mid // rides[i]
        
        if cnt >= n:
            time = mid
            right = mid - 1
        elif cnt < n:
            left = mid + 1

        
    before_cnt = 0
    for i in range(len(rides)):
        before_cnt += (time-1) // rides[i]
    
    n = n - m - before_cnt
    for i in range(len(rides)):
        if time % rides[i] == 0:
            n -= 1
            
        if n == 0:
            break
   
    print(i+1)
