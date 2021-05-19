# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = cur = head
        while cur and cur.next:
            cur = cur.next
            if cur.val == pre.val:
                pre.next = cur.next
            else:
                pre = pre.next
        return head

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """ 判断索引，最大索引是否出界"""
        maxi =0
        for i,n in enumerate(nums):
            if i+n>maxi and maxi>=i:
                maxi = i+n
            # if maxi<i:return False
        return maxi>=i