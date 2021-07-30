# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """ 双指针法 耗时严重"""
        dummy = pre = ListNode(0, head)
        cur = head
        # pre = dummy if cur.val==cur.next.val else head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    print(cur)
                    cur = cur.next
                
            else:
                # pre 永远站在无重复的值的节点
                pre.next = cur
                pre = pre.next
            cur = cur.next
        else:
            pre.next = cur
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode: 
        """ 单指针遍历"""      
        dummy = cur = ListNode(0, head)
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                tmp = cur.next.val
                while cur.next and cur.next.val == tmp:
                    cur.next = cur.next.next
            else:
                cur = cur.next
 
        return dummy.next

