# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """ 递归法 """
        if not head or not head.next: return head
        cur = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return cur