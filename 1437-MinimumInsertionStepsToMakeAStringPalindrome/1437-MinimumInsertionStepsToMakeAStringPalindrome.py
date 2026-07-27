# Last updated: 7/27/2026, 12:25:41 PM
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp =[]
        for i in range(n):
            r = []
            for j in range(n):
                r.append(-1)
            dp.append(r)
        def solve(i, j):
            if i>=j:
                return 0
            if dp[i][j]!= -1:
                return dp[i][j]

            if s[i] == s[j]:
                dp[i][j] = solve(i+1, j-1)

            else:
                dp[i][j] = 1 + min(solve(i + 1, j), solve(i, j -1))
            return dp[i][j]

        return solve(0, len(s) -1)
