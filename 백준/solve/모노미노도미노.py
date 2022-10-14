"""
    블럭쌓기

    1. 단순하게 쌓아준다.
    2. 한 줄이 가득차면 제거해준다.
    3. 제거되었을 경우, 제거된 칸 위의 블럭을 제거된 칸만큼 아래로 내린다.
    4. 연한 칸에 블록이 있을 경우, 맨 안쪽 행이 사라지고 연한칸의 수만큼씩 밀린다.

"""

import sys
input = sys.stdin.readline

n = int(input())

green_box = [[0 for _ in range(4)] for _ in range(6)]
blue_box = [[0 for _ in range(4)] for _ in range(6)]

def build_up(t, y, box):
    """ 단순히 쌓음 """
    col_absence = False # 블록을 쌓을 열이 비어있음을 의미

    if t == 1 or t == 3:
        if sum([row[y] for row in box]) == 0:
            col_absence = True
    else:
        if sum([row[y] + row[y+1] for row in box]) == 0:
            col_absence = True


    if col_absence: # 아래칸에 이무것도 없을 경우
        if t == 1:
            box[0][y] = 1
        elif t == 2:
            box[0][y] = 1
            box[0][y+1] = 1
        else:
            box[0][y] = 1
            box[1][y] = 1

    else: # 아래칸에 한 칸이라도 차 있을 경우
        for i in range(len(box)-3, -1, -1):
            if t == 1 and box[i][y]:
                box[i+1][y] = 1
                break
            elif t == 3 and box[i][y]:
                box[i+1][y] = 1
                box[i+2][y] = 1
                break
            elif t == 2 and (box[i][y] or box[i][y+1]):
                box[i+1][y] = 1
                box[i+1][y+1] = 1
                break
    return box

def remove_line(box):
    """ 행이 모두 가득 차 있을 경우, 행 제거 """
    removed_count = 0
    removed_line = 0

    for i in range(len(box)):
        if sum(box[i]) == 4:
            box[i] = [0,0,0,0]
            removed_count += 1
            removed_line = i

    # 처음 사라진 line을 기준으로 삼음 (제거할 때)
    removed_line = removed_line - removed_count + 1
            
    return box, removed_line, removed_count

def go_down(box, line, count):
    """ 아래로 count만큼 내림 """
    for i in range(line, len(box)-count):
        box[i] = box[i+count]

    if count == 1:
        box[-1] = [0,0,0,0]
    elif count == 2:
        box[-2] = [0,0,0,0]
        box[-1] = [0,0,0,0]

    return box

def rotate_90(t, x, y):
    """ x,y를 오른쪽으로 90도 회전 + 기준점의 좌표 탐색 """
    axis = []
    if t == 1:
        axis = [(x, y)]
        new_t = 1
    elif t == 2:
        axis = [(x, y), (x, y+1)]
        new_t = 3
    else:
        axis = [(x, y), (x+1, y)]
        new_t = 2

    new_axis = []
    for x, y in axis:
        nx, ny = y, 4-x-1 # (빨간색칸의 개수 - x - 1)
        new_axis.append((nx, ny))

    if new_t == 1:
        return new_t, nx, ny
    elif new_t == 2: # 가로 기준 => x좌표 작은 것
        if new_axis[0][0] < new_axis[1][0]:
            nx, ny = new_axis[0]
        else:
            nx, ny = new_axis[1]
        return new_t, nx, ny
    else: # 세로 기준 => y좌표 큰 것
        if new_axis[0][1] < new_axis[1][1]:
            nx, ny = new_axis[1]
        else:
            nx, ny = new_axis[0]
        return new_t, nx, ny
    

score = 0
for _ in range(n):
    green_t, green_x, green_y = list(map(int, input().split()))
    blue_t, blut_x, blue_y = rotate_90(green_t, green_x, green_y)

    # 1. 단순히 쌓아준다.
    green_box = build_up(green_t, green_y, green_box)
    blue_box = build_up(blue_t, blue_y, blue_box)


    # 2. 한 줄이 가득차면 제거한다.
    green_box, green_removed_line, green_removed_count = remove_line(green_box)
    blue_box, blue_removed_line, blue_removed_count = remove_line(blue_box)

    # 점수
    score += green_removed_count + blue_removed_count

    # 3. 제거되었을 경우, 제거된 칸 위의 블럭을 제거된 칸만큼 아래로 내린다.
    if green_removed_count:
        green_box = go_down(green_box, green_removed_line, green_removed_count)

    if blue_removed_count:
        blue_box = go_down(blue_box, blue_removed_line, blue_removed_count)

    # 4. 연한 칸에 블록이 있을 경우, 맨 안쪽 행이 사라지고 연한칸의 수만큼씩 밀린다.
    if sum(green_box[5]): # 두 칸 삭제
        green_box = go_down(green_box, 0, 2)
    elif sum(green_box[4]): # 한 칸 삭제
        green_box = go_down(green_box, 0, 1)

    if sum(blue_box[5]): # 두 칸 삭제
        blue_box = go_down(blue_box, 0, 2)
    elif sum(blue_box[4]): # 한 칸 삭제
        blue_box = go_down(blue_box, 0, 1)

box_space = sum([sum(row) for row in green_box]) + sum([sum(row) for row in blue_box])

print(score)
print(box_space)