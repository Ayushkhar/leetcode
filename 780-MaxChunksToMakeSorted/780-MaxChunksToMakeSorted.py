# Last updated: 6/6/2026, 10:25:18 PM
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        temp=sorted(arr)
        count=0
        maxseen=0
        for i in range(len(arr)):
            maxseen=max(maxseen,arr[i])
            if(maxseen==temp[i]):
                count+=1
        return count

        