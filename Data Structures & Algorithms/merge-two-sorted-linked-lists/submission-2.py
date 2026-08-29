# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def merge_recursive(list1, list2, merged_list):
            if list1 == None:
                merged_list.next = list2
                return head
            if list2 == None:
                merged_list.next = list1
                return head
            
            if list1.val <= list2.val:
                merged_list.next = list1
                list1 = list1.next
            else:
                merged_list.next = list2
                list2 = list2.next
            
            return merge_recursive(list1, list2, merged_list.next)

        # edge cases
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        # get head

        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        merged_list = head

        return merge_recursive(list1, list2, merged_list)



            





