# @before-stub-for-debug-begin
from python3problem104 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def dfs(depth, curTree):
            if curTree is None:return depth
            return max(dfs(depth+1,curTree.left),dfs(depth+1,curTree.right))

        return dfs(0, root)

        """方法二， 深度搜索优先
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) +1 if root else 0
        """

        """方法三， 广度搜索优先
        if root is None: return 0
        queue = [root] # 当前深度的节点列表
        res = 0
        while queue:  # 遍历所有深度节点列表
            n = len(queue)
            
            for i in range(n):
                node = queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res += 1
        return res
            
        """
# @lc code=end

