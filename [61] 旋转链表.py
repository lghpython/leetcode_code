# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next: return head
        dummy = ListNode(0,head)
        fast =slow = head
        count = 1
        while head.next:
            head = head.next
            count += 1
        k = k%count
        for i in range(k):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        fast.next = dummy.next
        dummy.next = slow.next 
        slow.next = None
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next: return head
        dummy = ListNode(0,head)
        cur = head
        count = 1
        while head.next:
            head = head.next
            count += 1
        k = k%count
        for i in range(count-k-1):
            cur = cur.next
        
        head.next = dummy.next
        dummy.next = cur.next 
        cur.next = None
        return dummy.next