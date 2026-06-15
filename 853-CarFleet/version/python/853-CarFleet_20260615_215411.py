# Last updated: 6/15/2026, 9:54:11 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        arr=[0] * len(position)
4        for i in range(len(position)):
5            time = (target - position[i])/speed[i]
6            arr[i] = time
7        hsh=defaultdict(int)
8        for j in range(len(position)):
9            hsh[position[j]]=arr[j]
10
11        pos = sorted(hsh.keys())
12        prevtime=0
13        fleet=0
14        for i in range(len(position)-1,-1,-1):
15            currtime= hsh[pos[i]]
16            if currtime > prevtime:
17                fleet+=1
18                prevtime =currtime 
19        return fleet
20
21        