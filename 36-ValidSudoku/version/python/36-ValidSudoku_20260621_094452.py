# Last updated: 6/21/2026, 9:44:52 AM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        row = [set() for _ in range(9)]
4        col = [set() for _ in range(9)] 
5        grd = [set() for _ in range(9)]
6
7        for i in range(9):
8            for j in range(9):
9                num = board[i][j]
10                box = (i//3)*3 +(j//3)
11                if num == ".":
12                    continue
13                if num in list(row[i]):
14                    return False
15                if num in list(col[j]):
16                    return False
17                if num in list(grd[box]):
18                    return False
19                row[i].add(num)
20                col[j].add(num)
21                grd[box].add(num)
22        return True
23        