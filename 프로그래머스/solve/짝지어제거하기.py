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
