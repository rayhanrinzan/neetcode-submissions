class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        curr_idx = 0
        while curr != None and curr_idx <= index:
            if curr_idx == index:
                return curr[0]
            curr_idx += 1
            curr = curr[1]
        return -1

    def insertHead(self, val: int) -> None:
        nxt = self.head
        self.head = [val, nxt]

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = [val, None]
        else:
            curr = self.head
            while curr[1] != None:
                curr = curr[1]
            curr[1] = [val, None]


    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        if index == 0:
            self.head = self.head[1]
            return True
        curr_idx = 0
        curr = self.head
        while curr != None and curr_idx <= index:
            if curr_idx == (index - 1):
                if curr[1] == None:
                    return False
                curr[1] = curr[1][1]
                return True
            curr = curr[1]
            curr_idx += 1
        return False

    def getValues(self) -> List[int]:
        lst = []
        curr = self.head
        while curr != None:
            lst.append(curr[0])
            curr = curr[1]
        return lst
        
