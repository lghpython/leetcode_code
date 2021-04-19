# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """删除链表的倒数第n个节点 之 链表长度 """
        pre = cur = ListNode(0, head)
        count = 0
        while head:
            head = head.next
            count += 1

        for i in range(count-n):
            pre = pre.next
        pre.next = pre.next.next
        return cur.next



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """删除链表的倒数第n个节点 之 双指针 """
        first = head
        dummy = second = ListNode(0, head)

        for i in range(n):
            first = first.next

        while first:
            first = first.next
            second = second.next
        second.next = second.next.next

        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """删除链表的倒数第n个节点 之 栈实现 """
        # first = head
        # dummy = second = ListNode(0, head)

        # for i in range(n):
        #     first = first.next

        # while first:
        #     first = first.next
        #     second = second.next
        # second.next = second.next.next

        # return dummy.next

        dummy = ListNode(0, head)
        cur = dummy
        stack = []

        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n):
            stack.pop()
        
        pre = stack[-1]
        pre.next = pre.next.next
        return dummy.next