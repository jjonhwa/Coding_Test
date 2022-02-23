def solution(m, n, puddles):
    answer = 0
    graph = [[0] * (m+1) for _ in range(n+1)]
    # graph에 puddle 표시: -1
    for puddle in puddles:
        y, x = puddle[0], puddle[1]
        graph[x][y] = -1
    
    graph[1][1] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            # 첫 위치, 웅덩이는 continue
            if (i == 1 and j == 1) or graph[i][j] == -1:
                continue
            # 왼쪽, 위쪽 모두 웅덩이일 경우 continue
            if graph[i-1][j] == -1 and graph[i][j-1] == -1:
                continue
            # 왼쪽만 웅덩이일 경우 위쪽 값 삽입
            elif graph[i-1][j] == -1:
                graph[i][j] = graph[i][j-1]
            # 위쪽만 웅덩이일 경우 왼쪽 값 삽입
            elif graph[i][j-1] == -1:
                graph[i][j] = graph[i-1][j]
            # 위쪽, 왼쪽에 웅덩이가 없을 경우, 둘의 합
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
                
    answer = graph[n][m] % 1000000007
    return answer