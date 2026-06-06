# Last updated: 6/6/2026, 10:25:31 PM
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_dia = 0

        def dfs(node):
            if not node:
                return 0
            lefth = dfs(node.left)
            righth = dfs(node.right)

            self.max_dia = max(self.max_dia,lefth + righth)

            return 1 + max(lefth,righth)
        dfs(root)
        return self.max_dia



