from collections import deque
from re import L
import sys
input = sys.stdin.readline

class Deque():
    def __init__(self, queue):
        self.queue = queue   

    def push_front(self, value):
        self.queue.appendleft(value)

    def push_back(self, value):
        self.queue.append(value)

    def pop_front(self):
        if self.queue:
            print(self.queue.popleft())
        else:
            print(-1)
    
    def pop_back(self):
        if self.queue:
            print(self.queue.pop())
        else:
            print(-1)
        
    def size(self):
        print(len(self.queue))
    
    def empty(self):
        if self.queue:
            print(0)
        else:
            print(1)
        
    def front(self):
        if self.queue:
            print(self.queue[0])
        else:
            print(-1)
    
    def back(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print(-1)

n = int(input())
locker = Deque(deque([]))

for _ in range(n):
    command = input().strip().split()
    

    value = None
    if len(command) >= 2:
        value = int(command[1])
    command = command[0]

    if command == "push_back":
        locker.push_back(value)
    elif command == "push_front":
        locker.push_front(value)
    elif command == "front":
        locker.front()
    elif command == "back":
        locker.back()
    elif command == "size":
        locker.size()
    elif command == "empty":
        locker.empty()
    elif command == "pop_front":
        locker.pop_front()
    elif command == "pop_back":
        locker.pop_back()
