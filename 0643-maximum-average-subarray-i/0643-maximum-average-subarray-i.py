class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = right = 0
        window_sum = 0
        max_sum = -2147483648
        while right<len(nums):
            window_sum += nums[right]
            if right-left+1 == k:
                if max_sum < window_sum:
                    max_sum = window_sum
                window_sum -= nums[left]
                left+=1
            right +=1
        return max_sum/k