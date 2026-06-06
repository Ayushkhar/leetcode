# Last updated: 6/6/2026, 10:25:30 PM
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visit = [0] * n

        def dfs(i: int):
            for j in range(n):
                if isConnected[i][j] == 1 and not visit[j]:
                    visit[j] = 1
                    dfs(j)

        prov = 0
        for i in range(n):
            if not visit[i]:
                visit[i] = 1  
                dfs(i)
                prov=prov+1

        return prov