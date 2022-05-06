class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = [0] * len(nums)
        answer = []
        
        stack = []
        def dfs():
            
            if len(stack) == len(nums):
                answer.append(stack[:])
                return
            
            for i in range(len(nums)):
                if visited[i] == 1:
                    continue
                
                visited[i] = 1
                stack.append(nums[i])
                dfs()
                visited[i] = 0
                stack.pop()
                
        dfs()
        return answer
