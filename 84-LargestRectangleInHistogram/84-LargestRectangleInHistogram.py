# Last updated: 6/28/2026, 6:10:47 AM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rse =[len(heights)]*len(heights)
        lse=[-1]*len(heights)

        rss=[]
        lss=[]
        res=[0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while(rss and heights[rss[-1]]>=heights[i]):
                rss.pop()

            if rss:
                rse[i] = rss[-1]

            rss.append(i)

        for j in range(len(heights)):
            while(lss and heights[lss[-1]]>=heights[j]):
                lss.pop()

            if lss:
                lse[j]=lss[-1]

            lss.append(j)    

        for k in range(len(heights)):
            res[k] = heights[k] * (rse[k] - lse[k] - 1)

        return max(res)