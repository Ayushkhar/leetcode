# Last updated: 6/6/2026, 10:25:40 PM
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #s target hogya
        s=sum(nums)/2
        if sum(nums)%2!=0:
            return False
        a=set()
        a.add(0)
        for i in range(len(nums)):
            for j in list(a):
                res=j+nums[i]
                a.add(res)
            # for j in range(len(a)):
            #     res=a[j]+nums[i]
            #     a.add(res)
        if s in a:
            return True
        return False
        

        