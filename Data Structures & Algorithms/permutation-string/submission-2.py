class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check_perm(s, segment):
            s, segment = sorted(s), sorted(segment)
            s, segment = "".join(s), "".join(segment)
            if s == segment:
                return True
            return False
            
        if len(s2) < len(s1):
            return False
        l = len(s1)
        for i in range(0, len(s2) - len(s1) + 1):
            segment = s2[i: i + len(s1)]
            s = s1
            print(segment)
            if check_perm(s, segment):
                return True
            
        return False
