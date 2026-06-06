# Last updated: 6/6/2026, 10:26:42 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # flag =True
        count =1
        max_count=1
        a=sorted(nums)
        if len(nums)<1:
            return 0
        for i in range(1,len(a)):
            if a[i]==a[i-1]:
                continue
            elif a[i]-a[i-1]==1:
                count+=1
            else:
                count=1
            max_count = max(max_count, count)
        return max_count 
        
                


       
        