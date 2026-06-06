# Last updated: 6/6/2026, 10:25:02 PM
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        t1 = []
        for i in range(len(nums)):
            #First convert in string 
            t1.append(str(nums[i]))
        #Combine numbers
        t2 = ""
        t3 = []
        for item in t1:
            t2 += item
            t3.append(t2)
        #Now i will convert in binary
        res1 = []
        resf = []
        for j in range(len(nums)):
            res1.append(int(t3[j],2))
            if res1[j] % 5==0:
                resf.append(True)
            else:
                resf.append(False)

        return resf

        
        



