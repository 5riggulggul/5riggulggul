class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        if len(digits) == 0:
            return answer
        def recur(i,st):
            if i == len(digits):
                answer.append(st)
            else:
                k = int(digits[i])
                if k <= 6:
                    recur(i+1, st + chr(3*k+91))
                    recur(i+1, st + chr(3*k+92))
                    recur(i+1, st + chr(3*k+93))
                elif k == 7:
                    recur(i+1, st + chr(112))
                    recur(i+1, st + chr(113))
                    recur(i+1, st + chr(114))
                    recur(i+1, st + chr(115))
                elif k == 8:
                    recur(i+1, st + chr(116))
                    recur(i+1, st + chr(117))
                    recur(i+1, st + chr(118))
                elif k == 9:
                    recur(i+1, st + chr(119))
                    recur(i+1, st + chr(120))
                    recur(i+1, st + chr(121))
                    recur(i+1, st + chr(122))
                    

        recur(0,"")    
        return answer