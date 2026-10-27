# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        for i in range(len(pairs)):
            key, val = pairs[i].key, pairs[i].value
            curr = i
            while (curr - 1) > -1 and pairs[curr-1].key > key:
                curr -= 1
            if curr != i:
                temp = pairs.pop(i)
                pairs.insert(curr, temp)

            pairs_state = pairs.copy()
            states.append(pairs_state)
        return states
        

            
        