"""
    문제:
    때는 2020년, 백준이는 월드나라의 한 국민이다. 월드나라에는 N개의 지점이 있고 N개의 지점 사이에는 M개의 도로와 W개의 웜홀이 있다. 
    (단 도로는 방향이 없으며 웜홀은 방향이 있다.) 
    웜홀은 시작 위치에서 도착 위치로 가는 하나의 경로인데, 특이하게도 도착을 하게 되면 시작을 하였을 때보다 시간이 뒤로 가게 된다. 
    웜홀 내에서는 시계가 거꾸로 간다고 생각하여도 좋다.

    시간 여행을 매우 좋아하는 백준이는 한 가지 궁금증에 빠졌다. 
    한 지점에서 출발을 하여서 시간여행을 하기 시작하여 다시 출발을 하였던 위치로 돌아왔을 때, 
    출발을 하였을 때보다 시간이 되돌아가 있는 경우가 있는지 없는지 궁금해졌다. 
    여러분은 백준이를 도와 이런 일이 가능한지 불가능한지 구하는 프로그램을 작성하여라.

    입력:
    첫 번째 줄에는 테스트케이스의 개수 TC(1 ≤ TC ≤ 5)가 주어진다.
    그리고 두 번째 줄부터 TC개의 테스트케이스가 차례로 주어지는데 
    각 테스트케이스의 첫 번째 줄에는 지점의 수 N(1 ≤ N ≤ 500), 도로의 개수 M(1 ≤ M ≤ 2500), 웜홀의 개수 W(1 ≤ W ≤ 200)이 주어진다. 
    그리고 두 번째 줄부터 M+1번째 줄에 도로의 정보가 주어지는데 각 도로의 정보는 S, E, T 세 정수로 주어진다. 
    S와 E는 연결된 지점의 번호, T는 이 도로를 통해 이동하는데 걸리는 시간을 의미한다. 
    그리고 M+2번째 줄부터 M+W+1번째 줄까지 웜홀의 정보가 S, E, T 세 정수로 주어지는데 S는 시작 지점, E는 도착 지점, T는 줄어드는 시간을 의미한다. 
    T는 10,000보다 작거나 같은 자연수 또는 0이다.

    두 지점을 연결하는 도로가 한 개보다 많을 수도 있다. 지점의 번호는 1부터 N까지 자연수로 중복 없이 매겨져 있다.

    출력:
    TC개의 줄에 걸쳐서 만약에 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES, 불가능하면 NO를 출력한다.

    NOTE: 아래의 예제는, Test Case가 1개라고 가정했을 떄의 코드이다.
"""

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m, w = list(map(int, input().split()))

    edge = []
    for _ in range(m):
        a, b, weight = list(map(int, input().split()))
        edge.append((a, b, weight))
        edge.append((b, a, weight))

    for _ in range(w):
        a, b, weight = list(map(int, input().split()))
        edge.append((a, b, -weight))

    ## (기존 방식 - 시작 지점을 고정하므로, 모든 값을 무한대로 초기화)
    # INF = int(1e9)
    # dist = [INF for _ in range(n+1)]

    ## (응용 - 단순 싸이클의 존재 유무만 확인하면 되므로 랜덤값으로 초기화해도 무방)
    dist = [0 for _ in range(n+1)]


    negative_cycle = False

    ## (기존 방식 - 시작 지점을 고정)
    # start = 1
    # dist[start] = 0

    ## (응용 - 시작 지점을 고정할 필요가 없음)

    # 전체 노드에 대하여 반복
    for i in range(n):

        # 모든 노드에 대해서 모든 간선을 확인
        for j in range(len(edge)):
            current, next_node, cost = edge[j]
            
            # 현재 간선에서 다음 노드로 이동하는 거리가 더 짧을 경우 갱신
            ## (기존 방식 - 특정 Node에서 출발해서 다른 Node로 가는 최단거리)
            # if dist[current] != INF and dist[next_node] > dist[current] + cost:
            #     dist[next_node] = dist[current] + cost

            #     if i == n-1:
            #         negative_cycle = True

            ## (응용 - 출발 지점이 없고, 단순 싸이클의 존재 유무만 확인)
            if dist[next_node] > dist[current] + cost:
                dist[next_node] = dist[current] + cost

                if i == n-1:
                    negative_cycle = True
                    break

    if negative_cycle:
        print("YES")
    else:
        print("NO")

"""
    밸만포드 알고리즘에 대하여 공부할 수 있었습니다!

    시작지점이 없다는 포인트 때문에 상당히 해맸었는데, 모든 지점을 시작점으로 할 것이 아니라
    단순히, 출발 지점에 대한 제약만 없애주면 되는 것이었네요. 

    다만, 이렇게 할 경우, 간선의 갱신을 Node의 개수만큼 진행하는 것이 최적인지는 의문으로 남았습니다.
"""
