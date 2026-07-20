class Solution:
    def isPalindrome(self, s: str) -> bool:
        def word_flipper(word):
            new_word = ""
            i = len(word)-1
            while i > -1:
                new_word += word[i]
                i -= 1
            return(new_word)
        def make_alpha(word):
            new_word = ""
            for char in word:
                if char.isalnum():
                    new_word += char
            return(new_word)
        if make_alpha(s).lower() == make_alpha(word_flipper(s)).lower():
            return(True)
        return(False)
        