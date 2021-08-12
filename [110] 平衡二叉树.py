#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(root):
            if not root: return 0
            return max(dfs(root.left), dfs(root.right))+1
        if not root:return True
        return abs(dfs(root.left)-dfs(root.right)) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)
# @lc code=end

