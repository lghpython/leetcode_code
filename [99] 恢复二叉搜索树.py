#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # """ # 中序遍历
        stack = []
        x = y = pred = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pred and root.val< pred.val: # 出口 找到替换值跳出循环
                y = root
                if x is None:
                    x = pred
                else:break
            pred = root 
            root = root.right
        x.val, y.val = y.val, x.val
        """ # 进阶 使用常数空间
        x=y=pred=predecessor=None 

        while root:
            if root.left:
                predecessor = root.left
                while predecessor.right and predecessor.right != root:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    predecessor.right = root
                    root = root.left
                else:
                    # 执行出口， 每个底层右节点 完成循环， 标记替换值，断开环
                    if pred and root.val < pred.val:
                        y = root
                        if x is None: 
                            x = pred
                    pred = root
                    predecessor.right = None
                    root = root.right
            else:
                
                if pred and root.val< pred.val:
                    y = root
                    if x is None: 
                        x = pred
                print(x.val,y.val,root.val)
                pred = root
                root = root.right
        print(x,y)
        x.val, y.val = y.val, x.val
        """
# @lc code=end

