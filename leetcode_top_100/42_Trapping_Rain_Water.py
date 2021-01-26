class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        ma = max(height)
        result = 0
        for i in range(1,ma+1):
            for j in range(len(height) - 1):
                l = 0
                r = 0
                if height[j] >= i and height[j+1] < i:
                    l = j+1
                    for k in range(j+1,len(height)-1):
                        if height[k] < i and height[k+1] >= i:
                            r = k
                            result += r - l + 1
                            break
        return result

        #밑 줄부터 한줄씩 갇혀있는 부분 계산하는 방법
        #높이가 클 경우 시간이 오래걸려서 시간초과 발생
                        