# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        mp = n // 2
        h = n
        l = 0
        if guess(n) == 0:
            return n
        while guess(mp) != 0:
            if guess(mp) == -1:
                temp = mp
                mp =  (mp + l) // 2
                h = temp
            else:
                temp = mp
                mp = (h + mp) // 2
                l = temp + 1
        return mp



        