# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            # save the new current node to not be altered
            nxt = curr.next

            #make the previous node the next of the current node
            curr.next = prev

            # set the previous node to now be the current node
            prev = curr

            # skip to the new current node
            curr = nxt

        return prev


        







            
        