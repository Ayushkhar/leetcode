# Last updated: 6/16/2026, 1:12:13 PM
1class Solution:
2    def minRemoveToMakeValid(self, s: str) -> str:
3        self.stack =[]
4        s=list(s)
5
6        for i in range(len(s)):
7            if(s[i]=="("):
8                self.stack.append(i)
9            elif(s[i]==")"):
10                if(len(self.stack)!=0):
11                    self.stack.pop()
12                else:
13                    s[i]=""
14
15        while len(self.stack)!=0:
16            a=self.stack.pop()
17            s[a]=""
18                
19
20        return "".join(s)
21
22
23        