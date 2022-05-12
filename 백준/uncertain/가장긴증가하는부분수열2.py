import sys
input = sys.stdin.readline

n = input()
array = map(int, input().split())

lis_arr = [0]
for num in array:
    if not lis_arr:
        lis_arr.append(num)
    elif lis_arr[-1] < num:
        lis_arr.append(num)
    else:
        left = 0
        right = len(lis_arr)
        while left < right:
            mid = (left + right) // 2

            if lis_arr[mid] < num:
                left = mid + 1
            else:
                right = mid
        lis_arr[right] = num
print(len(lis_arr)-1)