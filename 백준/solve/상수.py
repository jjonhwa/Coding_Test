import sys
input = sys.stdin.readline

num_list = input().split()

answer = 0
for num in num_list:
    new_num = ''
    for i in range(1, len(num)+1):
        new_num += num[-i]
    answer = max(answer, int(new_num))
print(answer)