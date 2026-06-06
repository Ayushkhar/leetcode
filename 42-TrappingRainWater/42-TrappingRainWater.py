# Last updated: 6/6/2026, 10:27:12 PM
class Solution:
    def trap(self, height: List[int]) -> int:

        lmax=[0]*len(height)
        rmax=[0]*len(height)
        lmax[0]=height[0]
        rmax[len(height)-1]=height[-1]

        for i in range(1,len(height)):
            newel=height[i]
            if lmax[i-1]<newel:
                lmax[i]=newel
            else:
                lmax[i]=lmax[i-1]
            
        for j in range(len(height)-2,-1,-1):
            newel=height[j]
            if rmax[j+1]<newel:
                rmax[j]=newel
            else:
                rmax[j]=rmax[j+1]
        res=[]
        for k in range(len(height)):
            res.append(min(lmax[k],rmax[k])-height[k])

        return sum(res)



       

           
     

        