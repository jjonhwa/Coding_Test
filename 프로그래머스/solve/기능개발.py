def solution(progresses, speeds):
    answer = []
    num_list = []
    n = 1
    for pro, spe in zip(progresses, speeds) :
        n = 1
        while True :
            if pro + n*spe >= 100 :
                break
            n += 1
        num_list.append(n)
        
    count = 1
    for i in range(1, len(num_list)) :
        if num_list[i] < num_list[i-1] :
            num_list[i] = num_list[i-1]
        if num_list[i] == num_list[i-1] :
            count += 1
        else :
            answer.append(count)
            count = 1
    answer.append(count)
    return answerv
