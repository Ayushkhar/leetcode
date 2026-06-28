# Last updated: 6/29/2026, 12:55:43 AM
1class Solution:
2    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
3        maxdia = 0
4        def dfs(curr):
5            nonlocal maxdia
6            if curr is None:
7                return 0
8
9            lefth = dfs(curr.left)
10            righth = dfs(curr.right)
11            maxdia = max(maxdia, lefth + righth)
12
13            return 1 + max(lefth, righth)
14        dfs(root)
15        return maxdia
16
17
18        