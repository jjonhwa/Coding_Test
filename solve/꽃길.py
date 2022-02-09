import sys
from typing import List
from itertools import combinations

input = sys.stdin.readline

N = int(input())
price = []
for _ in range(N):
    price.append(list(map(int, input().split())))

# 각 칸에 심을 경우의 비용 계산
cost = [[-1] * N for _ in range(N)] # 가장 바깥 테두리는 모두 -1 (심을 수 없으므로)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(1,len(price)-1):
    for j in range(1, len(price)-1):
        if i == 0 or j == 0:
            continue
        
        tmp_cost = price[i][j]
        for k in range(4):
            tmp_cost += price[i+dx[k]][j+dy[k]]

        cost[i][j] = tmp_cost

# 각 cost 칸에서의 최소 합을 구한다.
def overlap(axis: List):
    """
    각 꽃잎들이 겹치는 지 확인
    Args:
        axis: 꽃잎 cost의 좌표
            ex) axis = ([cost,1,2], [cost,3,3], [cost,4,1])
    Return:
        Boolean
    """
    overlap_check = [[0]*N for _ in range(N)]
    check_list = []
    for a in axis:
        check_list.append(a[1:])
        for i in range(4):
            check_list.append([a[1:][0]+dx[i], a[1:][1]+dy[i]])

    for axis in check_list:
        x, y = axis[0], axis[1]
        overlap_check[x][y] += 1
        if overlap_check[x][y] == 2:
            return False
    return True

final = []
for i in range(1, len(cost)-1):
    for j in range(1, len(cost[0])-1):
        # cost값과 좌표를 이중리스트형태로 담는다. [cost, x, y]
        final.append([cost[i][j], i, j])

comb = combinations(final, 3)
ans_list = []
for c in comb:
    if overlap(c):
        ans = 0
        for check in c:
            ans += check[0]
        ans_list.append(ans)
print(min(ans_list))

