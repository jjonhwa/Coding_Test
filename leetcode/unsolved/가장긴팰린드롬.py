# 1차시도 => time out
def check_palindrome(s: str) -> bool:
        length = len(s)
        half_length = len(s) // 2
        
        if length % 2 == 0: # even
            if s[:half_length] == s[half_length:][::-1]:
                return True
            else:
                return False
        if length % 2 != 0: # odd
            if s[:half_length] == s[half_length+1:][::-1]:
                return True
            else:
                return False
            
class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                cut_string = s[i:j]
                
                if check_palindrome(cut_string):
                    answer = cut_string if len(cut_string) >= len(answer) else answer
                    break
                    
        return answer
                
# 정답 풀이
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            """팰린드롬이 될 경우, 확장"""
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -= 1
                right += 1
            return s[left+1:right-1]
        
        answer = ''
        if len(s) < 2 or s == s[::-1]: # 길이가 1이거나, 뒤집어도 똑같을 경우 바로 return
            return s
        
        for i in range(len(s)-1):
            odd_lp, odd_rp = i, i+2
            even_lp, even_rp = i, i+1
            
            odd_string = expand(odd_lp, odd_rp)
            even_string = expand(even_lp, even_rp)
            
            answer = max(answer, odd_string, even_string, key = len)    
                
        return answe
            
