import sys
input = sys.stdin.readline

N = int(input())

ans = 0
row = [0] * N # N=4: row = [0,0,0,0]

def is_promising(x):
    """x가 유망한지 판단"""
    for i in range(x): # 퀸을 위에서 부터 놓는다 => x이전까지만 i를 탐색
        # 행이 같은 경우는 있을 수 없다. => i는 x보다 작으므로
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            # 열 체크: x의 열, i의 열을 비교했을 때 같은 열에 놓여져 있는지: row[x] == row[i]
            # 대각선 체크: 열의 차이와, 행의 차이의 절대값이 같은지: abs(row[x] - row[i]) == abs(x-i)
            return False
    return True

def dfs(x):
    global ans

    if x == N: # 마지막 행까지 전부 유망할 경우 1추가
        ans += 1
    else:
        # 각 행, 열에 놓는다.
        for i in range(N): # x행 1열부터 ~ x행 N열까지
            row[x] = i # x행 i열
            if is_promising(x):
                dfs(x+1) # x+1행 삽입

dfs(0)
print(ans)