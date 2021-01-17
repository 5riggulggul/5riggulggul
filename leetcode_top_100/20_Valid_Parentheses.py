class Solution:
    def isValid(self, s: str) -> bool:
        tem = list()
        for i in range(len(s)):
            if s[i] is '[' or s[i] is '{' or s[i] is '(':
                tem.append(s[i])

            elif s[i] is ']':
                if not tem:
                    return False
                if tem[-1] is '[':
                    tem.pop()
                else: return False

            elif s[i] is '}':
                if not tem:
                    return False
                if tem[-1] is '{':
                    tem.pop()
                else: return False
                
            elif s[i] is ')':
                if not tem:
                    return False
                if tem[-1] is '(':
                    tem.pop()
                else: return False
        if tem:
            return False
        else : return True
        