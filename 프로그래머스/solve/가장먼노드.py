from collections import deque

def solution(n, edge):
    max_dist = 0
    cnt = 0
    
    graph = [[] for _ in range(n+1)]
    for ed in edge:
        a, b = ed
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (n+1)
    
    queue = deque()
    visited[1] = True     # 첫 node 방문 처리
    queue.append((1,0))   # (첫번째 node 번호, 첫번째 node까지의 거리 0)
    while len(queue):
        node, distance = queue.popleft()
        if distance > max_dist:     # 갱신된 거리가 최대값보다 클경우
            max_dist = distance     # max_dist를 최대 거리로 갱신
            cnt = 1                 # max_dist를 갱신함과 동시에 count + 1
        elif distance == max_dist:  # max_dist와 같다면
            cnt += 1                # 우리가 찾고자하는 가장 멀리 떨어진 노드라고 판단되어 count + 1
            
        for n in graph[node]:       # 다음 node 탐색
            if not visited[n]:      # 방문처리가 되어있지 않은 node에 대해서만 queue에 추가
                visited[n] = True   # 방문 처리
                queue.append((n, distance+1))   # (node번호, 1번노드에서 현재 node까지의 거리)
    
    return cnt
