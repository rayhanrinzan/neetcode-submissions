class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        temp = self.nums
        temp.sort(reverse = True)
        return temp[self.k - 1]
        
