class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        here1 = 0
        here2 = 0
        ind = 0 #밑에 if문에서 ind가 나중에 증가하므로 while문이 ind가 0 ~ 중간번째 수 -1 까지 작동하게 한다.
        result = 0
        nums1.append(1000000) #len 길이 넘어갈 경우를 위해 모든 수보다 큰 값을 끝에 넣어놓는다.
        nums2.append(1000000)
        if len(nums1) == 0: #왼쪽 배열이 크기가 0인 경우 (nums[here1]이 존재하지 않으므로 따로 경우를 만들어줌)
            if len(nums2) % 2 == 1:
                return nums2((len(nums2)-1)/2)
            else :
                return (nums2((len(nums2)/2)) + nums2((len(nums2)/2)-1)) / 2
        elif len(nums2) == 0: #오른쪽 배열의 크기가 0인 경우
            if len(nums1) % 2 == 1:
                return nums1((len(nums1)-1)/2)
            else :
                return (nums1((len(nums1)/2)) + nums1((len(nums1)/2)-1)) / 2
        
        if total % 2 == 1: #총 길이가 홀수인 경우 (중간값 하나만 찾으면 됨)
            while ind != (total + 1) / 2:
                if nums1[here1] <= nums2[here2]:
                    ind += 1
                    result = nums1[here1]
                    here1 += 1
                else:
                    ind += 1
                    result = nums2[here2]
                    here2 += 1
            return result
        else: #총 길이가 짝수인 경우 (중간값 두개 평균 내야함)
            while ind != (total / 2):
                if nums1[here1] <= nums2[here2]:
                    ind += 1
                    result = nums1[here1]
                    here1 += 1
                else:
                    ind += 1
                    result = nums2[here2]
                    here2 += 1
            if nums1[here1] <= nums2[here2]:
                result += nums1[here1]
            else:
                result += nums2[here2]
            return result / 2
            
            