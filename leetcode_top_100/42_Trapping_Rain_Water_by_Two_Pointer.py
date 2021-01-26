class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        l = 0
        r = len(height) - 1
        max_l = 0
        max_r = 0
        
        while l < r:
            if height[l] < height[r]:
                if height[l] < max_l:
                    result += max_l - height[l]
                else:
                    max_l = height[l]
                l += 1
            else:
                if height[r] < max_r:
                    result += max_r - height[r]
                else:
                    max_r = height[r]
                r -= 1
        return result
                    