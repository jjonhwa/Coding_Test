# 속도: 663ms
# 메모리: 16MB
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        nums = [i+1 for i in range(n)]
        
        answer = []
        
        stack = []
        
        def dfs(nums):
            if len(stack) == k:
                answer.append(stack[:])
                return
            
            for i in range(len(nums)):
                stack.append(nums[i])
                dfs(nums[i+1:])
                stack.pop()
        
        dfs(nums)
        return answer
