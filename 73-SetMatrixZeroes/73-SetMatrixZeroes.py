# Last updated: 6/6/2026, 10:27:00 PM
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])

        zero_wali_row = set()
        zero_wali_column = set()

        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    zero_wali_row.add(i)
                    zero_wali_column.add(j)

        for i in range(r):
            for j in range(c):
                if i in zero_wali_row or j in zero_wali_column:
                    matrix[i][j] = 0
                    

      
            
