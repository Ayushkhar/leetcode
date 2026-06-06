# Last updated: 6/6/2026, 10:26:27 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        res=[]

        while i<j:
            sum=numbers[i]+numbers[j]
            if sum ==target:
                res.append(i+1)
                res.append(j+1)
                break
            elif sum<target:
                i=i+1
            elif sum>target:
                j=j-1

        return res


        