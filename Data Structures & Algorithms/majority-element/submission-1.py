class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """lets solve this in O(1)"""
        candidate = nums[0]
        count = 0
        for num in nums:
            count = count + 1 if num == candidate else count - 1
            if count < 1:
                candidate = num
                count = 1
        return candidate
            
    

        