class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        The key to understanding this problem is that whenever you split the
        list, one side is guaranteed to be sorted.
        If your target falls within the bounds of the sorted side, it is on
        the sorted side or not in the list at all,
        otherwise, it is on the unsorted side or just not in the list
        """
        l = 0
        h = len(nums) - 1
        while l <= h:
            if nums[l] == target:
                return l
            if nums[h] == target:
                return h
            mp = (l + h) // 2
            if nums[mp] == target:
                return mp
            # check if right is sorted and target on right
            if nums[mp] <= nums[h] and nums[mp] < target and target < nums[h]:
                l = mp + 1
            # check if left is sorted and target on left
            elif nums[l] <= nums[mp] and nums[mp] > target and target > nums[l]:
                h = mp
            elif nums[l] <= nums[mp]:
                l = mp + 1
            else:
                h = mp

        return -1

