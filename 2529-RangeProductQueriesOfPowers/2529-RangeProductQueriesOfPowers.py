# Last updated: 6/6/2026, 10:24:27 PM
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        powers = []

        for i in range(32):
            if(n & (1<<i) != 0):
                powers.append(pow(2,i))
            

        ans = []
        for s,e in queries:
            prod = 1
            for i in range(s,e+1): 
                prod = (prod * powers[i]) % mod
            ans.append(prod)
        return ans


        
