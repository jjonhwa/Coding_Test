import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))
# reverse_top = [i for i in top[::-1]]

stack = []
for i in range(len(top)):
    if stack:
        while stack:
            height, index = stack[-1]
            if height < top[i]: # 더 높은 타워가 결국 들어오므로, 더 작은 타워는 stack에서 pop
                stack.pop()
                if not stack: # stack에 아무것도 없을 경우 0출력
                    print(0, end=' ') 
            elif height > top[i]: # 자기보다 높은 타워가 있을 경우, 그 타워의 index 출력
                print(index+1, end=' ')
                break
            else: # 타워의 높이가 같을 경우, 출력해주고 pop. 이후 다시 append해주므로.
                print(index+1, end=' ')
                stack.pop()
                break
        stack.append([top[i], i])
    else:
        print(0, end=' ')
        stack.append([top[i], i])