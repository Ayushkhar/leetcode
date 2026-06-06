# Last updated: 6/6/2026, 10:26:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.dfspresumm(root,0)
        return self.total
    def dfspresumm(self, root: Optional[TreeNode],currsum) -> int:
        if root == None:
            return
        currsum = currsum * 10 + root.val

        if root.right is None and root.left is None:
            self.total = self.total + currsum
            return self.total
        
        self.dfspresumm(root.left,currsum)
        self.dfspresumm(root.right,currsum)

        