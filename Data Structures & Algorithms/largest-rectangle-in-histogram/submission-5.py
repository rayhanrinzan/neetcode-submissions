class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        areas = []
        max_heights = max(heights)
        for i in range(max_heights + 1):
            area = 0
            max_height = i
            for i, curr_height in enumerate(heights):
                if curr_height >= max_height:
                    area += max_height
                    if i == len(heights)-1:
                        areas.append(area)
                else:
                    areas.append(area)
                    area = 0
        return(max(areas))
                
                
                



        