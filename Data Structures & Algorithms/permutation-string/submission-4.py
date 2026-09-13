class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check_perm(s, segment):
            for char in s:
                if char in segment:
                    segment = segment.replace(char, "", 1)
            if len(segment) > 0:
                return False
            return True
            
        if len(s2) < len(s1):
            return False
        l = len(s1)
        for i in range(0, len(s2) - len(s1) + 1):
            segment = s2[i: i + len(s1)]
            s = s1
            if check_perm(s, segment):
                return True
            
        return False
