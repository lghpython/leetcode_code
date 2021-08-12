#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
         if inorder:
            rootv = preorder.pop(0)
            mid = inorder.index(rootv)
            root = TreeNode(rootv)
            root.left=self.buildTree(preorder,inorder[:mid])
            root.right=self.buildTree(preorder,inorder[mid+1:])
            return root
# @lc code=end

