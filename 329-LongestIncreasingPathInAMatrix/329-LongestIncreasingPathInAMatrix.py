# Last updated: 6/6/2026, 10:25:52 PM
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        row=len(matrix)
        cols=len(matrix[0])

        dp={}

        def solve(i,j):
            if (i,j) in dp:
                return dp[(i,j)]
            max_len=0

            if i+1<row and matrix[i+1][j]>matrix[i][j]:
                max_len=max(max_len,1+solve(i+1,j))
            if i-1>=0 and matrix[i-1][j]>matrix[i][j]:
                max_len=max(max_len,1+solve(i-1,j))
            if j+1<cols and matrix[i][j+1]>matrix[i][j]:
                max_len=max(max_len,1+solve(i,j+1))
            if j-1>=0 and matrix[i][j-1]>matrix[i][j]:
                max_len=max(max_len,1+solve(i,j-1))
            dp[(i,j)]=max_len
            return max_len
        res=0
        for i in range(row):
            for j in range(cols):
                res=max(res,solve(i,j))
        return res+1
