import sys
from itertools import combinations
input = sys.stdin.readline().rstrip()

strings = input

# 같은 bracket끼리 같은 숫자로 표시
bracket_check = []
max_cnt = 0
stack = []
for string in strings:
    if string == '(':
        max_cnt += 1
        stack.append(max_cnt)
        bracket_check.append(max_cnt)
    elif string == ')':
        cnt = stack.pop()
        bracket_check.append(cnt)
    else:
        bracket_check.append(0)

remove_bracket = []
comb_list = [i+1 for i in range(max_cnt)] # [1,2,3]
for c in comb_list: 
    # 1개짜리, 2개짜리, 3개짜리, ...
    for remove in list(combinations(comb_list, c)): # [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
        tmp = bracket_check.copy()
        for r in remove:
            tmp = [-1 if b==r else b for b in tmp]

        check = ''
        for o, r in zip(strings, tmp):
            if r == -1:
                continue
            check += o
        remove_bracket.append(check)

remove_bracket = set(remove_bracket)
for re in sorted(list(remove_bracket)):
    print(re)