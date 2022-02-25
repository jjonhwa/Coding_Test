def palindrome_check(string):
    """팰린드롬 확인하는 함수"""
    if len(string) % 2 == 0: # 짝수
        divide_point = len(string) // 2
        former = string[:divide_point]
        latter = string[divide_point:]
    else:
        divide_point = (len(string)+1) // 2
        former = string[:divide_point-1]
        latter = string[divide_point:]
    
    if former == latter[::-1]:
        return True
    else:
        return False
    
def solution(s):
    answer = 0

    max_length = False
    for i in range(len(s)):
        for j in range(len(s), i, -1):    
            if palindrome_check(s[i:j+1]):
                answer_candidate = len(s[i:j+1])
                answer = max(answer, answer_candidate)
                
    return answer