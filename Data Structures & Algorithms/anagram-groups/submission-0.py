class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def is_anagram(str_1, str_2):
            str_1 = list(str_1)
            if len(str_1) != len(str_2):
                return False
            for char in str_2:
                if char in str_1:
                    str_1.remove(char)
                else:
                    return False
            if len(str_1) == 0:
                return True
            return False
        
        anagrams = [[strs[0]]]
        strs.remove(strs[0])

        for str1 in strs:
            appended = False
            for anagram_list in anagrams:
                str2 = anagram_list[0]
                if is_anagram(str1, str2):
                    print("got it")
                    anagram_list.append(str1)
                    appended = True
            if appended == False:
                anagrams.append([str1])

        return anagrams



            
                

