# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 迭代法 实现合并两个有序链表"""
        dummy = l3 = ListNode(0,l1)
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l3.next = l1
                    l1 = l1.next  
                else:
                    l3.next = l2
                    l2 = l2.next
                l3 = l3.next
            elif l1:
                l3.next = l1
                l1 = None
            elif l2:
                l3.next = l2
                l2 = None
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """ 递归法 实现合并两个有序链表 """
        if l1 is None: 
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2