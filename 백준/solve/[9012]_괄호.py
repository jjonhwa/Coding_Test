import sys
input = sys.stdin.readline

dictionary = {
    "(": ")"
}

n = int(input())
for _ in range(n):
    braket = list(input().strip())

    stack = []
    no = False
    for b in braket:
        if b == "(":
            stack.append(b)
        else:
            if stack:
                if dictionary[stack[-1]] == b:
                    stack.pop()
                else:
                    stack.append(b)
            else:
                no = True
                break
    
    if no or stack:
        print("NO")
    else:
        print("YES")