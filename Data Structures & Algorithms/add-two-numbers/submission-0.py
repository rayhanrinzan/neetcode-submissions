# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def get_num(l):
            nums = []
            while l:
                nums.insert(0, str(l.val))
                l = l.next
            return int("".join(nums))

        def to_list(num):
            nums = list(str(num))
            nums.reverse()
            head = ListNode(nums[0])
            curr = head
            for i in range(1, len(nums)):
                curr.next = ListNode(nums[i])
                curr = curr.next
            return head

        new_num = get_num(l1) + get_num(l2)
        print(new_num)
        return to_list(new_num)


        

        