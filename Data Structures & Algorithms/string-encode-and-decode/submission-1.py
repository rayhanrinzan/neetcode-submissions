class Solution:

    def encode(self, strs: List[str]) -> str:
        final_string = ""
        for string in strs:
            for char in string:
                num = ord(char)
                char = chr(num+1)
                final_string += char
            final_string += "ë"
        return(final_string)


    def decode(self, s: str) -> List[str]:
        word_list = []
        word = ""
        for char in s:
            if char == "ë":
                word_list.append(word)
                word = ""
            else:
                num = ord(char)
                char = chr(num-1)
                word += char
        return(word_list)



