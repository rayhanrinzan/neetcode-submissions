class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {};
        t_map = {};
        for i in range(len(s)):
            if s[i] in s_map:
                s_map[s[i]] += 1;
            else:
                s_map[s[i]] = 1;
        for i in range(len(t)):
            if t[i] in t_map:
                t_map[t[i]] += 1;
            else:
                t_map[t[i]] = 1;
        if len(t) > len(s):
            for key in t_map:
                if key not in s_map:
                    return False;
                if s_map[key] != t_map[key]:
                    return False;
        else:
            for key in s_map:
                if key not in t_map:
                    return False;
                if s_map[key] != t_map[key]:
                    return False;
        return True;

