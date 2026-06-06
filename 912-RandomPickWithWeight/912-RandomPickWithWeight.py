# Last updated: 6/6/2026, 10:25:13 PM
import random
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        t = 0
        for i in w:
            t += i
            self.prefix.append(t)
        self.total = t  

    def pickIndex(self) -> int:
        rand = random.randint(1, self.total)
        def binary_search_left(arr, x):
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid
            return low

        index = binary_search_left(self.prefix, rand)
        return index

