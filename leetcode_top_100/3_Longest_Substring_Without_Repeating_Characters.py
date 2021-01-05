class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 #구간의 left index
        right = 0 #구간의 right index
        box = {} #구간에 존재하는 알파벳 : 가장 최근에 마주쳤을 때의 index
        maxi = 0 # 구간 길이 최댓값
        if len(s) == 0:
            return maxi
        while right != len(s):
            if s[right] not in box: #처음보는 알파벳일 경우
                box[s[right]] = right
            else: #알파벳 재출현의 경우
                if left < box[s[right]] + 1: #전의 알파벳 index가 left작으면 구간에 어차피 포함x -> left 그대로
                    left = box[s[right]] + 1
                box[s[right]] = right
            if (right - left + 1) > maxi:
                    maxi = right - left + 1
            right += 1
        return maxi