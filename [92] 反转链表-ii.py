#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        # if left == right: return head
        dummy= pre = ListNode(0, head)
        cur = head
        for i in range(1, right):
            if i == left-1 : pre = cur
            cur = cur.next
        tail = cur.next
        cur.next = None 
        self.reverseList(pre.next)
        pre.next.next = tail
        pre.next = cur
        return dummy.next

    def reverseList(self, head: ListNode) -> ListNode:
        """ 反转链表 """
        pre = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
# @lc code=end

