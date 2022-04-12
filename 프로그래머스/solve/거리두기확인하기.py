#  full   /   outer   / inner
#    #         #        
#   ###       # #         #
#  ## ##     #   #       # #  
#   ###       # #         #
#    #         #

# 1. full에 또 다른 P가 존재하는지 확인
# 2. P가 존재한다면 모든 P에 대하여 탐색
    # 2-1. 또 다른 P가 outer에 있다면 또 다른 P까지의 inner가 전부 X 인지 체크
    # 2-2. P가 inner에 존재한다면 return 0

from typing import List

def full_check(graph, x, y) -> List[tuple]:
    """
    full 모양 내에 또 다른 P가 있는지 확인
    Args:
        graph: 앉아 있는 형태에 대한 그래프
        x, y: 현재 앉아있는 사람의 좌표 (P)
    
    Return:
        List[(x1,y1), (x2,y2), ...]
    """
    
    another_p = []
    
    # 가로, 세로 체크
    for i in [-2, -1, 1, 1]:
        # 세로 체크
        if graph[x][y+i] == 'P':
            another_p.append((x,y+i))
        
        # 가로 체크
        if graph[x+i][y] == 'P':
            another_p.append((x+i, y))
        
    # 대각선 체크
    for i in [-1, 1]:
        if graph[x+i][y+i] == 'P':
            another_p.append((x+i, y+i))
        if graph[x+i][y-i] == 'P':
            another_p.append((x+i, y-i))
        
    return another_p

def keep_distance(graph, x,y, another_x, another_y) -> bool:
    """
    거리두기가 잘 치켜지고 있는지 확인하는 함수
    서로 다른 P가 같은 y 혹은 x를 가질 경우 (일직선 상에 또다른 P가 있을 경우)
        => 거리가 1이면, 거리두기가 잘 지켜지지 않음.
        => 거리가 2이면, 그 사이에 파티션이 있는지 없는지 여부로 판단
    서로 다른 P가 대각선에 위치할 경우
        => 대각선으로 가는 길에 전부 파티션이 있는지 없는지 여부로 판단
    """
    # 서로 다른 P가 같은 y를 가질 경우
    if y == another_y:
        if abs(x - another_x) == 1:
            return False
        else:
            median = (x + another_x) // 2
            if graph[median][y] == 'X':
                return True
            else:
                return False

    # 서로 다른 P가 같은 x를 가질 경우
    elif x == another_x:
        if abs(y - another_y) == 1:
            return False
        else:
            median = (y + another_y) // 2
            if graph[x][median] == 'X':
                return True
            else:
                return False

    # 서로 다른 P가 대각선에 위치할 경우
    else:
        if another_x - x == 1 and another_y - y == 1:
            if graph[x+1][y] == 'X' and graph[x][y+1] == 'X':
                return True
            else:
                return False
        if another_x - x == 1 and another_y - y == -1:
            if graph[x+1][y] == 'X' and graph[x][y-1] == 'X':
                return True
            else:
                return False
        if another_x - x == -1 and another_y - y == 1:
            if graph[x-1][y] == 'X' and graph[x][y+1] == 'X':
                return True
            else:
                return False
        if another_x - x == -1 and another_y - y == -1:
            if graph[x-1][y] == 'X' and graph[x][y-1] == 'X':
                return True
            else:
                return False
    
def solution(places):
    answer = []
    
    # 2칸을 상, 하, 좌, 우로 더 추가해준다. X로 채운다.
    new_places = []
    for place in places:
        new_place = []
        new_place.append('XXXXXXXXX')
        new_place.append('XXXXXXXXX')
        for p in place:
            new_place.append("XX"+p+"XX")
        new_place.append('XXXXXXXXX')
        new_place.append('XXXXXXXXX')
    
        new_places.append(new_place)
    
    for new_place in new_places:
        final = True # 한 번이라도 False가 나온다면 0 리턴 / 계속해서 True를 유지할 경우 1 리턴
        
        for i in range(2,7):
            for j in range(2,7):
                if new_place[i][j] == 'P':
                    another_p = full_check(new_place, i, j)

                    check = True
                    for another_x, another_y in another_p:
                        if not keep_distance(new_place, i, j, another_x, another_y):
                            check = False
                            final = False
                            break

                    if not check:
                        answer.append(0)
                        break
            if not final:
                break
        if final:
            answer.append(1)

    return answer
