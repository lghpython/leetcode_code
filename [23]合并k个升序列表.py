# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ reduce方法 迭代合并 速度较慢"""
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists: return
        if len(lists) == 1:
            return lists[0]

        def mergelists(l1, l2):
            dummy = l3 = ListNode(0, l1)
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
        return reduce(mergelists, lists)



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """ 二分法 迭代合并"""
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        dummy = l3 = ListNode(0, l1)
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
    """ 二分法 迭代合并"""
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:return 
        n = len(lists)
        return self.merge(lists, 0, n-1)
    def merge(self,lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)
    def mergeTwoLists(self,l1, l2):
        if not l1:return l2
        if not l2:return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next
