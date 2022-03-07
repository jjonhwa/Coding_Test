# 팰린드롬: 앞, 뒤가 똑같은 단어나 문장. 즉, 뒤집어도 똑같은 말이 되는 문장 혹은 단어
# 속도: 상위 8% / 메모리: 하위 10% => 메모리 측면에서 부족한 풀이

class Solution:
    def isPalindrome(self, s: str) -> bool:
        check_string = s
        
        # remove special string and make alphabet lower
        remove_special = []
        for string in check_string:
            string = string.lower()
            if string.isalpha() or string.isdigit():
                remove_special.append(string)

        # check until half length of string
        check_point = len(remove_special) // 2
                
        # if first alphabet and second alphabet are not same, answer is False
        answer = True
        for i in range(check_point):
            if remove_special[i] == remove_special[-1-i]:
                continue
            else:
                answer = False
                break

        return answer
