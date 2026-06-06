# Last updated: 6/6/2026, 10:24:17 PM
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        res = []
        seen = set()
        n = len(grid)

        # Repetition ke liye Logic
        for i in range(len(grid)):
            for num in grid[i]:
                if num in seen:
                    res.append(num)
                else:
                    seen.add(num)

        # Missing number wala logic
        for i in range(1,n * n + 1):
            if i not in seen:
                res.append(i)

        return res


        
        