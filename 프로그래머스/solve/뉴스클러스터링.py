import re
def solution(str1, str2):
    answer = 0
    # 소문자 변경, 스페이스 제거
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 두 개씩 쪼개기
    first_list = []
    for f, s in zip(str1, str1[1:]) :
        if f.isalpha() and s.isalpha() :
            first_list.append(''.join([f,s]))
    second_list = []
    for f, s in zip(str2, str2[1:]) :
        if f.isalpha() and s.isalpha() :
            second_list.append(''.join([f,s]))
    
    # 교집합, 합집합 만들기
    intersect = set(first_list) & set(second_list)
    union = set(first_list) | set(second_list)

    # 공집합일 경우
    if not union :
        return 65536
    
    # 유사도 구하기
    intersect_sum = sum([min(first_list.count(inter), second_list.count(inter)) for inter in intersect])
    union_sum = sum([max(first_list.count(uni), second_list.count(uni)) for uni in union])
    answer = intersect_sum / union_sum
    answer = int(answer * 65536)
    
    
    return answer
  
  
from typing import List

def jakad_similarity(set1: List, set2: List) -> float:
    normal_union = set(set1).union(set(set2))
    normal_intersection = set(set1).intersection(set(set2))
    
    jakad_union = []
    jakad_intersection = []
    
    for union_element in normal_union:
        cnt = max(set1.count(union_element), set2.count(union_element))
        for _ in range(cnt):
            jakad_union.append(union_element)
    
    for intersection_element in normal_intersection:
        cnt = min(set1.count(intersection_element), set2.count(intersection_element))
        for _ in range(cnt):
            jakad_intersection.append(intersection_element)
    
    if len(jakad_union):
        return len(jakad_intersection) / len(jakad_union)
    else:
        return 1
    
def solution(str1, str2):
    answer = 0
    
    # 두 글자씩 끊어서 다중집합의 원소로 만든다.
        # 두 글자씩 끊는다.
        # 기타 공백, 숫자, 특수문자는 제거한다. (is_alpha)
    multiset_1 = []
    multiset_2 = []
    
    str1 = str1.lower()
    str2 = str2.lower()
    
    for i in range(len(str1)-1):
        abnormal = False
        
        for string in str1[i:i+2]:
            if not string.isalpha():
                abnormal = True
        
        if not abnormal:
            multiset_1.append(str1[i:i+2])
            
    for i in range(len(str2)-1):
        abnormal = False
        
        for string in str2[i:i+2]:
            if not string.isalpha():
                abnormal = True
        
        if not abnormal:
            multiset_2.append(str2[i:i+2])
        
    js = jakad_similarity(multiset_1, multiset_2)
    return int(js * 65536)
