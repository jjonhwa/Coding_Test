from typing import List

# 내 풀이
# 속도: 상위 30% | 메모리: 상위 40%
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        answer = 0
        for i in range(len(nums) // 2):
            answer += nums[2*i]
        return answer

# 정답 풀이
# 속도: 상위 5% | 메모리: 상위 70%
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

