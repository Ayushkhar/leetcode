# Last updated: 6/6/2026, 10:26:38 PM
class Solution:
    def candy(self, ratings: List[int]) -> int:
        candyl = [1]
        candyr = [1]
        relvl = 1
        relvr = 1

        for i in range(1,len(ratings)):
            if(ratings[i-1]>=ratings[i]):
                relvl = 1
                candyl.append(relvl)
            else:
                relvl = relvl + 1
                candyl.append(relvl)

        for j in range(len(ratings)-1,0,-1):
            if(ratings[j-1]<=ratings[j]):
                relvr = 1
                candyr.append(relvr)
            else:
                relvr = relvr + 1
                candyr.append(relvr)

        candyr.reverse()
        res = []
        for k in range(len(ratings)):
            res.append(max(candyl[k],candyr[k]))
        return sum(res) 


        