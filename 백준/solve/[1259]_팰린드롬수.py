import sys
input = sys.stdin.readline

def check_palindrome(num: str):
    num = list(num)

    check = True
    if len(num) % 2 == 0:
        left = len(num) // 2 - 1
        right = len(num) // 2
    else:
        left = len(num) // 2 - 1
        right = len(num) // 2 + 1

    while 0<=left and right<len(num):
        if num[left] == num[right]:
            left -= 1
            right += 1
        else:
            check = False
            break

    return check

while True:
    number = input().strip()

    if number == "0":
        break
    
    if check_palindrome(number):
        print("yes")
    else:
        print("no")
