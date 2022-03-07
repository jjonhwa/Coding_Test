# 내 풀이
# 속도: 상위 20% | 메모리: 상위 10%
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 애너그램: 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
        spell_check = {}
        for string in strs:
            sort_string = ''.join(sorted(string))        # 정렬한 후 단어로 재생성
           
            if sort_string in spell_check.keys():
                spell_check[sort_string].append(string)  # key는 정렬된 단어 | value는 기존 단어
            else:
                spell_check[sort_string] = [string]
        
        answer = []
        for value in spell_check.values():               # 기존 단어들만 list형태로 answer에 삽입
            answer.append(value)
        
        return answer
      
# 정답 본 후, 내 풀이 수정
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 애너그램: 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
        spell_check = {}
        for string in strs:
            sort_string = ''.join(sorted(string))
           
            if sort_string in spell_check.keys():
                spell_check[sort_string].append(string)
            else:
                spell_check[sort_string] = [string]
        
        return spell_check.values()
      
# 정답
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 애너그램: 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        
        return anagrams.values()
