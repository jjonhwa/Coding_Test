def solution(n, results):
    def bfs(array, i):
        visited = [False] * (n+1) # 방문처리
        fb = 0                    # front or back에 있는 사람의 수
        node = array[i][:]        # array의 i번째 node

        # win_array 혹은 lose_array를 돌면서 이긴사람, 진사람의 수를 bfs로 탐색
        while node:
            fb_player = node.pop(0)
            if not visited[fb_player]:          
                fb += 1
                visited[fb_player] = True
                node.extend(array[fb_player])
        return fb
    
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]
    
    # 본인이 이긴 혹은 진 player의 번호를 자신의 index에 list형태로 초기화
    for result in results:
        win_player, lose_player = result
        win[win_player].append(lose_player)
        lose[lose_player].append(win_player)

    # bfs를 돌면서 이긴 혹은 진 player의 수를 count하고 n-1일 경우
    # 확실히 순위를 알 수 있는 사람으로 판단하여 answer += 1
    for i in range(1, n+1):
        win_count = bfs(win, i)
        lose_count = bfs(lose, i)
        if win_count + lose_count == n-1:
            answer += 1
                
    return answer