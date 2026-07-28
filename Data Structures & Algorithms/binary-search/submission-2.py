class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right, target):
            mp = (left + right) // 2
            if target == nums[mp]:
                return(mp)
            if target == nums[left]:
                return(left)
            if target == nums[right]:
                return(right)
            if target > nums[mp]:
                return(binary_search(mp, right, target))
            return(binary_search(left, mp, target))

        l = 0
        r = len(nums) - 1
        if target not in nums:
            return -1
        return(binary_search(l, r, target))