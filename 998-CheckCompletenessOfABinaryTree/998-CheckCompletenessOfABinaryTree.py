# Last updated: 6/6/2026, 10:25:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        a = deque([root])
        past = False
        while a:
            n = a.popleft()
            if n is None:
                past = True
            else:
                if past is True:
                    return False
                a.append(n.left)
                a.append(n.right)
        return True
