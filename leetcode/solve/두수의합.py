# 첫 풀이
# 브루트포스
# 속도: 하위 15% | 메모리: 상위 25%
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 풀이 2
# in을 이용한 탐색
