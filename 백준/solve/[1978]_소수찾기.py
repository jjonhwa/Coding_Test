import sys
import math
input = sys.stdin.readline

def prime_array(num):
    arr = [True for _ in range(num)]
    arr[0], arr[1] = False, False

    for i in range(2, int(math.sqrt(num))+1):
        if arr[i]:
            j = 2

            while i*j < num:
                arr[i*j] = False
                j += 1
    return arr

n = int(input())
num_list = list(map(int, input().split()))
max_num = max(num_list)

prime_set = prime_array(max_num + 1)
prime_set = set([i for i in range(len(prime_set)) if prime_set[i]])

answer = 0
for num in num_list:
    if num in prime_set:
        answer += 1

print(answer)