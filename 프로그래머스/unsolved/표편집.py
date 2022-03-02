def solution(n, k, cmd):
    answer = ''
    
    name_list = []
    for i in range(n):
        name_list.append([max(0,i-1), 'O', min(i+1,n-1)])
        # [[0,'O',1], [0,'O',2], [1,'O',3], [2,'O',4], ..., [5,'O',7], [6,'O',7]]
    
    delete_stack = []     # 삭제할 name & row
    now = k               # 현재 행
    for command in cmd:

        if "D" in command:
            move = command.split()[-1]
            for i in range(int(move)):
                now = name_list[now][2] # _next로 움직인 결과값

        elif 'U' in command:
            move = command.split()[-1]
            for i in range(int(move)):
                now = name_list[now][0] # prev로 움직인 결과값

        elif command == "C":
            name_list[now][1] = 'X'
            prev, _, _next = name_list[now]
            delete_stack.append([now, prev, _next])   

            # 주소 변환
            if now == name_list[now][2]: # 마지막 행일 경우
                name_list[prev][2] = prev # 기존 Node가 가지고 있는 다음 주소를 이전 Node의 다음 주소에 삽입 
                now = prev
            elif now == name_list[now][0]: # 첫 행일 경우
                name_list[_next][0] = _next
                now = _next
            else:
                name_list[prev][2] = _next
                name_list[_next][0] = prev
                now = _next

        elif command == 'Z':
            idx, prev, _next = delete_stack.pop()

            # 삽입 행
            name_list[idx][0] = prev
            name_list[idx][2] = _next
            name_list[idx][1] = 'O'

            # 이전 행
            if prev != idx:
                name_list[prev][2] = idx

            # 다음 행
            if _next != idx:
                name_list[_next][0] = idx
                
    for i in range(n):
        answer += name_list[i][1]
    return answer