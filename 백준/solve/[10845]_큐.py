from collections import deque

import sys
input = sys.stdin.readline

queue = deque([])

def push(x):
    queue.append(x)

def pop():
    if queue:
        x = queue.popleft()
        print(x)
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[-1])
    else:
        print(-1)

n = int(input())
for _ in range(n):
    command = input().rstrip().split()
    if len(command) == 2:
        command, value = command[0], command[1]
    else:
        command = command[0]

    if command == "push":
        push(value)
    elif command == "pop":
        pop()
    elif command == "front":
        front()
    elif command == "back":
        back()
    elif command == "size":
        size()
    elif command == "empty":
        empty()