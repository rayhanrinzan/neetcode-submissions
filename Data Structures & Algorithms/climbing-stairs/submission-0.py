class Solution:
    def climbStairs(self, n: int) -> int:
        stairs_dict = {}
        def climb_stairs_recursive(n, stairs_dict):
            if n == 0 or n == 1 or n == 2:
                return(n)
            if n-2 not in stairs_dict:
                stairs_dict[n-2] = climb_stairs_recursive(n-2, stairs_dict)
            if n-1 not in stairs_dict:
                stairs_dict[n-1] = climb_stairs_recursive(n-1, stairs_dict)
            return(stairs_dict[n-2] + stairs_dict[n-1])
        
        return(climb_stairs_recursive(n, stairs_dict))