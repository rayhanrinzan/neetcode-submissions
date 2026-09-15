class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) >= 0:
            stones.sort(reverse = True)
            if len(stones) == 0:
                return 0
            if len(stones) == 1:
                return stones[0]

            if stones[1] < stones[0]:
                stones[1] = stones[0] - stones[1]
                stones = stones[1:]
            
            else:
                stones = stones[2:]

            
            
        