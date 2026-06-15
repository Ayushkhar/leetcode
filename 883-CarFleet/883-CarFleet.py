# Last updated: 6/15/2026, 10:28:21 PM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr=[0] * len(position)
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            arr[i] = time
        hsh=defaultdict(int)
        for j in range(len(position)):
            hsh[position[j]]=arr[j]

        pos = sorted(hsh.keys())
        prevtime=0
        fleet=0
        for i in range(len(position)-1,-1,-1):
            currtime= hsh[pos[i]]
            if currtime > prevtime:
                fleet+=1
                prevtime =currtime 
        return fleet

        