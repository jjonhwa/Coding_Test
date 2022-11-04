import sys
input = sys.stdin.readline

dictionary = {
    "(": ")",
    "[": "]"
}
while True:
    string = input().rstrip()

    if string == ".":
        break

    stack = []
    no = False
    for s in string:
        if s in ["(", "["]:
            stack.append(s)
        elif s in [")", "]"]:   
            if stack:
                if dictionary[stack[-1]] == s:
                    stack.pop()
                else:
                    no = True
                    break
            else:
                no = True
                break

    if stack:
        no = True

    if no:
        print("no")
    else:
        print("yes")