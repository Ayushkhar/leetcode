# Last updated: 6/6/2026, 10:25:04 PM
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        #I wwill do it by hash wali technique singl hash
        indegree=defaultdict(int)
        outdegree = defaultdict(int) #default dict only gets 0 values default

        for a,b in trust:
            indegree[b]+=1
            outdegree[a]+=1

        for p in range(1,n+1):
            if indegree[p] == n-1 and outdegree[p]==0:
                return p
        return -1

        