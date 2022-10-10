"""
하나의 말 위에 다른 말을 올릴 수 있다.

턴
1. 1번말 ~ k번말 까지 '순서대로' 이동
2. 업은 말도 함께 이동
3. 4개의 말이 쌓일 경우 게임 종료

말 쌓기
1. 흰색
    1-1. 이동: 단순 이동
    1-2. 쌓기: 이동 말을 정지 말 위로 쌓는다.
2. 빨간색
    2-1. 이동: 이동 후 쌓은 순서 Reverse
    2-2. 쌓기: Reverse 된 말을 정지 말 위로 쌓는다.
3. 파란색
    3-1. 이동: 방향 반대로 전환 후 이동 (반대도 파란색일 경우 정지)
4. 외부로 이동 => 파란색과 동일

코딩
1. 1번말부터 k번말까지 이동
2. 겹칠 경우, 다른 플레이어 위로 쌓기
3. player = [x, y, direction, child]
"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

player_graph = [[[] for _ in range(n)] for _ in range(n)]
player_dir = []
for number in range(k):
    info = list(map(lambda x: (int(x) - 1), input().split()))
    player_dir.append(info[2] + 1)

    player_graph[info[0]][info[1]] = [number]


def move(x, y, direction):
    if direction == 1:
        return x, y+1
    elif direction == 2:
        return x, y-1
    elif direction == 3:
        return x-1, y
    else:
        return x+1, y

def opposite_direction(direction):
    if direction == 1:
        return 2
    elif direction == 2:
        return 1
    elif direction == 3:
        return 4
    else:
        return 3

end = False
turn = 0

while True:
    turn += 1

    for i in range(len(player_dir)):
        direction = player_dir[i]
        reverse = True

        # player의 위치 탐색
        for r in range(len(player_graph)):
            for c in range(len(player_graph[0])):
                if i in player_graph[r][c]:
                    x, y = r, c
                    break

        # 다음 좌표 구하기
        # 흰, 빨일 경우
        nx, ny = move(x, y, direction) 

        # 밖일 경우
        if nx<0 or nx >=n or ny<0 or ny>=n: # 밖으로 이동했을 경우
            direction = opposite_direction(direction)
            nx, ny = move(x, y, direction)

            if graph[nx][ny] == 2: # 파란색을 만날 경우
                nx, ny = x, y
                reverse = False
            
        # 파일 경우
        if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 2: 
            direction = opposite_direction(direction)
            nx, ny = move(x, y, direction)

            if nx<0 or nx >=n or ny<0 or ny>=n or graph[nx][ny] == 2: # 밖으로 이동했을 경우
                nx, ny = x, y
                reverse = False

        
        # 다음 좌표로 이동
        player_list = player_graph[x][y] # 기존 위치

        player_index = player_list.index(i) # 본인이 업힌 위치

        player_list = player_list[player_index:] # 본인부터 업은 말까지

        player_graph[x][y] = player_graph[x][y][:player_index] # 기존 위치의 말 정보 갱신

        # 빨간색일 경우
        if graph[nx][ny] == 1 and reverse:
            # Reverse
            player_list.reverse()
        player_graph[nx][ny].extend(player_list) # 다음 좌표에 추가

        # 종료 조건
        if len(player_graph[nx][ny]) >= 4:
            end = True
            break

        player_dir[i] = direction

    if end or turn > 1000:
        break
    
if turn > 1000:
    print(-1)
else:
    print(turn)


