# Last updated: 6/6/2026, 10:24:15 PM
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        arr = [0] * n

        for i in range(n-1,-1,-1):
            if i+k >= n:
                arr[i] = energy[i]
            else:
                # arr = [0,0,-10,-5,1]
                arr[i] = energy[i] + arr[i+k]
        return max(arr)
