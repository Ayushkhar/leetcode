# Last updated: 6/6/2026, 10:26:01 PM
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0

        citations.sort(reverse=True)
        flag = 0
        for i in range(len(citations)):
            if citations[i] > i:
                flag += 1
            else:
                return i  
        return len(citations)  
