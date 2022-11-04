import sys
input = sys.stdin.readline


def push(stack, x):
    stack.append(x)
    return stack

def pop(stack):
    if stack:
        pop_value = stack.pop()
        print(pop_value)
    else:
        print(-1)
    return stack

def size(stack):
    print(len(stack))

def empty(stack):
    if stack:
        print(0)
    else:
        print(1)

def top(stack):
    if stack:
        print(stack[-1])
    else:
        print(-1)

n = int(input())

stack = []
for _ in range(n):
    command = input().rstrip().split()
    if len(command) == 2:
        command, value = command[0], command[1]
    else:
        command = command[0]

    if command == "push":
        push(stack, value)
    elif command == "pop":
        pop(stack)
    elif command == "size":
        size(stack)
    elif command == "empty":
        empty(stack)
    elif command == "top":
        top(stack)
    