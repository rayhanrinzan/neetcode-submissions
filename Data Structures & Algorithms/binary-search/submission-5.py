class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low, high, target):
            mp = (low + high) // 2
            if target == nums[low]:
                return(low)
            if target == nums[high]:
                return(high)
            if target == nums[mp]:
                return(mp)
            if target > nums[mp]:
                return(binary_search(mp, high, target))
            return(binary_search(low, mp, target))

        l, h = 0, len(nums)-1
        if target not in nums:
            return -1
        return(binary_search(l, h, target))