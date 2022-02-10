import sys
input = sys.stdin.readline

N, M = list(map(int, input().split()))
money_list = list(map(int, input().split()))
money_count = [999999] * (10000+1)
money_count[0] = 0

for i in range(len(money_count)):
    for money in money_list:
        if i+money <= len(money_count)-1:
            money_count[i+money] = min(money_count[i+money], money_count[i]+1)

if money_count[M] == 999999:
    print(-1)
else:
    print(money_count[M])