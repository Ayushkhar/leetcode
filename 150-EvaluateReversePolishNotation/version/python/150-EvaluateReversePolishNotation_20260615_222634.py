# Last updated: 6/15/2026, 10:26:34 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        self.stack = []
4        res=0
5        if len(tokens)<=2:
6            return int(float(tokens[0]))
7
8        for i in range(len(tokens)):
9            if(tokens[i]=="*" or tokens[i]=="/" or tokens[i]=="+" or tokens[i]=="-"):
10                b=self.stack.pop()
11                a=self.stack.pop()
12                l=tokens[i]
13                match l:
14                    case "*":
15                        res = int(a) * int(b)
16                        self.stack.append(res)
17
18                    case "/":
19                        res = int(a) / int(b)
20                        self.stack.append(res)
21                    case "+":
22                        res = int(a) + int(b)
23                        self.stack.append(res)
24                    case "-":
25                        res = int(a) - int(b)
26                        self.stack.append(res)
27            else:
28                self.stack.append(tokens[i])
29        return int(float(res))
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48