import sys
input = sys.stdin.readline

N, S = list(map(int, input().split()))
num_list = list(map(int, input().split()))

if max(num_list) >= S:
    print(1)
else:
    left, right = 0, 0
    minimum_length = float('inf')
    summation = num_list[left]

    while left <= right:
        if summation >= S:
            minimum_length = min(minimum_length, right-left+1)
            summation -= num_list[left]
            left += 1
            
        else:
            right += 1
            if right >= len(num_list):
                break
            summation += num_list[right]
   
    if minimum_length == float('inf'):
        print(0)
    else:
        print(minimum_length)
