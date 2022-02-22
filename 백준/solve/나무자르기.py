import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
tree = list(map(int, input().split()))

start = 0
end = max(tree)
while True:
    mid = (start + end) // 2
    if start > end:
        break
    cutting = sum([t-mid for t in tree if t > mid]) 
    if cutting == M:
        break
    elif cutting > M:
        start = mid + 1
    else:
        end = mid - 1
print(mid)