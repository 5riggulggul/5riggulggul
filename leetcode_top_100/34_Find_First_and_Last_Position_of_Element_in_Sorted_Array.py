class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        def firstend(m): #target 구간 인덱스 구하기
            li = m
            ri = m
            while True:
                if li == -1 or nums[li] != target:
                    li += 1
                    break
                li -= 1
            while True:
                if ri == len(nums) or nums[ri] != target:
                    ri -= 1
                    break
                ri += 1
            return [li,ri]

        while l <= r: #target 이진탐색
            m = (l + r) // 2
            print(l,m,r)
            if nums[m] == target:
                return firstend(m)
            elif nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
        return [-1,-1]
    
                    
