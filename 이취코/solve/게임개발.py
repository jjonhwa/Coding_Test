import sys
input = sys.stdin.readline

# 바라보는 방향
# 반시계 방향으로 90도 회전
# 방문 기록
N, M = list(map(int, input().split()))
x, y, see = list(map(int, input().split()))
mapp = []
for _ in range(N):
    mapp.append(list(map(int, input().split())))

# 북: 0, 동: 1, 남: 2, 서: 3
def reverse_rotate(see):
    if see % 4 == 0:
        return 3
    elif see % 4 == 3:
        return 2
    elif see % 4 == 2:
        return 1
    else:
        return 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * M for _ in range(N)] # 방문 표시
visited[x][y] = True # 초기 시작점 방문
cnt = 1 # 방문한 칸의 수
while True:
    no_go = False
    for _ in range(4):
        see = reverse_rotate(see)
        nx = x + dx[see]
        ny = y + dy[see]
        # map을 벗어나지 않고, 왼쪽방향 회전 후 한칸 전진할 곳이 육지이고, 방문하지 않았다면 이동
        if 0 <= nx < N and 0 <= ny < M and mapp[nx][ny] == 0 and not visited[nx][ny]:   
            x, y = nx, ny
            visited[x][y] = True
            cnt += 1
            no_go = True
            break

    if not no_go: # 네 방향 모두 가본 칸이거나, 바다로 되어있을 경우, 뒤로 한 칸 움직인다.
        back = (see + 2) % 4
        nx = x + dx[back]
        ny = x + dy[back]
        if 0 <= nx < N and 0 <= ny < M and mapp[nx][ny] == 0:
            x, y = nx, ny
            if not visited[x][y]: # 이미 네 방향 모두 가본칸이기 때문에 not visited 조건은 없어도 된다.
                cnt += 1
                visited[x][y] = True
        else:
            break
print(cnt)



