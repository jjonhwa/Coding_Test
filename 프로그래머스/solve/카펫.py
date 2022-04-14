# 더 빠름
def solution(brown, yellow):
    answer = []
    vertical = 3
    horizontal = int((brown + 4 - 2*vertical)/2)
    
    while True :
        if (vertical-2)*(horizontal-2) == yellow :
            break
        else :
            vertical += 1
            horizontal -= 1
    answer.append(horizontal)
    answer.append(vertical)
    return answer
    
    
# brown + yellow를 기준으로 공약수 계산
# 공약수를 for loop 돌면서, yellow를 만족하는 경우 탐색
from typing import List

def gongyaksu(number: int) -> List[int]:
    max_devide = number // 2
    
    yaksu_list = []
    for i in range(2, max_devide+1):
        if number % i == 0:
            yaksu_list.append(i)
    
    return yaksu_list

def solution(brown, yellow):
    yaksu = gongyaksu(brown+yellow)
    
    for i in range(len(yaksu)):
        x = yaksu[i]
        y = (brown+yellow) // x
        
        if (x-2) * (y-2) == yellow:
            return (x,y) if x>=y else (y,x)
