import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input().split()))

m = int(input())
find_num = list(map(int, input().split()))

set_num = set(num_list)
[print(1) if num in set_num else print(0) for num in find_num]

