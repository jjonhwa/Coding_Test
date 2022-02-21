import numpy as np

def solution(board, skill):
    answer = 0
    board = np.array(board)
    
    # 누적합을 계산하기 위한 틀 생성
    N, M = len(board), len(board[0])
    calculate_skill = [[0]*(M+1) for _ in range(N+1)]
    for sk in skill:
        _type, r1, c1, r2, c2, degree = sk
        if _type == 1: degree *= -1
        
        calculate_skill[r1][c1] += degree
        calculate_skill[r1][c2+1] -= degree
        calculate_skill[r2+1][c1] -= degree
        calculate_skill[r2+1][c2+1] += degree
    
    # 누적합 계산
    prefix_sum = [[0]*(M+1) for _ in range(N+1)]
    # 오른쪽으로 휩쓴다.
    for i in range(len(calculate_skill)):
        prefix = 0
        for j in range(len(calculate_skill[i])):
            prefix += calculate_skill[i][j]
            prefix_sum[i][j] = prefix

    # 아래쪽으로 휩쓴다.
    for j in range(len(prefix_sum[0])):
        prefix = 0
        for i in range(len(prefix_sum)):
            prefix += prefix_sum[i][j]
            # print(prefix)
            if i == 0:
                continue
            prefix_sum[i][j] = prefix

    prefix_sum = np.array(prefix_sum)
    prefix_sum = prefix_sum[:-1, :-1]
    
    # Broadcasting을 활용한 board 계산
    board += prefix_sum
    
    for br in board:
        for b in br:
            if b > 0:
                answer += 1
    
    return answer