# Last updated: 6/23/2026, 12:22:38 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        self.stack = []
4        flag =1
5
6        if(len(s) <2):
7            return False
8
9        for i in range(len(s)):
10            if(s[i] == "{" or s[i] == "(" or s[i] == "["):
11                self.stack.append(s[i])
12            elif(s[i] == "}" or s[i] == ")" or s[i] == "]"):
13                if(len(self.stack)==0):
14                    flag =0
15                    break
16                else:
17                    a = self.stack.pop() 
18                    if(a == "{" and s[i] == "}"):
19                        flag = 1
20                    elif(a == "[" and s[i] == "]"):
21                        flag = 1
22                    elif(a == "(" and s[i] == ")"):
23                        flag = 1
24                    else:
25                        flag =0
26                        break
27    
28            
29        if(flag == 1 and len(self.stack) == 0):
30            return True
31        else:
32            return False
33