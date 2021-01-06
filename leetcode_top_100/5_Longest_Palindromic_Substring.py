class Solution:
    def longestPalindrome(self, s: str) -> str:
        mbox= [0] * 1001
        maxi = 1
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s
            else: return s[0]
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                box = [0]*1001
                cnt = 1
                k = i
                l = i+2
                box[k+1] = 1
                while k>=0 and l<=(len(s)-1):
                    if s[k] == s[l]:
                        cnt += 2
                        box[k] = 1
                        box[l] = 1
                        k -= 1
                        l += 1
                    else: break
                if maxi < cnt:
                    mbox = box[:]
                    maxi = cnt
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                box = [0]*1001
                cnt = 0
                k = i
                l = i+1
                box[k+1] = 1
                while k>=0 and l<=(len(s)-1):
                    if s[k] == s[l]:
                        cnt += 2
                        box[k] = 1
                        box[l] = 1
                        k -= 1
                        l += 1
                    else: break
                if maxi < cnt:
                    mbox = box[:]
                    maxi = cnt
        result = []
        for i in range(len(s)):
            if mbox[i] == 1:
                result.append(s[i])
        if len(result) == 0:
            return s[0]
        return ''.join(result)