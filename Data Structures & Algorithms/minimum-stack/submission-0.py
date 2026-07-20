class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        popped = self.stack[len(self.stack)-1]
        del self.stack[len(self.stack)-1]
        return(popped)

    def top(self) -> int:
        return(self.stack[len(self.stack)-1])

    def getMin(self) -> int:
        minimum = self.stack[0]
        for num in self.stack:
            if num < minimum:
                minimum = num
        return minimum
            

        
