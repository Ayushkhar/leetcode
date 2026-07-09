# Last updated: 7/9/2026, 12:41:56 PM
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        x = len(word)
        row = len(board)
        cols = len(board[0])

        def solve(i, j, k):
            if k == x:
                return True 
            if(i <0 or j<0 or i>=row or j>=cols):
                return False
            if(board[i][j]!=word[k]):
                return False
            temp = board[i][j]

            board[i][j] ="#"

            found = solve(i+1,j,k+1) or solve(i-1,j,k+1) or solve(i,j+1,k+1) or solve(i,j-1,k+1)
            
            board[i][j] =temp
            return found 

        for i in range(row):
            for j in range(cols):
                if(solve(i,j,0)):
                    return True 
        return False  
        