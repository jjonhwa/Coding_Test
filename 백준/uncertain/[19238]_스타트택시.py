"""
    1. 가장 가까운 위치에 있는 승객을 태운다.
        1-1. 가장 가까운 위치에 있는 승객이 여러명일 경우, 행 작은 승객 -> 열 작은 승객 순으로
    2. 연료
        2-1. 한 칸 이동할 때마다 1씩 소모
        2-2. 목적지에 도착할 경우, 소모한 양의 두 배 충전
    3. 종료 조건
        3-1. 연료가 바닥날 경우 종료
        3-2. 모든 승객을 목적지에 데려다 줬을 경우 종료
        3-3. 승객을 태울 수 없거나, 목적지까지 데려다 줄 수 없는 경우
"""
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m, gas = list(map(int, input().split()))

graph = []
for _ in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

taxi = list(map(int, input().split()))
taxi = [value-1 for value in taxi]

peoples = defaultdict(int)
destinations = defaultdict(int)
for i in range(m):
    people_x, people_y, destination_x, destination_y = list(map(int, input().split()))
    peoples[(people_x-1, people_y-1)] = i+1
    destinations[i+1] = (destination_x-1, destination_y-1)
    

def find_people(start):
    """ 가장 가까이 있는 사람 찾기"""

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start[0], start[1], 0)]) # x좌표, y좌표, 거리
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    people_cand = [k for k, v in peoples.items() if v != -1]
    min_distance = float("inf")
    
    candidate_dest = []
    while queue:
        x, y, distance = queue.popleft()

        if distance > min_distance:
            break
        
        if (x, y) in people_cand:
            candidate_dest.append((x, y, peoples[(x, y)]))
            min_distance = distance
            continue

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, distance + 1))
    
    if candidate_dest:
        if len(candidate_dest) >= 2:
            candidate_dest.sort(key = lambda x: (x[0], x[1]))
        return candidate_dest[0], min_distance
    else:
        return False

def go_destination(start, dest):
    """ 목적지로 이동 """ 

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(start[0], start[1], 0)]) # x좌표, y좌표, 사용한 가스의 양
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    arrive = False
    while queue:
        x, y, used_gas = queue.popleft()

        if (x, y) == dest:
            arrive = True
            break

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, used_gas + 1))
    
    if arrive:
        return used_gas
    else:
        return False

mission_fail = False
for k in range(m):

    # 택시 -> 사람
    f_people = find_people(taxi)

    if f_people:
        people, used_gas = f_people
    else:
        mission_fail = True
        break

    gas -= used_gas
    if gas < 0:
        mission_fail = True
        break

    # 사람 -> 목적지
    people_x, people_y, people_num = people
    used_gas = go_destination([people_x, people_y], destinations[people_num])
    if not used_gas:
        mission_fail = True
        break

    peoples[(people_x, people_y)] = -1

    gas -= used_gas
    if gas < 0:
        mission_fail = True
        break
    else:
        gas += used_gas * 2
    taxi = destinations[people_num]

if not mission_fail:
    print(gas)
else:
    print(-1)