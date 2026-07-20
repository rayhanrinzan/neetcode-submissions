class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num1 = nums[i]
            for j in range(len(nums)):
                num2 = nums[j]
                if i != j and num1+num2 == target:
                    return([i,j])
                    
