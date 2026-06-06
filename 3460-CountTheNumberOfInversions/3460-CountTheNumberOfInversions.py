# Last updated: 6/6/2026, 10:24:12 PM
MOD = 1_000_000_007
class Solution:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        self.dp = [[None] * (n * (n - 1) // 2 + 1) for _ in range(n + 1)]
        
        requirements.sort(key=lambda x: x[0])
        
        for r in requirements:
            if self.count(r[0], r[1]) == 0:
                return 0
            for i in range(len(self.dp[r[0]])):
                if i != r[1]:
                    self.dp[r[0]][i] = 0

        last = requirements[-1]
        return self.dp[last[0]][last[1]]

    def count(self, pos: int, inv: int) -> int:
        if inv < 0:
            return 0
        if pos == 0:
            return 1 if inv == 0 else 0
        if self.dp[pos][inv] is not None:
            return self.dp[pos][inv]
        
        res = 0
        for i in range(pos + 1):
            res = (res + self.count(pos - 1, inv - i)) % MOD
        self.dp[pos][inv] = res
        return res