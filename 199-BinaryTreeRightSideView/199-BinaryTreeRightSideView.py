# Last updated: 7/9/2026, 12:40:42 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return []

        q = deque()
        q.append(root)
        while q:
            lastv = 0
            for i in range(len(q)):
                a= q.popleft()
                lastv = a.val
                if(a.left):
                    q.append(a.left)
                if(a.right):
                    q.append(a.right)
            res.append(a.val)
        return res
        