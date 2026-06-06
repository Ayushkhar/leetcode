# Last updated: 6/6/2026, 10:24:35 PM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        H=defaultdict(list)
        for a,b in edges:
            H[a].append(b)
            H[b].append(a)

        visit=set()
        q=deque([source])

        while q:
            a=q.popleft()
            if a==destination:
                return True
            else:
                for i in H[a]:
                    if i not in visit:
                        visit.add(i)
                        q.append(i)
        return False
        
        