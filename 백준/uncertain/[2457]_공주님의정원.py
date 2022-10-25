"""
    정렬 + 스택비교

    1. 종료시점으로 꽃들을 정렬
    2. 하나씩 스택에 삽입
        2-1. 스택이 두 개 이상일 경우
            2-1-1. 시작시점이 앞앞 꽃의 종료시점보다 빠를 경우
                (앞 꽃을 pop한 후, 새 꽃을 삽입)
            2-1-2. 시작시점이 앞앞 꽃의 종료시점보다 느리고, 앞 꽃의 종료시점보다 빠를 경우
                (새 꽃을 삽입)
            2-1-3. 그 외
                (무시)
        
        2-2. 스택이 한 개 있을 경우
            2-2-1. 시작시점이 301보다 빠른 경우
                (앞 꽃을 pop한 후, 새 꽃을 삽입)
            2-2-2. 시작시점이 301보다 느리고, 앞 꽃의 종료시점보다 빠를 경우
                (새 꽃을 삽입)
            2-2-2. 그 외
                (무시)
"""

import sys
input = sys.stdin.readline

n = int(input())

flower = []
for _ in range(n):
    m1, d1, m2, d2 = list(map(int, input().split()))
    flower.append((m1*100+d1, m2*100+d2))

# 예외 조건: 3월1일부터 11월30일까지 매일 꽃이 한 가지 이상 피어있어야 한다.
except1 = 301
except2 = 1130

# 1. 종료시점으로 꽃들을 정렬
flower.sort(key = lambda x: x[1])

# 2. 하나씩 스택에 삽입
stack = []

for i in range(len(flower)):
    start, end = flower[i]

    insert = True
    while stack:
        last_start, last_end = stack.pop()

        # 2-1. 스택이 두 개 이상일 경우
        if stack:

            # 2-1-1. 시작시점이 앞앞 꽃의 종료시점보다 빠를 경우
            if start <= stack[-1][1]:
                continue

            # 2-1-2. 시작시점이 앞앞 꽃의 종료시점보다 느리고, 앞 꽃의 종료시점보다 빠를 경우
            elif start > stack[-1][1] and start <= last_end:
                stack.append((last_start, last_end)) 
                break

            # 2-1-3. 그 외
            else:
                stack.append((last_start, last_end))
                insert = False
                break
        
        # 2-2. 스택이 한 개 있을 경우
        else:
            # 2-2-1. 시작시점이 301보다 빠른 경우
            if start <= 301:
                continue

            # 2-2-2. 시작시점이 301보다 느리고, 앞 꽃의 종료시점보다 빠를 경우
            elif start >= 301 and start <= last_end:
                stack.append((last_start, last_end))
                break

            # 2-2-3. 그 외
            else:
                stack.append((last_start, last_end))
                insert = False
                break

    if insert and start <= except2:
        stack.append((start, end)) 

# 예외 케이스
except2_count = sum([1 for s in stack if s[1] > except2])
except1_count = sum([1 for s in stack if s[0] <= except1])

if except2_count == 0 or except1_count == 0:
    print(0)
elif except2_count > 1:
    print(len(stack) - except2_count + 1)
else:
    print(len(stack))