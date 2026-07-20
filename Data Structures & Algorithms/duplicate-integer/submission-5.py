class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = list()
        for i in range(len(nums)):
            curr = nums[i];
            if curr in seen:
                return True;

            seen.append(curr);       

        return False;     

        