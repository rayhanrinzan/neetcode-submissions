# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode()
        l3_head = l3
        carry = 0
        while l1 != None or l2 != None:
            if l1 == None:
                l1 = ListNode()
            if l2 == None:
                l2 = ListNode()
            need_to_add = l1.val + l2.val + carry
            print(l1.val, l2.val)
            if need_to_add > 9:
                l3.val = need_to_add - 10
                carry = 1
            else:
                l3.val = need_to_add
                carry = 0
            l3.next = ListNode()
            if l1.next == None and l2.next == None:
                if carry == 1:
                    l3.next.val = 1
                    l3.next.next = None
                else:
                    l3.next = None
            else:
                l3 = l3.next
            l1 = l1.next
            l2 = l2.next


        return l3_head
        