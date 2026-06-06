# Last updated: 6/6/2026, 10:24:23 PM
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        
        count = 0
        rec = []
        for i in range(low,high + 1):
            s = str(i)
            n = len(s)

            if n % 2 == 0:
                half = n // 2

                sum1 = 0
                for c in s[:half]:
                    sum1 = sum1 + int(c)
                sum2 = 0
                for g in s[half:]:
                    sum2 = sum2 + int(g)

                if sum1 == sum2:
                    rec.append(i)
        return len(rec)



                
