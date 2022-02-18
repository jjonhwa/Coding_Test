import sys
input = sys.stdin.readline

N = int(input())
confetti = []
for _ in range(N):
    confetti.append(list(map(int, input().split())))

def check(confetti):
    # 이중 list -> 단일 list
    two_to_one = sum(confetti, [])
    
    # 0과 1이 들어있으면 'OUT'
    # 0만 들어있으면 'WHITE'
    # 1만 들어있으면 'BLUE'
    ch = list(set(two_to_one))
    if len(ch) == 2:
        return 'OUT'
    elif len(ch) == 1 and ch[0] == 1:
        return 'BLUE'
    elif len(ch) == 1 and ch[0] == 0:
        return 'WHITE'

blue = 0
white = 0
out = 0
def dfs(confetti):
    global blue
    global white

    if check(confetti) == 'BLUE':
        blue += 1
        return
    elif check(confetti) == 'WHITE':
        white += 1
        return

    row = len(confetti)
    
    first_confetti = []
    second_confetti = []
    third_confetti = []
    forth_confetti = []

    half = int(row/2)
    for i in range(half):
        first_confetti.append(confetti[i][:half])
        second_confetti.append(confetti[i][half:])
    for i in range(half, row):
        third_confetti.append(confetti[i][:half])
        forth_confetti.append(confetti[i][half:])
    
    dfs(first_confetti)
    dfs(second_confetti)
    dfs(third_confetti)
    dfs(forth_confetti)

dfs(confetti)
print(white)
print(blue)
