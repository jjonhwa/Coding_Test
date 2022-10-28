import sys
input = sys.stdin.readline

num = int(input())

is_answer = False
for candidate_num in range(1, num):
    constructor = int(candidate_num)

    for digit in str(candidate_num):
        constructor += int(digit)

    if constructor == num:
        is_answer = True
        break

if not is_answer:
    print(0)
else:
    print(candidate_num)
