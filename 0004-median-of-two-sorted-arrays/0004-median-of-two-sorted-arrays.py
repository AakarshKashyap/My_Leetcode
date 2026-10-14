class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        while left <= right:
            partition1 = (left + right)//2
            partition2 = (m+n+1)//2 - partition1
            maxleft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minright1 = float('inf') if partition1 == m else nums1[partition1]
            maxleft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minright2 = float('inf') if partition2 == n else nums2[partition2]
            if maxleft1 <= minright2 and maxleft2 <= minright1:
                if (m+n)%2 == 0:
                    return (max(maxleft1, maxleft2) + min(minright1, minright2))/2.0
                else: 
                    return float(max(maxleft1, maxleft2))
            elif maxleft1 > minright2:
                right = partition1 - 1
            else:
                left = partition1 + 1
        return 0.0
        