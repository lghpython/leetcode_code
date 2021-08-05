#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        queue = [root]
        ans = [] 
        fromleft = True
        while queue:
            n = len(queue)
            tmp = []

            for i in range(n):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if  node.right: 
                    queue.append(node.right)
        
            ans.append(tmp if fromleft else tmp[::-1])
            fromleft ^= True
        return ans
# @lc code=end

