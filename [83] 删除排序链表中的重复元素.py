# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = cur = head
        while cur and cur.next:
            cur = cur.next
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = pre.next
        return head