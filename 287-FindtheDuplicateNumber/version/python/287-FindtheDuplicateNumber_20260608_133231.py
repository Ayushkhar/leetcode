# Last updated: 6/8/2026, 1:32:31 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        dc={}
4        # cnt=1
5        for n in nums:
6            if n in dc:
7                dc[n]+=1
8            else:
9                dc[n]=1
10        return max(dc,key=dc.get)
11        
12        # counts =Counter(nums)
13        # return max(counts,key=counts.get)
14        