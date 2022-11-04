from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

count_dict = Counter(card)
for num in check:
    print(count_dict[num], end = " ")

