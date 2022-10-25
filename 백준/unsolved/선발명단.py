import sys
input = sys.stdin.readline

c = int(input())

def back_permutation(chosen, num):
    global max_value

    if len(chosen) == len(arr):
        summation = sum([graph[i][chosen[i]] for i in range(len(chosen))])
        max_value = max(max_value, summation)
        return

    for i in range(len(arr)):
        if not visit[i] and graph[num][i] != 0:
            chosen.append(arr[i])
            visit[i] = 1
            back_permutation(chosen, num+1)
            visit[i] = 0
            chosen.pop()

for _ in range(c):
    graph = []
    for _ in range(11):
        row = list(map(int, input().split()))
        graph.append(row)

    arr = [i for i in range(11)]
    visit = [0] * len(arr)
    max_value = float("-inf")

    back_permutation([], 0)

    print(max_value)