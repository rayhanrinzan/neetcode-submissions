class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)):
            l, r = 0, len(nums)-1
            while l < r:
                if i == l or i == r:
                    break
                triplet = [nums[i], nums[l], nums[r]]
                triplet.sort()
                total = sum(triplet)
                if total == 0 and triplet not in triplets:
                    triplets.append(triplet)
                
                if total <= 0:
                    l += 1
                else:
                    r -= 1            

        return(triplets)

                    
        