def solution(n):
    answer = ''
    while True:
        if n == 0:
            break
            
        remainder = n % 3
        n = n // 3
        
        if remainder == 0 and n != 0:
            n -= 1
            answer += str('4')
        else:
            answer += str(remainder)
    return answer[::-1]