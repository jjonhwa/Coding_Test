"""
    에라토스테네스의 체 + 투포인터
"""
import sys
import math

input = sys.stdin.readline

def is_prime_num(n):
    arr = [True] * (n+1)
    arr[0] = False
    arr[1] = False
    
    check_point = int(math.sqrt(n)) + 1
    for i in range(2, check_point):
        if arr[i] == True:
            j = 2

            while (i*j) <= n:
                arr[i*j] = False
                j += 1
    
    return arr

n = int(input())

prime = is_prime_num(4000000)
prime = [i for i in range(len(prime)) if prime[i]]

left_pointer, right_pointer = 0, 0

if n == 1:
    answer = 0
elif n == 2:
    answer = 1
else:
    answer = 0
    check_answer = prime[answer]

while True:

    # n=1, n=2일 경우, 루프를 돌 필요가 없으므로 종료
    if n == 1 or n == 2:
        break

    # 1. 연속합의 값이 목표값보다 작을 경우 right up, 크거나 같을 경우 left up
    if check_answer < n:
        right_pointer += 1
        
        if right_pointer >= len(prime):
            break

        check_answer += prime[right_pointer]
    else:
        check_answer -= prime[left_pointer]
        left_pointer += 1

        if left_pointer > right_pointer:
            break

    # 2. 합이 n과 같을 경우 count
    if check_answer == n:
        answer += 1

print(answer)