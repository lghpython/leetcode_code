#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        queue = []
        while head:
            queue.append(head.val)
            head = head.next
        n = len(queue)
        def dfs(l,r):
            if l>=r : return None
            i = (l+r)//2
            return TreeNode(queue[i],dfs(l,i), dfs(i+1,r))

        return dfs(0,n)
# @lc code=end

