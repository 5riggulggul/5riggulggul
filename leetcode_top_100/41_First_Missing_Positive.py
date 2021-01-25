class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = {}
        ma = 0
        for i in range(len(nums)):
            dic[nums[i]] = 1
            if ma < nums[i]:
                ma = nums[i]
        for i in range(1,ma+2):
            if dic.get(i) == None:
                return i