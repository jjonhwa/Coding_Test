# 더 빠름
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

# 
def solution(s):
    answer = 0
    
    # 문자열의 길이가 1이라면 1 return
    if len(s) == 1:
        return 1
    
    string_length = []

    max_cutting = len(s) // 2 # 문자열을 자를 수 있는 최대 길이 정의

    # 길이를 1개씩 늘려주면서 자를 수 있는 문장 max_length 확인
    for i in range(1, max_cutting+1):
        check = list(s)
        check.reverse() # => deque 사용시 시간 더 단축 가능
        
        # i의 길이만큼 문장을 절단하여 list에 삽입해줍니다.
        # if i == 2라면
            # ["aa", "bb", "ac", "cc"]
        split_string = []
        while check:
            tmp_string = ''
            for _ in range(i):
                if check:
                    tmp_string += check.pop()
                else:
                    break
            split_string.append(tmp_string)
        
        # zip으로 두 문장을 비교하면스 같은 문장이 나올 경우 cnt를 늘려주고
        # 나오지 않을 경우, 바로 새로운 string에 삽입해줍니다.
        string = ''
        cnt = 1
        for first, second in zip(split_string, split_string[1:]):
            if first == second:
                cnt += 1
            else:
                if cnt == 1:
                    string += first
                else:
                    string += str(cnt) + first
                    cnt = 1
        
        if cnt != 1:
            string += str(cnt) + second
        else:
            string += second
        
        # i의 길이만큼 잘랐을 떄, 문장의 길이 저장
        string_length.append(len(string))
        
    # 그 길이 중 최소값을 return
    return min(string_length)
