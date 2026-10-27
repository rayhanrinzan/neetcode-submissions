class Node:
        def __init__(self, val = None, nxt = None):
            self.val = val
            self.next = nxt
class LinkedList:
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        curr = self.head
        curr_idx = 0
        while curr != None and curr_idx <= index:
            if curr_idx == index:
                return curr.val
            curr_idx += 1
            curr = curr.next
        return -1

    def insertHead(self, val: int) -> None:
        nxt = self.head
        self.head = Node(val, nxt)

    def insertTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val, None)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = Node(val, None)


    def remove(self, index: int) -> bool:
        if self.head == None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        curr_idx = 0
        curr = self.head
        while curr != None and curr_idx <= index:
            if curr_idx == (index - 1):
                if curr.next == None:
                    return False
                curr.next = curr.next.next
                return True
            curr = curr.next
            curr_idx += 1
        return False

    def getValues(self) -> List[int]:
        lst = []
        curr = self.head
        while curr != None:
            lst.append(curr.val)
            curr = curr.next
        return lst
        
