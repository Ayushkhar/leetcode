# Last updated: 6/25/2026, 1:15:28 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        rsl = [0]  * len(height)
4        lsl = [0] * len(height)
5
6        rsl[len(height) - 1] = height[len(height) - 1]
7        lsl[0] = height[0]
8
9        for i in range(len(height)-2,-1,-1):
10            rsl[i]= max(rsl[i+1],height[i])
11            
12
13        for j in range(1,len(height)):
14            lsl[j] = max(lsl[j-1],height[j])
15
16        sum = 0
17
18        for h in range(len(height)):
19            sum = sum + (min(rsl[h],lsl[h])-height[h])
20
21        return sum 
22 
23
24
25        
26
27
28            
29        