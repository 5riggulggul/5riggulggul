# 브루트 포스 O(n^2)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        for i in range(len(height)):
            for j in range(i,len(height)):
                if maxi < (j-i)*min(height[i],height[j]):
                    maxi = (j-i)*min(height[i],height[j])
        
        return maxi '''

# 2 index pointer O(n)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        left = 0
        right = len(height) - 1
        while left != right:
            if maxi < (right-left)*min(height[left],height[right]):
                maxi = (right-left)*min(height[left],height[right])
            if height[left] <= height[right]:
                left += 1
            else: right -= 1
        
        return maxi
