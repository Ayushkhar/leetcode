# Last updated: 6/7/2026, 7:09:14 PM
1class Solution:
2    def splitArray(self, nums: List[int], k: int) -> int:
3        def ispossible(mid):
4            currsum =0
5            subarr=0
6            for n in nums:
7                currsum+=n
8                if currsum >mid:
9                    subarr+=1
10                    currsum= n
11            return subarr+1<=k
12
13
14        l=max(nums)
15        r=sum(nums)
16        res=r
17
18        while(l<=r):
19            mid = (l+r)//2
20
21            if(ispossible(mid)):
22                res=mid
23                r=mid-1
24            else:
25                l=mid+1
26        return res
27
28                