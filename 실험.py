'''
https://www.acmicpc.net/problem/22942
0, 1, 2로 visited를 표기할건데,
0은 아무 영역도 아님,
1은 원 내부 표기
2는 원 양끝 표기.
'''

import sys
input = sys.stdin.readline
RANGE= 2000001
N = int(input())
circles = []
visited = [0 for i in range(RANGE)]
for _ in range(N):
    x, r = list(map(int,input().rstrip().split()))
    x = x+1000000 # X좌표 -100만 ~ 100만 인덱스 지원하기위해서.
    circles.append((x,r))

# x좌표 순서대로 정렬
circles.sort(key = lambda x: x[0])
for x,r in circles:
    flag = True # 안되는 경우 for문 벗어나기 위해서
		
		#1. 원을 그리려고 하는데, x좌표에 아무것도 없는 경우
    if visited[x] == 0:
				# 1-1 그리려는 원의 반지름위치에도 아무것도 없어야함.
        if visited[x-r] ==0 and visited[x+r] == 0:
						# 1-2 진짜 없으면, 양 끝에는 2로 표기하고,
						# 원 내부는 1로 표시.
            for xx in range(x-r, x+r+1):
                if xx == x-r or xx == x+r:
                    visited[xx] = 2
                elif visited[xx] == 0:
                    visited[xx] = 1
				# 양 끝점에 무언가 있으면 그릴 수 없음.
        else:
            flag = False
            break

	  #2. 원을 그리려는데 원 내부에 들어왔음.
    elif visited[x] ==1:
        #원 안에 원을 그려야하는데 원을 벗어나면 안됨.
				# 그려야하는 원의 반지름만큼 확인해서 다른 원과 겹치게 되면 안되므로 확인
        visited[x-r], visited[x+r] = 2, 2
        twopoint_count = 0
        for i in range(x-r+1, x+r):
            if visited[i] == 0:
                visited[i] = 1
            elif visited[i] == 2:
                twopoint_count += 1
        if twopoint_count == 1:
            # 그리고 나서는 양 끝을 2로 표기
            flag = False        	
    
		#3. 원을 그리려는데 다른 원의 끝점에 걸렸음. 이경우 더 큰 원만 그릴 수 있음.
    elif visited[x] ==2:
				#3-1 그리려는 원이 아무것도 없는 곳에 그려져야함.
        if visited[x-r] ==0 and visited[x+r] == 0:
            for xx in range(x-r, x+r+1):
                if xx == x-r or xx == x+r:
                    visited[xx] = 2
                elif visited[xx] ==0:
                    visited[xx] = 1
        else:
            flag = False
            break
    if flag == False:
        break
if flag == True:
    print("YES")
else:
    print("NO")