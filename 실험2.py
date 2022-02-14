import sys
input = sys.stdin.readline

N = int(input())
circle = []
for _ in range(N):
    circle.append(list(map(int, input().split())))

# 원의 시작점 혹은 끝점의 좌표 / start 혹은 end / 몇번째 원인지
# 이 세가지를 이중리스트 형태로 담아준다.
start_end_list = []
for i, c in enumerate(circle):
    d, r = c[0], c[1]
    start = [d-r, 's', i]
    end = [d+r, 'e', i]
    start_end_list.append(start)
    start_end_list.append(end)
# start_end_list = [[2,'s',1], [4,'e',1], [3,'s',2], [5,'e',2], ...] => 첫번째 예제

start_end_list.sort(key = lambda x: x[0]) # 시작 및 끝점의 좌표 기준으로 정렬
# start_end_list = [[1,'s',4], [2,'s',1], [3,'s',2], ...] => 첫번째 예제

# 연속되는 두 개의 점을 비교한다.
# 이 때, start와 end가 교차되면서, 서로 다른 원일 경우에 '겹친다'
print(start_end_list)
condition = False
for first, second in zip(start_end_list, start_end_list[1:]):
    if first[1] == 's' and second[1] == 'e' and first[2] != second[2]:
        condition = True
        break
    if (first[1] == 's' and second[1] == 's') or (first[1] == 'e' and second[1] == 'e'):
        if first[0] == second[0]:
            condition = True
            break

if condition:
    print('NO')
else:
    print('YES')