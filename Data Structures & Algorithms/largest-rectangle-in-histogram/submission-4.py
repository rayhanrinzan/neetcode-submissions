class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0

        for rectangle_height in range(1, max(heights) + 1):
            current_area = 0

            for current_height in heights:
                if current_height >= rectangle_height:
                    current_area += rectangle_height
                    max_area = max(max_area, current_area)
                else:
                    current_area = 0

        return max_area