import sys
input = sys.stdin.readline

V, E = list(map(int, input().split()))
# 초기 node의 root는 자기자신으로 생성
vroot = [i for i in range(V+1)] # [0, 1, 2, 3, ...]
elist = [] # 2개의 node와 weight를 list형태로 삽입

for _ in range(E):
    elist.append(list(map(int, input().split()))) # [[1,2,1], [2,3,2], [1,3,3]]
elist.sort(key = lambda x: x[2]) # 간선 기준 정렬
# [[1,2,1], [2,3,2], [1,3,3]]

def find(x):
    """Root 찾기"""
    if x != vroot[x]:
        vroot[x] = find(vroot[x])
    return vroot[x]

answer = 0
for s, e, w in elist:
    sroot = find(s) # 1 -> 1
    eroot = find(e) # 2 -> 2

    if sroot != eroot:
        if sroot > eroot:
            vroot[sroot] = eroot
        else:
            vroot[eroot] = sroot
        answer += w

# for loop 첫번쨰
# s = 1, e = 2 --> sroot = 1, eroot = 2
# if문 => sroot와 eroot가 서로 다르므로,
# if 속 if문 => 작은 값을 기준으로 root 생성
# 즉, vroot[2] = 1 --> 2의 root node를 1로 변경
# answer에 weight 추가

# for loop 두번째
# s = 2, e = 3 --> sroot = 1, eroot = 3
# if문 => sroot와 eroot가 서로 다르므로,
# if 속 if문 => 작은 값을 기준으로 root 새엇
# 즉, vroot[3] = 1 --> 3의 root node를 1로 변경
# answer에 weight 추가

# for loop 세번쨰
# s = 1, e = 3 --> sroot = 1, eroot = 1
# if문 => sroot와 eroot가 같으므로 if문 생략