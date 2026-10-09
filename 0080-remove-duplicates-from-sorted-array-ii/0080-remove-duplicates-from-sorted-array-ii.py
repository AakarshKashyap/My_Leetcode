class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        write = 1
        for read in range(2, len(nums)):
            if nums[read] != nums[write-1]:
                write += 1
                nums[write] = nums[read]
        return write +1

                