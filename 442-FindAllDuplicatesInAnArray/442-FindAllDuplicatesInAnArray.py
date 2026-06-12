# Last updated: 6/12/2026, 5:51:48 PM
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hsh={}
        for n in nums:
            if n in hsh:
                hsh[n]+=1
            else:
                hsh[n]=1
        res=[]

        for key,val in hsh.items():
            if val==2:
                res.append(key)
        return res

        