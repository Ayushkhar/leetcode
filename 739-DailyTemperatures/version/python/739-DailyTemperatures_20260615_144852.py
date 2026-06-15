# Last updated: 6/15/2026, 2:48:52 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        res=[0]*len(temperatures)
4        self.stack =[]
5        i=0
6        while(i<len(temperatures)):
7            while(len(self.stack)!=0 and temperatures[i]>temperatures[self.stack[-1]]):
8                a=self.stack.pop()
9                res[a]=(i-a)
10            self.stack.append(i)
11            i=i+1
12        return res
13
14