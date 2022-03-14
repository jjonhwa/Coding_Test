def solution(n, build_frame):
    def install_condition(y: int, x: int, stick: int) -> bool:
        if stick == 0: # 기둥
            # graph[x-1][y]: 보의 한쪽 끝에 위치하는지
            # graph[x][y] => 겹치게 쌓지 않으므로 pass
            # graph[x][y-1]: 기둥 위에 쌓는지
            # y == 0: 바닥에 쌓는지
            if (x > 0 and graph[x-1][y] == 1) or (y > 0 and graph[x][y-1] == 0) or y == 0:
                return True
            return False
        elif stick == 1: # 보
            # 보의 왼쪽 혹은 오른쪽에 기둥이 있을 경우 True
            if (y > 0 and graph[x][y-1] == 0) or (x < n and y > 0 and graph[x+1][y-1] == 0):
                return True
            # 양쪽 끝에 보가 있을 경우 True
            elif (x > 0 and graph[x-1][y]) == 1 and (x < n and graph[x+1][y] == 1):
                return True
            return False

    def delete_condition(y: int, x:int, stick: int) -> bool:
        if stick == 0: # 기둥일 경우
            if y < n and graph[x][y+1] == 1: # 위에 보가 있을 경우 오른쪽
                # 보가 install_condition을 만족하면 삭제 가능 => False return
                if install_condition(x, y+1, 1):
                    return True
                return False
            elif x > 0 and y < n and graph[x-1][y+1] == 1: # 위에 보가 있을 경우 왼쪽
                if install_condition(x-1, y+1, 1):
                    return True
                return False
            elif y < n and graph[x][y+1] == 0: # 위에 기둥이 있다면
                # 기둥이 install_condition을 만족True 삭제 가능 => False
                if install_condition(x, y+1, 0): 
                    return True
                return False

        elif stick == 1: # 보일 경우
            if x > 0 and graph[x-1][y] == 1:
                if install_condition(x-1, y, 1):
                    return False
                return True
            elif x < n and graph[x+1][y] == 1:
                if install_condition(x+1, y, 1):
                    return False
                return True
            elif y > 0 and graph[x][y-1] == 0:
                if install_condition(x, y-1, 0):
                    return False
                return True
            elif x < n and graph[x+1][y] == 0:
                if install_condition(x+1, y, 0):
                    return False
                return True
        
    answer = []

    graph = []
    for _ in range(n+1):
        one = []
        for _ in range(n+1):
            one.append(2)
        graph.append(one)
    # graph = [[2,2,2,2,2,2], [2,2,2,2,2,2], [2,2,2,2,2,2], [2,2,2,2,2,2], [2,2,2,2,2,2], [2,2,2,2,2,2]]
    # graph = [[2] * (n+1)] * (n+1) # 기둥과 보의 시작 위치를 그린 그래프

    # graph => 2: 없음, 0: 기둥, 1: 보
    for bf in build_frame:
        x, y, option, condition = bf
        
        if condition == 1:
            if install_condition(x,y,option):
                graph[x][y] = option
        elif condition == 0:
            if delete_condition(x,y,option):
                graph[x][y] = 2
    print(graph)
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 2:
                continue
            answer.append([i,j, graph[i][j]])
    return answer

solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]	)