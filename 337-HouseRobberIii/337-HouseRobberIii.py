# Last updated: 6/6/2026, 10:25:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root == None:
                return [0,0]

            dfs_left = dfs(root.left)
            dfs_right = dfs(root.right)

            with_root = root.val +dfs_left[1]+dfs_right[1]
            without_root = max(dfs_left) + max(dfs_right)

            return [with_root,without_root]
        return max(dfs(root))

