class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        box = {}
        maxi = 0
        if len(s) == 0:
            return maxi
        while right != len(s):
            if s[right] not in box:
                box[s[right]] = right
            else:
                if left < box[s[right]] + 1:
                    left = box[s[right]] + 1
                box[s[right]] = right
            if (right - left + 1) > maxi:
                    maxi = right - left + 1
            right += 1
        return maxi