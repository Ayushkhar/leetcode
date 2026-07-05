# Last updated: 7/5/2026, 3:38:01 PM
1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        rss = []
4        lss = []
5        n = len(heights)
6        rse = [n] *n
7        lse = [-1] * n
8        res = [0]*n
9
10        for i in range(len(heights)-1,-1,-1):
11            while rss and heights[rss[-1]]>=heights[i]:
12                rss.pop()
13
14            if rss:
15                rse[i] = rss[-1]
16
17            rss.append(i)
18
19        for j in range(len(heights)):
20            while lss and heights[lss[-1]] >= heights[j]:
21                lss.pop()
22            if lss:
23                lse[j] = lss[-1]
24            lss.append(j)
25
26        for k in range(len(heights)):
27            res[k] = heights[k] * (rse[k] -lse[k] - 1)
28
29
30        return max(res)