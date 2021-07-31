# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        dummy = pre = ListNode(0,head)
        cur = head
        while cur and cur.next:

            if cur.next.val >= x and cur.val < x:
                pre  = cur
                cur = cur.next
            elif cur.next.val <x and cur.val >=x:
                tmp = pre.next        
                pre.next = cur.next
                cur.next=cur.next.next
                pre = pre.next
                pre.next = tmp
            elif cur.next.val>=x and cur.val >=x:
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return dummy.next
            