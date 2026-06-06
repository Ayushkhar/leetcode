# Last updated: 6/6/2026, 10:25:36 PM
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def solve(index,current_sum):
            if index==len(nums):
                return 1 if current_sum==target else 0
            if (index,current_sum) in dp:
                return dp[(index,current_sum)]
            

            plus =solve(index+1,current_sum+nums[index])
            minus=solve(index+1,current_sum-nums[index])

            res= plus+minus
            dp[(index,current_sum)]=res
            return res

        a=solve(0,0)
        return a
        