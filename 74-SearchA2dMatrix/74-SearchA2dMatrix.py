# Last updated: 6/28/2026, 12:42:50 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flag = True
        for i in matrix:
            low = 0 
            high = len(i) -1
            while(low <= high):
                mid = (low + high) // 2
                if(i[mid] == target):
                    return True
                elif(i[mid] < target):
                    low = mid + 1
                else:
                    high = mid - 1
        return False
            
            

        