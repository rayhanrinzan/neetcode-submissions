class Deque:
    
    def __init__(self):
        self.queue = []

    def isEmpty(self) -> bool:
        if len(self.queue) == 0:
            return True
        return False

    def append(self, value: int) -> None:
        self.queue.append(value)
        
    def appendleft(self, value: int) -> None:
        self.queue.insert(0, value)

    def pop(self) -> int:
        try:
            return self.queue.pop()
        except:
            return -1

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.queue[0]
        self.queue = self.queue[1::]
        return first
