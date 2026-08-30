# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_length(linked_list):
            counter = 0
            while linked_list:
                counter += 1
                linked_list = linked_list.next
            return counter

        temp = head
        delete_index = get_length(temp) - n

        i = 0
        prev = None
        curr = head
        while curr:
            if i == delete_index:
                #removal logic
                if prev:
                    prev.next = curr.next
                else:
                    head = curr.next
            else:
                prev = curr
            curr = curr.next
            i += 1

        return head
        