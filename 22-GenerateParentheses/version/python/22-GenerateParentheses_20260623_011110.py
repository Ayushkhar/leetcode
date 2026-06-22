# Last updated: 6/23/2026, 1:11:10 AM
1class Solution:
2    def generateParenthesis(self, n: int) -> List[str]:
3
4
5        self.stack = []
6        self.res = []
7
8        def backtrack(open,closed):
9            if(open == closed == n):
10                self.res.append("".join(self.stack))
11                return      
12            if(open < n):
13                self.stack.append("(")
14                backtrack(open + 1, closed)
15                self.stack.pop()
16            if(closed < open):
17                self.stack.append(")")
18                backtrack(open, closed + 1)
19                self.stack.pop()
20
21        backtrack(0,0)
22        return self.res