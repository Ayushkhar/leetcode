# Last updated: 7/4/2026, 4:10:57 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def rob(self, root: Optional[TreeNode]) -> int:
9        def dfs(root):
10            if root is None:
11                return [0,0]
12            leftpair = dfs(root.left)
13            rightpair = dfs(root.right)
14
15            withroot = root.val + leftpair[1] + rightpair[1]
16            withoutroot = max(leftpair) + max(rightpair)
17
18            return [withroot, withoutroot]
19        return max(dfs(root))