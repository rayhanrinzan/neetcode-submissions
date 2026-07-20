class Solution:
    def isValid(self, s: str) -> bool:
        def is_open(char):
            if char == "{" or char == "(" or char == "[":
                return(True)
        
        need_next = []
        for char in s:
            if is_open(char):
                if char == "{":
                    need_next.append("}")
                if char == "[":
                    need_next.append("]")
                if char == "(":
                    need_next.append(")")
            else:
                if len(need_next) > 0:
                    needed_char = need_next.pop()
                else:
                    return(False)

                if needed_char != char:
                    print(char, needed_char)
                    return(False)

        if len(need_next) != 0:
            return(False)

        return(True)
        
        
         



        