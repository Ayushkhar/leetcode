# Last updated: 7/9/2026, 12:41:45 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if root is None:
            return []
        q.append(root)
        while q:
            lev = []
            for i in range(len(q)):
                a = q.popleft()
                v = a.val
                lev.append(v)
                if a.left:
                    q.append(a.left)
                if a.right:
                    q.append(a.right)
            res.append(lev)
        return res
                    
        