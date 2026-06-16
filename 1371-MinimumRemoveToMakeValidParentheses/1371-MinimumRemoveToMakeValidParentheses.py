# Last updated: 6/16/2026, 9:27:00 PM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        self.stack =[]
        s=list(s)

        for i in range(len(s)):
            if(s[i]=="("):
                self.stack.append(i)
            elif(s[i]==")"):
                if(len(self.stack)!=0):
                    self.stack.pop()
                else:
                    s[i]=""

        while len(self.stack)!=0:
            a=self.stack.pop()
            s[a]=""
                

        return "".join(s)


        