# Last updated: 6/6/2026, 10:26:19 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=[]

        for l in range(row):
            visited.append([0]*col)

        def dfs(i,j):
            if i<0 or j<0 or i>=row or j>=col:
                return 
            if visited[i][j]==1 or grid[i][j]=="0":
                return 
            visited[i][j]=1
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)

        cnt=0
        for k in range(row):
            for u in range(col):
                if grid[k][u]=="1" and  visited[k][u]==0:
                    cnt+=1
                    dfs(k,u)
        return cnt 

        # return visited

        