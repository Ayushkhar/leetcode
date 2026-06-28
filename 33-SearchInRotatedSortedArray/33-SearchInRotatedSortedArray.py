# Last updated: 6/28/2026, 12:43:01 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # finding the peak element first 
        def Peak():
            low = 0 
            high  = len(nums) - 1

            while(low < high):
                mid = (low + high) // 2
                if(nums[mid] > nums[high]):
                    low = mid + 1
                else:
                    high = mid 

            return low 

        def ascbinary(low,high):
            while(low <= high):
                mid = (low + high) // 2
                if(nums[mid] == target):
                    return mid
                elif(nums[mid] < target):
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        
        pivot = Peak()
        left = ascbinary(0,pivot-1) 
        if(left != -1):
            return left 
        return ascbinary(pivot, len(nums)-1) 

        






