import sys
input = sys.stdin.readline

while True:
    num_list= list(map(int, input().split()))
    num_list.sort()

    a, b, c = num_list 

    if a == 0 and b == 0 and c == 0:
        break

    if int(a**2) + int(b**2) == int(c**2):
        print("right")
    else:
        print("wrong")