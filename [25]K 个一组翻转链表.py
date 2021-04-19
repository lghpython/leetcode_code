# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        l = r = start = head
        dummy = pre = ListNode(0, head)
        # k 个节点为一组， 每组第一个指针l， 最后一个指针 r , start保存下一组第一个指针
        while start:
            for i in range(k):
                if not start: # 单小组节点不足k个时，不做反转
                    pre.next = l
                    return dummy.next
                if i == k-1:  # 设置分组右边界
                    r = start
                start = start.next
        
            r.next = None  # 每个小组切割，单独做反转
            # 衔接k个反转后的链表
            pre.next = self.reverseList(l)
            pre = l  # 小组的第一个节点衔接下一个小组
            l = r = start # l r 初始化到下组
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


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        zero = ListNode(0)
        zero.next = head
        tail = zero
        pre = zero
        count = 0
        while tail:
            count += 1
            tail = tail.next
            if not tail: break
            if count % k == 0:
                head = pre.next
                # 当前指针插入tail后面
                while pre.next != tail:
                    cur = pre.next
                    pre.next = cur.next
                    cur.next = tail.next
                    tail.next = cur
                pre = head
                tail = head
        return zero.next