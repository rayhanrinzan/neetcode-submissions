class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dupe_map = {}
        for i in range (1, len(nums) + 1):
            dupe_map[i] = 0

        for num in nums:
            if dupe_map[num] == 0:
                dupe_map[num] = 1
            else:
                return num