# Last updated: 7/16/2026, 6:36:47 PM
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        hsh = {}

        def insert_maxheap(val):
            heap.append(val)
            curr_ind = len(heap) - 1

            while curr_ind > 0:
                parent = (curr_ind - 1) // 2
                if heap[curr_ind] > heap[parent]:
                    temp = heap[curr_ind]
                    heap[curr_ind] = heap[parent]
                    heap[parent] = temp

                    curr_ind = parent
                else:
                    break 

        def delete_maxheap():
            maximum = heap[0]
            heap[0] = heap[-1]
            heap.pop()      

            curr_ind = 0
            while True:
                left = (2 * curr_ind) + 1
                right = (2 * curr_ind) + 2
                larger = curr_ind

                if(left < len(heap) and heap[left] > heap[larger]):
                    larger = left 
                if(right < len(heap) and heap[right] > heap[larger]):
                    larger = right 

                if(larger == curr_ind):
                    break 

                temp = heap[curr_ind]
                heap[curr_ind] = heap[larger]
                heap[larger] = temp

                curr_ind = larger 

            return maximum

        # Figuring out the frequencies 
        hsh = {}

        for task in tasks:
            if task in hsh:
                hsh[task] += 1
            else:
                hsh[task] = 1

        #  Pushing in the heap 

        for freq in hsh.values():
            insert_maxheap(freq)

        # desingning the queue 

        q = deque()
        time = 1
        while heap or q:
            while q and q[0][1] == time:
                insert_maxheap(q[0][0])
                q.popleft()

            if heap: 
                freq = delete_maxheap()
                freq -= 1

                if freq > 0:
                    q.append([freq, time + (n + 1)])
            time += 1

        return time - 1

            