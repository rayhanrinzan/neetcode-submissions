class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        sum = -1001
        while sum != target and left != right:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            if sum > target:
                right -= 1
        return([left+1, right+1])