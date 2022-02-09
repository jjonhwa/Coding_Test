import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
rice = list(map(int, input().split()))

start = 0
end = max(rice)
compare = []
while True:
    mid = (start + end) // 2
    cutting = 0
    for r in rice:
        if r > mid:
            cutting += (r-mid)
    compare.append([mid, cutting])
    if start > mid:
        break
    if cutting > M:
        start = mid + 1
    else:
        end = mid - 1

final = []
for c in compare:
    if c[1] >= M:
        final.append(c)
final.sort(key = lambda x: x[1])
print(final[0][0])