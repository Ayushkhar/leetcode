# Last updated: 6/6/2026, 10:26:50 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        r = []
        level = 0
        self.zigza(level,root,r)
        return r
    def zigza(self,level,root,r):
        if root is None:
            return []
        if len(r) <= level:
            r.append([])

        if level%2 == 0:
            r[level].append(root.val)
        else:
            r[level].insert(0,root.val)

        self.zigza(level+1,root.left,r)
        self.zigza(level+1,root.right,r)

        
        