import sys
input = sys.stdin.readline

N = int(input())
city = []
for i in range(N):
    city.append(list(map(int, input().split())))

def dfs(now, cost, visited):
    global res
    global result_list
    # BackTracking: 계산된 cost가 현재까지의 cost보다 클경우 return
    if cost >= res:
        return
    
    if sum(visited) == N:
        res = min(res, cost)
        result_list.append((now,res))
        return 

    for k in range(N):
        if now == k:
            continue
        if city[now][k] and not visited[k]:
            visited[k] = 1
            dfs(k, cost+city[now][k], visited)
            visited[k] = 0

#### 10%에서 계속 틀리길래, 시작점을 전부 돌면서 실행한 후 그 중 최소값을 출력 ####
# 이랬더니 40%에서 계속 틀렸습니다
ans = int(1e9)
for i in range(N):
		# 시작점부터 순회하면서 시작점 전까지
    visited = [0] * N
    res = int(1e9)
    result_list = []

    start = i
    visited[start] = 1
    dfs(start, 0, visited)

		# 마지막 node에서 시작점으로 이동
    for result in result_list:
        node, cost = result[0], result[1]
        if city[node][start] != 0:
            ans = min(ans, cost + city[node][start])
print(ans)