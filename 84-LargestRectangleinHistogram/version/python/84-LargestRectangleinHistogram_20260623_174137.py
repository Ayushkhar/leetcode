# Last updated: 6/23/2026, 5:41:37 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        rse =[len(heights)]*len(heights)
4        lse=[-1]*len(heights)
5
6        rss=[]
7        lss=[]
8        res=[0]*len(heights)
9        for i in range(len(heights)-1,-1,-1):
10            while(rss and heights[rss[-1]]>=heights[i]):
11                rss.pop()
12
13            if rss:
14                rse[i] = rss[-1]
15
16            rss.append(i)
17
18        for j in range(len(heights)):
19            while(lss and heights[lss[-1]]>=heights[j]):
20                lss.pop()
21
22            if lss:
23                lse[j]=lss[-1]
24
25            lss.append(j)    
26
27        for k in range(len(heights)):
28            res[k] = heights[k] * (rse[k] - lse[k] - 1)
29
30        return max(res)