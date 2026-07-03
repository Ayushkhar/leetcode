# Last updated: 7/4/2026, 5:25:28 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def goodNodes(self, root: TreeNode) -> int:
9        if root is None:
10            return 0
11
12        def dfs(node,max_till):
13            # nonlocal
14            if node is None:
15                return 0
16            ans = 0
17            if node.val>=max_till:
18                ans=1
19            max_till = max(max_till,node.val)
20            ans = ans + dfs(node.left,max_till)
21            ans = ans + dfs(node.right,max_till)
22            
23            return ans
24        return dfs(root,root.val)
25
26        