import sys

input = sys.stdin.readline

string = input().split()

if string == sorted(string):
    print("ascending")
elif string == sorted(string, reverse = True):
    print("descending")
else:
    print("mixed")
