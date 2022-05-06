class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        answer = []

        def dfs(k, idx, stack):
            if sum(stack) > target:
                return
            if sum(stack) == target:
                answer.append(stack)
                return
            
            for i in range(idx, len(candidates)):
                dfs(k+candidates[i], i, stack+[candidates[i]])
                
        dfs(0, 0, [])
        return answer
                
