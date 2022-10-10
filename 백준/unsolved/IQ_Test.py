"""
연립방정식 풀이

y1 - b = a * x1
y2 - b = a * x2
=> a(x1-x2) = (y1-y2)
=> a = (y1-y2) / (x1-x2)
=> a = (data[1]-data[2]) / (data[0]-data[1])
"""

import sys

input = sys.stdin.readline
n = int(input())
values = list(map(int, input().split()))

# 값이 1개일 경우: 여러개 가능
if len(values) == 1:
    print("A")
    exit()

# 값이 2개일 경우: 같은 값 => 같은 값 return, 다른 값 => 여러개 가능 
if len(values) == 2:
    if values[0] == values[1]:
        print(values[1])
    else:
        print("A")
    exit()

# 값이 3개 이상일 경우
if values[0] - values[1] == 0: # ZeroDivisionError 방지 및 같은 값일 경우
    if values[1] - values[2] == 0: # 세수가 같다면 `*1+0` 혹은 `*0+값` 가능
        a = 1 # 0도 가능
    else: # 하나라도 다르다면 계산 불가능
        print("B")
        exit()
else:
    # 연립방정식을 통한 해 
    # => a가 정수가 아니라면 정수인 a를 얻을 수 없음 => 값 취득 불가능
    a = (values[1] - values[2]) / (values[0] - values[1])
    int_a = int(a)

    if a != int_a:
        print("B")
        exit()
    else:
        a = int(a)

b = values[1] - values[0]*a

# 연립방정식을 통해 얻은 값을 활용하여 수열에 적용 => 틀릴 경우 can=False
can = True
for first, second in zip(values, values[1:]):
    if second != first*a+b:
        can = False
        break

if can and len(values) != 1:
    print(values[-1]*a+b)
else:
    print("B")

