def dfs(node, computers, visited):
    for i, computer in enumerate(computers[node]):
        if i == node:                           # 내 자신을 방문할 경우 방문 처리 후 continue
            visited[i] = True
            continue
        if computer == 1 and not visited[i]:    # 연결되어있으면서 방문하지 않았을 경우
            visited[i] = True                   # 방문 처리 후
            dfs(i, computers, visited)          # dfs로 타고 들어간다.
    return visited

def solution(n, computers):
    answer = 0
    origin_visited = [False] * n
    for i in range(n):
        visited = origin_visited.copy()
        visited = dfs(i, computers, visited)
        if visited != origin_visited:           # 방문 처리가 바뀌지 않을 경우
            answer += 1                         # answer += 1
        origin_visited = visited
    return answer