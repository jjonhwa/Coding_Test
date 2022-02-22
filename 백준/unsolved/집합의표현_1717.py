# n = 1,000,000 / m = 100,000
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = list(map(int, input().split()))
parent = [i for i in range(n+1)]
def find(x):
    '''부모 node를 찾는 함수'''
    if parent[x] == x: # x의 부모가 자기 자신일 경우 그대로 반환
        return x
    parent[x] = find(parent[x]) # x의 부모가 다른 값일 경우 재귀 형태로 찾아준다.
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    cal, a, b = list(map(int, input().split()))
    parent_a = find(a)
    parent_b = find(b)

    if cal == 0:
        union(a, b)
    else:
        if parent_a == parent_b:
            print('YES')
        else:
            print('NO')
