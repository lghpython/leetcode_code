#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(l,r, node):
            """ 深度搜索
            : @param l: 保留左边界
            ：#param r: 保留右边界
            """
            if node is None: return True
            if l >= node.val or r <= node.val: 
                return False
            return dfs(l, node.val,node.left) and dfs(node.val,r,node.right)            
        return dfs(root.val, float('inf'), root.right) and dfs(float('-inf'),root.val,root.left)

        """ 中序遍历法
        stack,minum = [], float('-inf')

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val<= minum:
                return False
            minum = root.val
            root = root.right
        return True
        """
# @lc code=end

