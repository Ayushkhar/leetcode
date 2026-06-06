# Last updated: 6/6/2026, 10:26:39 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        
        total = 0
        a = []
        index = 0
        for i in range(len(gas)): 
            diff = gas[i] - cost[i]
            a.append(diff)

        for i in range(len(a)):
            total += a[i]
            if total < 0: 
                total = 0
                index = i + 1

        return index 
