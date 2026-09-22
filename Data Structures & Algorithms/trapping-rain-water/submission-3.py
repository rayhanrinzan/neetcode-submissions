class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Brute force: create a 2d array where filled positions = 0 and 
        empty positions = 1; iterate through that array and for each 
        position find if it can be filled

        Other idea: we can modify the array as we go, turning the water
        walls. there is no need to treat the water any differently from
        the walls, so we can fill in wherever water can exist. 

        I like the second approach the best.

        We just need to track how much "water" we add to each index of
        our array. How do we keep track of this?: a "count" variable.
        How do we know if water can be added to an index of our array?:
        There is elevation (a higher value) in the indexes to the 
        left or the right. Water can be added up to the second highest
        index in the list that the current index is between.

        We can use left and right pointers to track the largest left and
        right indices, and add water as we keep moving inwards.
        """
        if len(height) < 3:
            return 0

        l, r = 0, len(height) - 1

        left_wall = 0
        right_wall = 0
        count = 0
        while l < r:
            if height[l] > left_wall:
                left_wall = height[l]
            if height[r] > right_wall:
                right_wall = height[r]

            lower = min(left_wall, right_wall)

            if height[l] < lower:
                temp = height[l]
                height[l] += lower - height[l]
                count += lower - temp
            if height[r] < lower:
                temp = height[r]
                height[r] += lower - height[r]
                count += lower - temp

            if height[r] > height[l]:
                l += 1
            else:
                r -= 1



        if l == r:
            if height[l] < lower:
                height[l] += lower - height[l]
                count += lower - height[r]

        return count






        
        