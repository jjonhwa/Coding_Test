def solution(n, s, a, b, fares):
    answer = 0
    
    def floid(fares, n):
        
        # 초기값 설정
        inf = 20_000_001
        floid_graph = [[inf] * (n+1) for _ in range(n+1)]
        
        # 대각 행렬 0으로 초기화
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i == j:
                    floid_graph[i][j] = 0
                    break
                          
        # 인접한 노드의 값 삽입
        for fare in fares:
            a, b, distance = fare
            floid_graph[a][b] = distance
            floid_graph[b][a] = distance
        
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    floid_graph[i][j] = min(floid_graph[i][j], floid_graph[i][k] + floid_graph[k][j])
        
        return floid_graph
    
    graph = floid(fares, n)
    arrive_a = graph[s][a]
    arrive_b = graph[s][b]
    answer = arrive_a + arrive_b
    for k in range(1, n+1):
        arrive_k = graph[s][k]
        arrive_a = graph[k][a]
        arrive_b = graph[k][b]
        answer = min(answer, arrive_k + arrive_a + arrive_b)

    return answer