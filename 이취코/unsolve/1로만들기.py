import sys
input = sys.stdin.readline

X = int(input())
check_list = [0] * (X+1)

for i in range(2, X+1):
    # 1을 빼는 경우
    check_list[i] = check_list[i-1]+1

    # 2로 나누어 떨어지는 경우

    if i % 2 == 0:
        divide_num = i // 2
        check_list[i] = min(check_list[i], check_list[divide_num]+1)
    if i % 3 == 0:
        divide_num = i // 3
        check_list[i] = min(check_list[i], check_list[divide_num]+1)
    if i % 5 == 0:
        divide_num = i // 5
        check_list[i] = min(check_list[i], check_list[divide_num]+1)
print(check_list[-1])