class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in range(len(nums)):
            curr = nums[i];
            if curr in seen:
                return True;

            seen.add(curr);       

        return False;     

        