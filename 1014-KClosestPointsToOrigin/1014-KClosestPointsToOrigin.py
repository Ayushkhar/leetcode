# Last updated: 7/10/2026, 8:00:32 PM
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        rs = []
        hsh = defaultdict(list)
        for i in range(len(points)):
            x = pow(points[i][0], 2)
            y = pow(points[i][1], 2)
            sm = x + y
            hsh[sm].append(points[i])
            rs.append(sm)

        rs.sort()
        res = []
        rs = rs[:k]
        for j in rs:
            res.append(hsh[j].pop())
    
        return res


        