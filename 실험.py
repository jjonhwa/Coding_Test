import sys
input = sys.stdin.readline

N = int(input())
city = []
for i in range(N):
    city.append(list(map(int, input().split())))
visited = [0] * N
res = int(1e9)

def dfs(now, cost, visited):
    global res
    # BackTracking: 계산된 cost가 현재까지의 cost보다 클경우 return
    if cost >= res:
        return
    
    if sum(visited) == N-1:
        if city[now][0]:
            res = min(res, cost+city[now][0])
        return

    for k in range(1, N):
        # if now == k:
        #     continue
        if city[now][k] and not visited[k]:
            visited[k] = 1
            dfs(k, cost+city[now][k], visited)
            visited[k] = 0

res_list = []
for i in range(1, N):
    if city[0][i]:
        visited[i] = 1
        dfs(i, city[0][i], visited)
        visited[i] = 0

print(res)
