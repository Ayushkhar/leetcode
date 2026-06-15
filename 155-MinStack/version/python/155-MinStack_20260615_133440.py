# Last updated: 6/15/2026, 1:34:40 PM
1class MinStack:
2
3    def __init__(self):
4        self.stack=[]
5        self.minstack=[]
6    def push(self, value: int) -> None:
7        self.stack.append(value)
8        if len(self.minstack)==0 or self.minstack[-1]>=value:
9            self.minstack.append(value)
10    def pop(self) -> None:
11        if(self.minstack[-1]==self.stack[-1]):
12            self.minstack.pop()
13        self.stack.pop()
14
15    def top(self) -> int:
16        return self.stack[-1]
17    def getMin(self) -> int:
18        return self.minstack[-1]
19        
20
21
22# Your MinStack object will be instantiated and called as such:
23# obj = MinStack()
24# obj.push(value)
25# obj.pop()
26# param_3 = obj.top()
27# param_4 = obj.getMin()