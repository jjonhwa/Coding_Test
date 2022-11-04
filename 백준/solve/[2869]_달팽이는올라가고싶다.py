import sys
input = sys.stdin.readline

a, b, v = list(map(int, input().split()))
check_value = v-a
up = a-b

go_up = check_value // up
more = check_value % up
if more:
    go_up += 1
print(go_up+1)
