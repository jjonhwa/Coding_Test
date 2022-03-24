from itertools import permutations

def solution(user_id, banned_id):
    answers = []
    
    # permutations을 활용하여 banned_id와 비교
    user_perm = permutations(user_id, len(banned_id))
    for users in user_perm:
        
        check = True
        for user, banned in zip(users, banned_id): # 하나씩 꺼내오면서 비교
            if len(user) != len(banned): # 길이가 다르다면 break
                check = False
                break
            
            # 길이가 같다면 한글자씩 비교하여 user_id가 banned_id와 같은지 확인
            for i in range(len(user)):
                if banned[i] == '*':
                    continue
                if banned[i] != user[i]:
                    check = False
                    break
            
            if not check:
                break
        if check:
            answers.append(users)
    # answers = [('frodo', 'abc123'), ('fradi', 'abc123')]
    
    # 중복제거를 위하여 dictionary를 활용
    answer_dict = {}
    for ans in answers:
        ans = list(ans)
        ans.sort()
        answer_dict[str(ans)] = 1
    
    return sum(answer_dict.values())