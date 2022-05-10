import sys
input = sys.stdin.readline

num_list = list(map(int, input().split()))

value = 0

for num in num_list:
    value += num**2
value %= 10
print(value)