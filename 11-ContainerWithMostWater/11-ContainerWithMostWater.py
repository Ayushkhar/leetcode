# Last updated: 6/6/2026, 10:27:29 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i =0 
        j=len(height)-1
        res=0
        while i<j:
            a=min(height[i],height[j])
            ar=a*(j-i)
            res=max(res,ar)
            if height[i]<height[j]:
                i+=1
            elif height[i]>=height[j]:
                j-=1
        return res