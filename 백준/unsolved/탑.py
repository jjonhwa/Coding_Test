import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
# reverse_top = [i for i in top[::-1]]

stack = []
for i in range(len(top)):
    if stack:
        while stack:
            value, index = stack[-1]
            if value < top[i]:
                stack.pop()
                if not stack: # stack에 아무것도 없을 경우 0출력
                    print(0, end=' ') 
            elif value > top[i]:
                print(index+1, end=' ')
                break
            else:
                print(index+1, end=' ')
                stack.pop()
                break
        stack.append([top[i], i])
    else:
        print(0, end=' ')
        stack.append([top[i], i])