class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_ones = 0
        for i in range(len(nums)):
            if i+1 == len(nums) and nums[i] == 1:
                curr_ones += 1
                if curr_ones > max_ones:
                    max_ones = curr_ones
                curr_ones = 0
            if nums[i] == 0:
                if curr_ones > max_ones:
                    max_ones = curr_ones
                curr_ones = 0
            else:
                curr_ones += 1

        return max_ones

