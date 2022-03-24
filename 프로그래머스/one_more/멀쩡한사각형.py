import math

def solution(w,h):
    answer = w+h-math.gcd(w, h)
    return w*h - answer