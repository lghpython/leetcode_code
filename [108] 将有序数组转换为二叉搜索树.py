#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        
        n = len(nums)
        def dfs(start,end):
            if start>=end : return None
            i = (end+start)//2
            root = TreeNode(nums[i])
            root.left = dfs(start,i)
            root.right = dfs(i+1, end)
            return root
            
        return dfs(0,n)

        # n = len(nums)
        # def dfs(l,r):
        #     if l>=r : return None
        #     i = (l+r)//2
        #     return TreeNode(nums[i],dfs(l,i), dfs(i+1,r))

        # return dfs(0,n)

# @lc code=end

