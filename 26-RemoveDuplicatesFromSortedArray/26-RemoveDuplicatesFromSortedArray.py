# Last updated: 6/6/2026, 10:27:19 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        size = len(nums)  # Total size of the array
        if size == 0:  # Edge case: empty array
            return 0

        idx = 0  # Pointer for the position of the last unique element
        for jdx in range(1, size):
            if nums[jdx] != nums[idx]:
                nums[idx + 1] = nums[jdx]  # Update the next position with the unique element
                idx += 1  # Move the pointer forward

        return idx + 1  # Return the count of unique elements
