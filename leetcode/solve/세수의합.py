# 내 풀이
# 속도: 하위 20% | 메모리: 상위 10%
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        stack = set()
        for i in range(len(nums)-2):
            threshold = nums[i]
            
            start, end = i+1, len(nums)-1
            while start < end:
                if nums[start] + nums[end] + threshold > 0:
                    end -= 1
                elif nums[start] + nums[end] + threshold < 0:
                    start += 1
                else:
                    ans = [nums[start], nums[end], threshold]
                    ans.sort()
                    ans = tuple(ans)
                    stack.add(ans)
                    
                    end -= 1
                    start += 1
        
        return stack
      
  
# 내 풀이 - 수정
# 연속된 기준점이 똑같을 경우에 대해서만 continue로 처리해줘도 시간이 절반 이상으로 줄어든다.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = set()
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # 역속된 기준점이 똑같을 경우 continue
                continue
                
            threshold = nums[i]
            
            start, end = i+1, len(nums)-1
            while start < end:
                if nums[start] + nums[end] + threshold > 0:
                    end -= 1
                elif nums[start] + nums[end] + threshold < 0:
                    start += 1
                else:
                    ans = [nums[start], nums[end], threshold]
                    ans.sort()
                    ans = tuple(ans)
                    stack.add(ans)
                    
                    end -= 1
                    start += 1
        
        return stack
      
# 정답 풀이
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        stack = []
        
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: # 역속된 기준점이 똑같을 경우 continue
                continue
                
            threshold = nums[i]
            
            start, end = i+1, len(nums)-1
            while start < end:
                summation = nums[start] + nums[end] + threshold
                if summation > 0:
                    end -= 1
                elif summation < 0:
                    start += 1
                else:
                    stack.append((nums[start], nums[end], threshold))
                    
                    # 여기서 중복값 제거
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                        
                    end -= 1
                    start += 1
        
        return stack
