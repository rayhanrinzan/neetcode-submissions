class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def perform_operation(num1, num2, op):
            if op == "+":
                num = num1+num2
            elif op == "-":
                num = num1-num2
            elif op == "*":
                num = num1*num2
            elif op == "/":
                num = int(num1/num2)
            return(num)
        
        if len(tokens) == 1:
            return(int(tokens[0]))
        
        next_nums = []
        next_ops = []

        for token in tokens:
            if token == '+' or token == '-' or token == '*' or token == '/':
                element2 = int(next_nums.pop())
                element1 = int(next_nums.pop())
                next_nums.append(perform_operation(element1, element2, token))
            else:
                next_nums.append(token)
            

        return(next_nums[0])