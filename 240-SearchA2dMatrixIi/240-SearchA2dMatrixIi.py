# Last updated: 6/6/2026, 10:26:07 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = 0
        col = len(matrix[0]) - 1
        
        while(row < m and col >= 0):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col = col - 1
            elif matrix[row][col] < target:
                row = row + 1
                
        return False
