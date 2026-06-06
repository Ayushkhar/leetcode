# Last updated: 6/6/2026, 10:24:53 PM
from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        l = []  
        for num in arr:
            if num * 2 in l or (num % 2 == 0 and num // 2 in l):
                return True
            l.append(num)
        return False

