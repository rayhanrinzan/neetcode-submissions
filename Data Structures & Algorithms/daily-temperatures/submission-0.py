class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            temp1 = temperatures[i]
            count = 0
            for j in range(i, len(temperatures)):
                temp2 = temperatures[j]
                if j == len(temperatures)-1 and temp2 <= temp1:
                    result.append(0)
                if temp2 > temp1:
                    result.append(count)
                    break
                count += 1
        return(result)
