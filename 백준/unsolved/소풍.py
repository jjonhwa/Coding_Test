"""
    1. 1번부터 순차적으로 "친구 후보군"으로 등록
    2. 시작 "친구 후보군" (맨 처음 - 1번) 이후부터 "친구의 친구"인지 탐색
    3. "친구의 친구"라면, "친구 후보군"으로 추가 등록
    4. "친구 후보군"이 "k명"이라면 종료 

    Time Complexity: O(N x N^2*K)
"""

import sys
input = sys.stdin.readline

k, n, f = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(f):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
graph = [set(g) for g in graph]

def find_friend(current, candidate):
    global answer

    # 이미 answer가 생성됬다면, 다음으로 진행하지 않음
    if answer:
        return

    # 종료 조건 => 순차적으로 방문하므로 처음으로 k명이 됬다면 바로 종료 
    ## ""find_friend""만 종료되므로, answer 유무로 종료하는 조건이 추가되어야 한다.
    if len(candidate) == k:
        answer = sorted(candidate) # 정렬된 list로 반환
        return 

    # current 1 => 2번 ~ n+1번까지 순회
    for next_friend in range(current+1, n+1):

        # 다음 번호부터 순회하면서, "친구 후보군"에 없을 경우에만, 후보군 탐색
        if next_friend not in candidate:

            # "친구 후보군"들이 "다음 친구의 친구"인지 확인
            friend_of_friend = True
            for cand in candidate:
                if cand not in graph[next_friend]:
                    friend_of_friend = False
                    break
            
            # "친구 후보군"들이 "다음 친구의 친구"가 맞다면 => "다음 친구를 탐색"
            if friend_of_friend:

                # append로 주면, candidate이 변해버리기 때문에 input 값에 "+[값]" 혹은 " | (값)" 으로 넣어줘야 한다.
                find_friend(next_friend, candidate | set([next_friend])) 

answer= []
for i in range(1, n+1):

    candidate = set([i])
    find_friend(i, candidate)

    # 정답이 한 번이라도 나왔다면 종료
    if answer:
        break

if not answer:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])




"""
    1. 1번부터 순차적으로 "친구 후보군"으로 등록
    2. 시작 "친구 후보군" (맨 처음 - 1번) 이후부터 "친구의 친구"인지 탐색
    3. "친구의 친구"라면, "친구 후보군"으로 추가 등록
    4. "친구 후보군"이 "k명"이라면 종료 

    Time Complexity: O(N x N^2*K)
"""

import sys
input = sys.stdin.readline

k, n, f = list(map(int, input().split()))

graph = [[] for _ in range(n+1)]
for _ in range(f):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)
graph = [set(g) for g in graph]

def find_friend(current, candidate):
    global answer

    # 이미 answer가 생성됬다면, 다음으로 진행하지 않음
    if answer:
        return

    # 종료 조건 => 순차적으로 방문하므로 처음으로 k명이 됬다면 바로 종료 
    ## ""find_friend""만 종료되므로, answer 유무로 종료하는 조건이 추가되어야 한다.
    if len(candidate) == k:
        answer = sorted(candidate) # 정렬된 list로 반환
        return 

    # current 1 => 2번 ~ n+1번까지 순회
    for next_friend in range(current+1, n+1):

        # 다음 번호부터 순회하면서, "친구 후보군"에 없을 경우에만, 후보군 탐색
        if not visited[next_friend]:

            # "친구 후보군"들이 "다음 친구의 친구"인지 확인
            friend_of_friend = True
            for cand in candidate:
                if cand not in graph[next_friend]:
                    friend_of_friend = False
                    break
            
            # "친구 후보군"들이 "다음 친구의 친구"가 맞다면 => "다음 친구를 탐색"
            if friend_of_friend:
                visited[next_friend] = True

                # append로 주면, candidate이 변해버리기 때문에 input 값에 "+[값]"으로 넣어줘야 한다.
                find_friend(next_friend, candidate | set([next_friend])) 

answer= []
for i in range(1, n+1):

    visited = [False for _ in range(n+1)]
    visited[i] = True

    candidate = set([i])
    find_friend(i, candidate)

    # 정답이 한 번이라도 나왔다면 종료
    if answer:
        break

if not answer:
    print(-1)
else:
    for i in range(len(answer)):
        print(answer[i])
