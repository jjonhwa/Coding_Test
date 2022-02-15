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

ans = int(1e9)
for i in range(N):
    visited = [0] * N
    res = int(1e9)
    result_list = []

    start = i
    visited[start] = 1
    dfs(start, 0, visited)

    for result in result_list:
        node, cost = result[0], result[1]
        ans = min(ans, cost + city[node][start])
print(ans)
