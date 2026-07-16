# Last updated: 7/16/2026, 6:38:02 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # if we take the val
            subset.append(nums[i])
            dfs(i + 1)
            # if we dont
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
                
        