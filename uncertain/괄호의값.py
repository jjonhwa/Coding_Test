import sys
from collections import deque
input = sys.stdin.readline

bracket = input()

# 예외 Case
# open, close의 개수가 다를 경우
# 서로 다른 괄호가 open, close 될 경우
# ) 혹은 ]로 시작할 경우
exception = False
open_n = 0
close_n = 0
open_s = 0
close_s = 0
start = bracket[0]
if start == '(': open_n += 1
elif start == '[': open_s += 1
elif start == ')': exception = True
elif start == ']': exception = True

for first, second in zip(bracket, bracket[1:]):
    if second == '(': open_n += 1
    elif second == '[': open_s += 1
    elif second == ')': close_n += 1
    elif second == ']': close_s += 1

    if (first == '(' and second == ']') or (first == '[' and second == ')'):
        exception = True
        break

if not exception:
    if (open_n != close_n) or (open_s != close_s):
        exception = True

# 예외가 아닐 경우
# 괄호가 포함되거나 따로 떨어져있어야 올바른 괄호열
# (()[[]])([])
# '(' => '((' => '(2' => '(2[' =>
# '(2[[' => '(2[3' => '(2 9' => '(11' =>
# '22' => '22(' => '22([' => '22(3' =>
# '22 6' => '28

if not exception:
    bracket = deque(list(bracket))
    start = bracket.popleft()
    stack = [start]

    while len(bracket):
        b = bracket.popleft()
        
        # 숫자가 연속해서 2개가 들어올 경우 더해주기
        if len(stack) >= 2 and stack[-1].isdigit() and stack[-2].isdigit():
            cal1 = int(stack.pop())
            cal2 = int(stack.pop())
            stack.append(str(cal1 + cal2))

        # ()가 오면 괄호를 빼주고 2 삽입
        # '((' 혹은 '([' 혹은 '숫자(' 혹은 '숫자['가 올 경우, 그냥 삽입
        if stack[-1] == '(' and b == ')':
            stack.pop()
            stack.append('2')
            continue
        elif (stack[-1] == '(' or stack[-1].isdigit()) and (b == '(' or b == '['):
            stack.append(b)
            continue

        # []가 오면 괄호를 빼주고 3 삽입
        # '[[' 혹은 '[[' 혹은 '숫자[' 혹은 '숫자('가 올 경우, 그냥 삽입
        if stack[-1] == '[' and b == ']':
            stack.pop()
            stack.append('3')
            continue
        elif (stack[-1] == '[' or stack[-1].isdigit()) and (b == '(' or b == '['):
            stack.append(b)
            continue

        # [숫자]일 경우, "3 * 숫자" 삽입
        # (숫자)일 경우, "2 * 숫자" 삽입
        if len(stack) >= 2 and stack[-1].isdigit() and stack[-2] == '[' and b == ']':
            cal1 = int(stack.pop())
            stack.pop()
            stack.append(str(cal1 * 3))
        elif len(stack) >= 2 and stack[-1].isdigit() and stack[-2] == '(' and b == ')':
            cal1 = int(stack.pop())
            stack.pop()
            stack.append(str(cal1 * 2))
else:
    stack = ['0']
print(int(stack[0]))