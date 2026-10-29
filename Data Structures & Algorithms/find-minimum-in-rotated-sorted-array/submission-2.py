class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        
        next_l = 0
        next_l = len(nums) - 1

        while l <= h:
            mp = (l + h) // 2
            if nums[mp] == nums[h]:
                return nums[l]
            if nums[mp] > nums[h]:
                l = mp + 1
            else:
                h = mp






