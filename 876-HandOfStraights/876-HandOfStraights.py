# Last updated: 7/30/2026, 7:33:57 AM
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # Applying min heap 
        heap = []
        def insert(val):
            heap.append(val) 
            curr_ind = len(heap) - 1
            while curr_ind > 0:
                parent = (curr_ind - 1) // 2
                if heap[curr_ind] < heap[parent]:
                    temp = heap[parent]
                    heap[parent] = heap[curr_ind]
                    heap[curr_ind] = temp
                    curr_ind = parent 
                else:
                    break 

        def delete():
            minimum = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            curr_ind = 0

            while True:
                left = (2*curr_ind) + 1
                right = (2*curr_ind) + 2
                smaller = curr_ind 
                if left < len(heap) and heap[left] < heap[smaller]:
                    smaller = left
                if right < len(heap) and heap[right] < heap[smaller]:
                    smaller = right 
                if smaller == curr_ind:
                    break 
                temp = heap[curr_ind]
                heap[curr_ind] = heap[smaller]
                heap[smaller] = temp
                curr_ind = smaller
            return minimum 

        # Main logic 
        # Building counter hashmap
        hsh = {}
        for h in hand:
            if h in hsh:
                hsh[h]+=1
            else:
                hsh[h] = 1

        # Insertion of values
        for h, freq in hsh.items():
            insert([h, freq])
        res = []
        while heap:
            while heap and hsh[heap[0][0]] == 0:
                delete()
            if not heap:
                break
            start = heap[0][0]
            for i in range(start, start + groupSize):
                if i not in hsh or hsh[i] == 0:
                    return False 
                hsh[i]-=1
        return True 


        # return sort_hand_key

        