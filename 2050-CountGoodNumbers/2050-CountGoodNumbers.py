# Last updated: 6/6/2026, 10:24:36 PM
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        po = 10**9 + 7

        a = (n + 1) // 2
        b = n // 2

        res = (pow(5, a, po) * pow(4, b, po)) % po
        return res


        