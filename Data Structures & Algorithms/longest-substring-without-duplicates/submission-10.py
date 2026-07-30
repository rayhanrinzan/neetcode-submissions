class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lens = []
        seen = {}

        if len(s) == 0 or len(s) == 1:
            return(len(s))

        start = 0
        for i in range(len(s)):
            if i < start:
                continue
            elif i == len(s) - 1:
                if s[i] in seen and seen[s[i]] >= start:
                    print(s[start: i])
                    lens.append(i - start)
                else:
                    print(s[start: i + 1])
                    lens.append(i - start + 1)
            elif s[i] in seen and seen[s[i]] >= start:
                print(s[start: i])
                lens.append(i - start)
                start = seen[s[i]] + 1                
            seen[s[i]] = i
            
        print(lens)
        return(max(lens))

                
