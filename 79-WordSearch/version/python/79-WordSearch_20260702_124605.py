# Last updated: 7/2/2026, 12:46:05 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        x = len(word)
4        row = len(board)
5        cols = len(board[0])
6
7        def solve(i, j, k):
8            if k == x:
9                return True 
10            if(i <0 or j<0 or i>=row or j>=cols):
11                return False
12            if(board[i][j]!=word[k]):
13                return False
14            temp = board[i][j]
15
16            board[i][j] ="#"
17
18            found = solve(i+1,j,k+1) or solve(i-1,j,k+1) or solve(i,j+1,k+1) or solve(i,j-1,k+1)
19            
20            board[i][j] =temp
21            return found 
22
23        for i in range(row):
24            for j in range(cols):
25                if(solve(i,j,0)):
26                    return True 
27        return False  
28        