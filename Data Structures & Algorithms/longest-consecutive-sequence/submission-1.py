class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def one_less(count, nums, num):
            while num in nums:
                nums.remove(num)
            if num-1 in nums:
                count += 1                    
                return one_less(count, nums, num - 1)
            else:
                return count

        if len(nums) < 1:
            return(0)
        count_list = []
        start = max(nums)
        while len(nums) > 0: 
            count_list.append(one_less(1, nums, start))
            if len(nums) > 0:
                start = max(nums)
            else:
                break
        print(count_list)
        return(max(count_list))
            