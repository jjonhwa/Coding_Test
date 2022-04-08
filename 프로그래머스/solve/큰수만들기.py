def solution(number, k):
    stack = [number[0]]
    for num in number[1:] :
        while len(stack) > 0 and stack[-1] < num and k > 0 :
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0 :
        stack = stack[:-k]
    return ''.join(stack)
  
# 더 빠름
from collections import deque

def solution(number, k):
    answer = ''
    
    length = len(number)-k
    number = deque(list(number))
    stack = []
    
    # initialization
    first = number.popleft()
    stack.append(first)
    
    while number:
        num = number.popleft()
        
        while stack and k:
            if num > stack[-1]:
                stack.pop()
                k -= 1
            else:
                stack.append(num)
                break
            
        if not stack or not k:
            stack.append(num)
        
        if not k:
            stack += number
            break
    
    if len(stack) > length:
        return ''.join(stack)[:length]

    return ''.join(stack)
