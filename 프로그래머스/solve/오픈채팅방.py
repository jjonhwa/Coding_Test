# 기존 풀이
def solution(record):
    name_dict = {}
    out_list = []
    for re in record :
        if re.split(' ')[0] == 'Enter'  or re.split(' ')[0] == 'Change':
            name_dict[re.split(' ')[1]] = re.split(' ')[2]
        if re.split(' ')[0] == 'Enter' :
            out_list.append('{}님이 들어왔습니다.'.format(re.split(' ')[1]))
        elif re.split(' ')[0] == 'Leave' :
            out_list.append('{}님이 나갔습니다.'.format(re.split(' ')[1]))

    final_list = []
    for item in out_list :
        id_ = name_dict.get(item.split('님')[0])
        final_list.append(id_ + '님' + item.split('님')[1])
    return final_list
  
# 한 번 더
def solution(record):
    answer = [] # 최종 정답
    id_answer = [] # id로 구성된 정답
    id_name_pair = {} # key: id / value: name
    
    for re in record:
        if re.split()[0] == 'Enter':
            behavior, _id, name = re.split()
            id_name_pair[_id] = name
            sentence = _id + '님이 들어왔습니다.'
            id_answer.append(sentence)
        elif re.split()[0] == 'Leave':
            behavior, _id = re.split()
            sentence = _id + '님이 나갔습니다.'
            id_answer.append(sentence)
        else:
            behavior, _id, name = re.split()
            id_name_pair[_id] = name
            
    for ans in id_answer:
        _id = ans.split('님')[0]
        answer.append(ans.replace(_id, id_name_pair[_id]))
                                                    
    return answer
