class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        first, account for base cases
        we start with the minimum length possible
        left pointer at 0, right pointer at 1
        if the maximum recurring element in that substring has 
        gaps that are less than or equal
        to k, then the max is the length of that substring
        we can then increment the right pointer
        but how do we check every single substring?

        the best way of maintaining our character frequencies for each
        window so that we dont end up recalculating them for every loop
        iteration is to build our dictionary as we go
        every loop iteration, a single character (which would already be
        in our dict) is lost and a single character (which may or may 
        not already be in our dict) is added
        """

        if len(s) < 2:
            return(1)

        char_freqs = {}
        for i in range(2):
            if s[i] in char_freqs:
                char_freqs[s[i]] += 1
            else:
                char_freqs[s[i]] = 1

        l = 0
        r = 1
        curr_max = 0

        while r < len(s):
            max_freq = max(char_freqs.values())
            string = s[l:r+1]
            gaps = len(string) - max_freq
            if k >= gaps:
                if len(string) > curr_max:
                    curr_max = len(string)
                r += 1
                if r >= len(s):
                    break
                if s[r] not in char_freqs:
                    char_freqs[s[r]] = 1
                else:
                    char_freqs[s[r]] += 1

            else:
                char_freqs[s[l]] -= 1
                l += 1

        return curr_max
             


                
    


