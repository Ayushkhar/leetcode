# Last updated: 6/12/2026, 5:51:50 PM
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def ispossible(mid):
            currsum =0
            subarr=0
            for n in nums:
                currsum+=n
                if currsum >mid:
                    subarr+=1
                    currsum= n
            return subarr+1<=k


        l=max(nums)
        r=sum(nums)
        res=r

        while(l<=r):
            mid = (l+r)//2

            if(ispossible(mid)):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res

                