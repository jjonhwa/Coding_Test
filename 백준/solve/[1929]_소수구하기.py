import sys
import math
input = sys.stdin.readline

m, n = list(map(int, input().split()))

def find_primary(num):
    array = [True for _ in range(num+1)]
    array[0], array[1] = False, False

    for i in range(2, int(math.sqrt(num)) + 1):
        if array[i]:

            j = 2
            while (i*j) <= num:
                if array[i*j]:
                    array[i*j] = False

                j += 1

    return array

array1 = find_primary(n)
array1 = [i for i in range(len(array1)) if array1[i]]
array1 = [value for value in array1 if value >= m]

for i in range(len(array1)):
    print(array1[i])