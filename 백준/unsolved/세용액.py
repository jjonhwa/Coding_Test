N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

three_point_sum = int(1e9)
result = []
zero = False
for i in range(N-2):
    lp, rp = i+1, N-1
    while lp < rp:
        sum_liquid = liquid[lp] + liquid[rp] + liquid[i]
        if abs(sum_liquid) < abs(three_point_sum):
            result = [lp, rp, i]
            three_point_sum = sum_liquid
        
        if sum_liquid == 0:
            result = [lp, rp, i]
            zero=True
            break
        elif sum_liquid < 0:
            lp += 1
        else:
            rp -= 1
    if zero:
        break

result.sort()
for r in result:
    print(liquid[r], end = ' ')
    