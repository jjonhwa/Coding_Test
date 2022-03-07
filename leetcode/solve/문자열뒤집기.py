# 내 풀이
# 시간: 상위 40% / 메모리: 상위 30%
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:]=s[::-1]
       
      
# 내 풀이 2 => 투 포인터, 스왑
# 내 풀이 1과 유사
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
