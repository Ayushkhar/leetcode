# Last updated: 7/16/2026, 6:37:22 PM
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        def insert(val):
            heap.append(val)
            curr_ind = len(heap) - 1
            while(curr_ind > 0):
                parent = (curr_ind - 1) // 2
                if heap[curr_ind] > heap[parent]:
                    temp = heap[curr_ind]
                    heap[curr_ind] = heap[parent]
                    heap[parent]= temp
                    curr_ind = parent 
                else:
                    break 
            
        def delete():
            maximum = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            if len(heap) == 0:
                return maximum
            curr_ind = 0
            while True:
                left = (2*curr_ind) +1
                right = (2*curr_ind) +2
                larger = curr_ind

                if left < len(heap) and heap[left] > heap[larger]:
                    larger = left 
                if right < len(heap) and heap[right] > heap[larger]:
                    larger = right
                if larger == curr_ind:
                    break
                temp = heap[curr_ind]
                heap[curr_ind] = heap[larger]
                heap[larger] = temp
                curr_ind = larger
            return maximum
        for i in range(len(nums)):
            insert(nums[i])
        for j in range(k-1):
            delete()
        return heap[0]

        