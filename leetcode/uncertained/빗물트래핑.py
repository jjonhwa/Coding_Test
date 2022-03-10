# 내 풀이
# 속도: 상위 25% | 메모리: 상위 20%

class Solution:
    def trap(self, height: List[int]) -> int:
        max_idx = height.index(max(height)) # index of max value
        left_side = height[:max_idx+1]
        right_side = height[max_idx:]
        right_side.reverse()
        
        volumn = 0
        
        if left_side:
            max_left = 0
            for left in left_side:
                max_left = max(max_left, left)
                if max_left >= left:
                    volumn += max_left - left
                    
        if right_side:
            max_right = 0
            for right in right_side:
                max_right = max(max_right, right)
                if max_right >= right:
                    volumn += max_right - right
                
        return volumn
 
# 풀이 1
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volumn = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left < right: 
            left_max = max(height[left], left_max)
            right_max= max(height[right], right_max)
            
            if left_max <= right_max: # 이 부분에서 -> 최대치를 기준으로 더 이상 상대방으로 넘어가지 않게됨.
                volumn += left_max - height[left]
                left += 1
            else:
                volumn += right_max - height[right]
                right -= 1
        
        return volumn
