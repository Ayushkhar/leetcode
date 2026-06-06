# Last updated: 6/6/2026, 10:24:28 PM
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([root])
        level = 0 
        while q:
            if level %2 != 0:
                l = 0          
                r = len(q)-1    
                while l<r: 
                    q[l].val,q[r].val = q[r].val,q[l].val
                    l+=1
                    r-=1
            for i in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)
   
            level += 1
        return root
        