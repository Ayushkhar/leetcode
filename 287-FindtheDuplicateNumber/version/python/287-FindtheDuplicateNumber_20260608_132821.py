# Last updated: 6/8/2026, 1:28:21 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        # dc={}
4        # cnt=0
5        # for n in nums:
6        #     if n in dc:
7            
8        #     dc[n]=cnt+1
9        counts =Counter(nums)
10        return max(counts,key=counts.get)
11        