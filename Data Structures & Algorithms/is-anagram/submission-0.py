class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False;
        s_list = list(s)
        t_list = list(t)
        for i in range(len(s_list)):
            char = s_list[i];
            if char in t_list:
                t_list.remove(char);

        if len(t_list) == 0:
            return True

        return False;
