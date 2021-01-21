class Solution:
    def longestValidParentheses(self, s: str) -> int:
        op = 0
        cl = 0
        result = 0
        for i in range(len(s)):
            if s[i] == "(":
                op += 1
            elif s[i] == ")":
                cl += 1
            if op == cl:
                if result < op + cl:
                    result = op + cl
            elif op < cl:
                op = 0
                cl = 0
                
        op = 0
        cl = 0
        for i in reversed(range(len(s))):
            if s[i] == "(":
                op += 1
            elif s[i] == ")":
                cl += 1
            if op == cl:
                if result < op + cl:
                    result = op + cl
            elif op > cl:
                op = 0
                cl = 0
                
        return result