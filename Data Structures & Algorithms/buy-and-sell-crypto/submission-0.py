# strategy: calculate all of the profits, storing each increment 
# in order to reduce time complexity, then choose the max of all
# calculated profits
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profs = [0]
        for i in range(0, len(prices) - 1):
            for j in range(i+1, len(prices)):
                profs.append(prices[j] - prices[i])
                print(prices[i], prices[j])
        max_prof = max(profs)
        return(max_prof)           