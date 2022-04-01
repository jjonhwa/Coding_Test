def solution(key, lock):
    answer = True
    # 롹이 키보다 행렬이 큰데 키를 적용가능하지 못한 구역에 0이 있을 경우 false
    if len(lock) > len(key) :
        for r in lock :
            for c in lock[r] :
                if r > len(key) or c > len(key[0]) :
                    if lock[r][c] == 0 :
                        return False
    return answer

lock = [[1,1,1,1], [1,1,0,1], [0,0,0,1], [1,1,1,1]]
key = [[0,0,0], [1,1,1], [0,0,0]]
print(solution(key, lock))
