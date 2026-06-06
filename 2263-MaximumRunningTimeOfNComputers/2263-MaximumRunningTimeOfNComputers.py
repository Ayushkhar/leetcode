# Last updated: 6/6/2026, 10:24:32 PM
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort()
        # n = len(n)
        bt = len(batteries)

        total = sum(batteries)

        while batteries[-1] > total//n:
            n = n-1
            total = total-batteries.pop()

        return total//n



        
        