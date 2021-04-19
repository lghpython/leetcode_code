# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = head
        if not head: return 
        cur = head.next
        dummy = ListNode(0, head)
        while cur:
            pre.val, cur.val = cur.val,  pre.val
            if cur.next and cur.next.next:
                pre = cur.next
                cur = cur.next.next
            else: 
                break
        return dummy.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy= cur = ListNode(0, head)
        while cur.next and cur.next.next:
            cur.next.val, cur.next.next.val = cur.next.next.val,  cur.next.val
            cur = cur.next.next
        return dummy.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        head.val,head.next.val = head.next.val, head.val
        head.next.next = self.swapPairs(head.next.next)
        return head

"""以上交换节点的值  以下是交换节点 """

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy = pre =ListNode(0, head)
        cur = head.next
        while cur:
            pre.next.next = cur.next
            cur.next = pre.next
            pre.next = cur

            if cur.next.next and cur.next.next.next:
                pre = cur.next
                cur =  cur.next.next.next
            else:
                break
        return dummy.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy= pre = ListNode(0, head)
        cur = head
        while cur and cur.next:
            pre.next = cur.next 
            cur.next= cur.next.next 
            pre.next.next =cur 
            
            pre = cur
            cur = cur.next or None
        return dummy.next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: 
            return head
        newhead = head.next
        head.next = self.swapPairs(newhead.next)
        newhead.next = head
        return newhead