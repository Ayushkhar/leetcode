# Last updated: 6/6/2026, 10:25:41 PM
import sys
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        a=int(num1)
        b=int(num2)
        res=a+b
        return str(res)
        