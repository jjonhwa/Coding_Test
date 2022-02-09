import sys
input = sys.stdin.readline

N = int(input())
have = list(map(int, input().split()))
have.sort()

M = int(input())
find = list(map(int, input().split()))

def binary_search(have, find_element):
    start = 0
    end = len(have)-1
    while True:
        mid = (start + end) // 2
        if start > end:
            return False
        if have[mid] == find_element:
            return True
        elif have[mid] > find_element:
            end = mid-1
        else:
            start = mid+1

for i in range(len(find)):

    if binary_search(have, find[i]):
        print('yes', end = ' ')
    else:
        print('no', end = ' ')