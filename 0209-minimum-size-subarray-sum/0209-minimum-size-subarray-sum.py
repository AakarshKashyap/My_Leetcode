class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        sum_of_nums = 0
        min_len = float('inf')
        while right<len(nums):
            sum_of_nums += nums[right]
            while sum_of_nums>=target:
                length = right-left+1
                min_len = min(length, min_len)
                sum_of_nums-=nums[left]
                left += 1
            right += 1
        if min_len == float('inf'):
            return 0
        return min_len
