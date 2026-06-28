# Last updated: 6/28/2026, 6:11:04 AM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        for i in range(n):
            def dfs(openb, closedb):
                if(openb == closedb == n):
                    res.append("".join(stack))
                    return 
                if(openb < n):
                    stack.append("(")
                    dfs(openb + 1,closedb)
                    stack.pop()
                if(closedb < openb):
                    stack.append(")")
                    dfs(openb, closedb + 1)
                    stack.pop()
        dfs(0,0)
        return res


