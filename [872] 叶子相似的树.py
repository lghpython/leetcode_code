# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.leaf(root1, "")==self.leaf(root2, "")

    def leaf(self, root: TreeNode, s: string ):
        if not root: return s
        if not root.right and not root.left:
            s += "_"+str(root.val)
            return s
        return self.leaf(root.left,s) + self.leaf(root.right, s) 



#######################官方题解 ######################
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                yield node.val
            else:
                if node.left:
                    yield from dfs(node.left)
                if node.right:
                    yield from dfs(node.right)
        
        seq1 = list(dfs(root1)) if root1 else list()
        seq2 = list(dfs(root2)) if root2 else list()
        return seq1 == seq2
