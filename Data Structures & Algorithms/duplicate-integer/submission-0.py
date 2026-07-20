class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = nums.copy();
        for i in range(len(nums)):
            curr = nums[i];
            duplicate.remove(curr);
            if curr in duplicate:
                return True;
            
        return False
            
        