class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i] == nums[j] and i<j:
                    count += 1
        return count
        