# Last updated: 7/27/2026, 12:25:19 PM
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        cnt = 0 
        def back(child, rem):
            nonlocal cnt
            if child == 3:
                if rem == 0:
                    cnt+=1
                return 
            for gv in range(limit + 1):
                if gv > rem:
                    break
                back(child + 1,rem - gv)
        back(0, n)
        return cnt 
