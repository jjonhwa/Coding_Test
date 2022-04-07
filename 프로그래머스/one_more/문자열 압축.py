def solution(s):
    answer = []
    
    if len(s) == 1:
        return 1
    result = ''
    for cut in range(1, (len(s)//2)+1) :
        temp = s[:cut]
        count = 1
        for i in range(cut, len(s), cut) :
            if s[i:cut+i] == temp :
                count += 1
            else :
                if count == 1:
                    count = ''
                result += str(count) + temp
                temp = s[i:cut+i]
                count = 1
        if count == 1 :
            count = ''
        result += str(count) + temp
        answer.append(len(result))
        result = ''
    return min(answer)
