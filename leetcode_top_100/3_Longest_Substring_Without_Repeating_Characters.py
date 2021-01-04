class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        maxi = 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        box = {s[0]:0}
        while right != (len(s)):
            if left == right:
                right += 1
            else:
                if s[right] not in box:
                    box[s[right]] = right
                    if (right - left + 1) > maxi:
                        maxi = right - left + 1
                    right += 1
                else:
                    left = box[s[right]] + 1
                    box[s[right]] = right
                    right += 1
        return maxi