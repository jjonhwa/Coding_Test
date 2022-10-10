import sys
from math import gcd
input = sys.stdin.readline

n = int(input())
values = list(map(int, input().split()))

prefix_gcd = []
suffix_gcd = []

g = values[0]
prefix_gcd.append(g)
for i in range(1, len(values)):
    g = gcd(g, values[i])
    prefix_gcd.append(g)
    
g = values[-1]
suffix_gcd.append(g)
for i in range(len(values)-2, -1, -1):
    g = gcd(g, values[i])
    suffix_gcd.append(g)
suffix_gcd.reverse()

maximum_ans = float("-inf")
for i in range(len(values)):

    if i == 0:
        ans = suffix_gcd[i+1]
    elif i == len(values)-1:
        ans = prefix_gcd[i-1]
    else:
        ans = gcd(prefix_gcd[i-1], suffix_gcd[i+1])

    if gcd(ans, values[i]) != ans:
        if ans > maximum_ans:
            k = values[i]
            maximum_ans = ans

if maximum_ans == float("-inf"):
    print(-1)
else:
    print(maximum_ans, k)