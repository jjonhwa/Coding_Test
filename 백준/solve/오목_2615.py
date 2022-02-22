import sys
input = sys.stdin.readline

# 바둑판 생성
go_base = []
for _ in range(19):
    go_base.append(list(map(int, input().split())))

def solution():
    for i in range(len(go_base)):
        for j in range(len(go_base[i])):
            candidate = go_base[i][j]
            if candidate == 0: # 바둑알이 없을 경우, 다음 진행
                continue
            
            right = 1
            under = 1
            diogonal_right = 1
            diogonal_left = 1
            # 아래쪽 체크
            while True:
                if i+under < 19 and go_base[i+under][j] == candidate:
                    under += 1
                else:
                    break

                if under == 5:
                    if i-1 >=0 and go_base[i-1][j] == candidate: # 그 전칸이 같은 경우일 경우 6목이 되므로 break
                        break
                    if i+under >= 19: # 5개가 채워진 상태로 바둑판을 벗어날 경우
                        winner = candidate
                        winner_space = [i, j]
                        return winner, winner_space
                    elif i+under < 19 and go_base[i+under][j] != candidate: # 바둑판 내에 있으면서 다음칸이 없어나 다른 색 바둑알일 경우
                        winner = candidate
                        winner_space = [i, j]
                        return winner, winner_space
                    else:
                        break

            # 오른쪽 체크
            while True:
                if j+right < 19 and go_base[i][j+right] == candidate:
                    right += 1
                else:
                    break

                if right == 5:
                    if j-1 >=0 and go_base[i][j-1] == candidate: # 그 전칸이 같은 경우일 경우 6목이 되므로 break
                        break
                    if j+right >= 19:
                        winner = candidate
                        winner_space = [i, j]
                        return winner, winner_space
                    elif j+right < 19 and go_base[i][j+right] != candidate:
                        winner = candidate
                        winner_space = [i, j]
                        return winner, winner_space
                    else:
                        break

            # 대각선 체크 1
            while True:
                if i+diogonal_right < 19 and j+diogonal_right < 19 and go_base[i+diogonal_right][j+diogonal_right] == candidate:
                    diogonal_right += 1
                else:
                    break

                if diogonal_right == 5:
                    if i-1 >=0 and j-1 >=0 and go_base[i-1][j-1] == candidate: # 그 전칸이 같은 경우일 경우 6목이 되므로 break
                        break
                    if i+diogonal_right >= 19 or j+diogonal_right >= 19:
                        winner = candidate
                        winner_space = [i, j]
                        return winner, winner_space
                    elif j+diogonal_right < 19 and i+diogonal_right < 19 and go_base[i+diogonal_right][j+diogonal_right] != candidate:
                        winner = candidate
                        winner_space = [i, j]
                        return winner, winner_space
                    else:
                        break
            
            # 대각선 체크 2
            while True:  
                if i+diogonal_left < 19 and j-diogonal_left >= 0 and go_base[i+diogonal_left][j-diogonal_left] == candidate:
                    diogonal_left += 1
                else:
                    break

                if diogonal_left == 5:
                    if i-1 >=0 and j+1 < 19 and go_base[i-1][j+1] == candidate: # 그 전칸이 같은 경우일 경우 6목이 되므로 break
                        break
                    if i+diogonal_left >= 19 or j-diogonal_left < 0:
                        winner = candidate
                        winner_space = [i+diogonal_left-1, j-diogonal_left+1]
                        return winner, winner_space
                    elif i+diogonal_left < 19 and j-diogonal_left >= 0 and go_base[i+diogonal_left][j-diogonal_left] != candidate:
                        winner = candidate
                        winner_space = [i+diogonal_left-1, j-diogonal_left+1]
                        return winner, winner_space
                    else:
                        break
    return 0, 0
winner, winner_space = solution()
print(winner_space)
if winner == 0:
    print(winner)
else:
    print(winner)
    for w in winner_space:
        print(w+1, end=' ')
