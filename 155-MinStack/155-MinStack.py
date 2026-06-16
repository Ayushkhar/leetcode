# Last updated: 6/16/2026, 9:28:25 PM
class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.minstack)==0 or self.minstack[-1]>=value:
            self.minstack.append(value)
    def pop(self) -> None:
        if(self.minstack[-1]==self.stack[-1]):
            self.minstack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()