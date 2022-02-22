import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
number = list(map(int, input().split()))
operator_count = list(map(int, input().split()))

# 나눗셈은 몫만을 취한다.
# 음수 / 양수 => '양수 / 양수'를 취한 후 몫을 취하고, 그 몫을 음수로 바꾼다.
operator = []
for i, oper in enumerate(operator_count):
    if i == 0:
        for _ in range(oper):
            operator.append('+')
    elif i == 1:
        for _ in range(oper):
            operator.append('-')
    elif i == 2:
        for _ in range(oper):
            operator.append('*')
    elif i == 3:
        for _ in range(oper):
            operator.append('/')

# 완전탐색
maximum = -1e9
minimum = 1e9
total = 0

# 연산자의 개수 10개 => 10! = 약 360만
# 시간복잡도: 360만 x 11 => 약 4천만
for perm in permutations(operator, N-1):
    total = number[0]
    for i in range(1, len(number)):
        if perm[i-1] == '*': 
            total *= number[i]
        elif perm[i-1] == '+':
            total += number[i]
        elif perm[i-1] == '-':
            total -= number[i]
        elif perm[i-1] == '/':
            total = int(total/number[i])

    if total > maximum:
        maximum = total
    if total < minimum:
        minimum = total

print(maximum)
print(minimum)
