# Last updated: 7/9/2026, 12:38:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0

        def dfs(node,max_till):
            # nonlocal
            if node is None:
                return 0
            ans = 0
            if node.val>=max_till:
                ans=1
            max_till = max(max_till,node.val)
            ans = ans + dfs(node.left,max_till)
            ans = ans + dfs(node.right,max_till)
            
            return ans
        return dfs(root,root.val)

        