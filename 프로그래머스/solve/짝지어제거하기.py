def solution(s) :
    stack = []
    for string in s :
        if not stack :
            stack.append(string)
        elif stack[-1] == string :
            stack.pop()
        else :
            stack.append(string)
        
    if not stack :
        return 1
    else :
        return 0

    
from collections import deque

def solution(s):    
    string = deque(s)
    stack = []
    while string:
        spell = string.popleft()
        stack.append(spell)
        
        while len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
            else:
                break
    
    if stack:
        return 0
    else:
        return  1
