# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_recursive(curr, prev):
            if curr == None:
                return prev
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            return reverse_list_recursive(nxt, prev)

        prev, curr = None, head
        return(reverse_list_recursive(curr, prev))
        