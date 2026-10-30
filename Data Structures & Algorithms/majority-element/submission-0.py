class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """lets solve this in O(1)"""
        candidate = nums[0]
        count = 0
        for num in nums:
            if num == candidate:
                count += 1
            else:
                count -= 1

            if count < 1:
                candidate = num
                count = 1
        return candidate
            
    

        