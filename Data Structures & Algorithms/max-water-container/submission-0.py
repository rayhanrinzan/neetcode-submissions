# two pointers, store all the area values
# move the pointer at the smaller bar height inwards
# and also decrease width by 1
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        width = len(heights) - 1
        areas = []
        while l < r:
            if heights[l] > heights[r]:
                areas.append(width * heights[r])
                r -= 1
            else:
                areas.append(width * heights[l])
                l += 1
            width -= 1
        print(areas)
        return(max(areas))

        