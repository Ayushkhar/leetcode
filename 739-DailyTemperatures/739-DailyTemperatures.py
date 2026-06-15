# Last updated: 6/15/2026, 10:28:26 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        i=0
        self.stack=[]
        while(i<len(temperatures)):
            while(len(self.stack)!=0 and temperatures[i]>temperatures[self.stack[-1]]):
                a=self.stack.pop()
                res[a]=i-a

            self.stack.append(i)
            i=i+1
        return res

        



        