class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_dict = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }
        
        answer = []
        
        if not digits:
            return answer
                
        check = []
        def dfs(idx):
            if len(check) == len(digits):
                answer.append(''.join(check))
                return
            
            num = digits[idx]
            for alpha in phone_dict[num]:
                check.append(alpha)
                idx += 1
                dfs(idx)
                idx -= 1
                check.pop()
        
        dfs(0)
        
        return answer
