class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """binary search on a range:
        find lower bound, upper bound,
        search range using function

        lets try brute force first

        we need to find the LOWEST valid eating speed
        therefore, we can start at a lower bound, and work
        upwards until we find a valid speed
        so we will need a function checking if an eating
        speed is valid
        we now have this. 
        we can use the largest pile size as the upper bound, 
        since the largest pile size means Koko will eat each pile in 1 hour
        """
        def valid_speed(s):
            total_hours_taken = 0
            for pile in piles:
                hours_to_eat = pile // s + (0 if pile % s == 0 else 1)
                total_hours_taken += hours_to_eat
            if total_hours_taken <= h:
                return True
            return False
        
        valid_speeds = []
        
        low = 1
        high = max(piles)

        while low <= high:
            mp = (low + high) // 2
            if valid_speed(mp):
                valid_speeds.append(mp)
                high = mp - 1
            else:
                low = mp + 1

        valid_speeds.sort()
        print(valid_speeds)
        return valid_speeds[0]
        



            