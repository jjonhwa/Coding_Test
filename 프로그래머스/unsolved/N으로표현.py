def solution(N, number):
    answer = 0
    dp = []
    if N == number:                     # 주어진 숫자와 찾고자하는 숫자가 같을 경우 1 반환
        return 1
    
    case_set = set()
    for i in range(1,9):
        if int(str(N)*i) not in case_set:
            case_set.add(int(str(N)*i))
        
        i_half = i // 2             # 절반을 넘어간 시점엔 결국 똑같은 연산을 반복하므로 "i의 절반 = 1"에 대해서만 연산
        for j in range(0, i_half):
            for op1 in dp[j]:
                for op2 in dp[-1-j]:
                    if op1+op2 not in case_set:
                        case_set.add(op1+op2)
                    if op1-op2 not in case_set:
                        case_set.add(op1-op2)
                    if op2-op1 not in case_set:
                        case_set.add(op2-op1)
                    if op1*op2 not in case_set:
                        case_set.add(op1*op2)
                    if op1 != 0: 
                        if op2//op1 not in case_set:
                            case_set.add(op2 // op1)
                    if op2 != 0:
                        if op1//op2 not in case_set:
                            case_set.add(op1 // op2)
        if number in case_set:      # 찾고자 하는 숫자가 들어있을 경우 반환
            return i
        dp.append(case_set)
    return -1