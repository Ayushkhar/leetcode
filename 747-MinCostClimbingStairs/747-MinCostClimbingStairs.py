# Last updated: 6/6/2026, 10:25:21 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        onestep=cost[0]
        twostep=cost[1]

        for i in range(2,len(cost)):
            res=cost[i]+min(onestep,twostep)
            onestep=twostep
            twostep=res
        return min(onestep,twostep)
        