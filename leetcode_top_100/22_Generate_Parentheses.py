class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        temp = []
        result =[]
        def recur(a,b,at):
            if a > 0:
                temp.append('(')
                recur(a-1,b,at+1)
                temp.pop()
            if b > 0 and at > 0:
                temp.append(')')
                recur(a,b-1,at-1)
                temp.pop()
            if a == 0 and b == 0:
                result.append(''.join(temp))
        recur(n,n,0)
        return result