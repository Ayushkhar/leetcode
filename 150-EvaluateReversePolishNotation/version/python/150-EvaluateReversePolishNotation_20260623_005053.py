# Last updated: 6/23/2026, 12:50:53 AM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        self.stack = []
4        for i in range(len(tokens)):
5            if(tokens[i] != "+" and tokens[i] != "*" and tokens[i] != "/" and tokens[i] != "-"):
6                self.stack.append(tokens[i])
7            else:
8                res = 0
9                a = int(self.stack.pop())
10                b = int(self.stack.pop())
11
12                if(tokens[i] == "*"):
13                    res = a*b
14                    self.stack.append(res)
15
16                elif(tokens[i] == "/"):
17                    res =  b / a
18                    self.stack.append(res)
19
20                elif(tokens[i] == "+"):
21                    res = a + b
22                    self.stack.append(res)
23
24                elif(tokens[i] == "-"):
25                    res = b-a
26                    self.stack.append(res)
27
28
29        return int(self.stack[-1])
30