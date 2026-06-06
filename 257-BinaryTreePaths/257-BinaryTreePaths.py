# Last updated: 6/6/2026, 10:26:04 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def depthfirst(node,leaf):
            if not node:
                return

            leaf = leaf + str(node.val)
            
            if not node.left and not node.right:
                res.append(leaf)
                return

            leaf = leaf + "->"
            depthfirst(node.left,leaf)
            depthfirst(node.right,leaf)
        
        depthfirst(root, "")

        return res
