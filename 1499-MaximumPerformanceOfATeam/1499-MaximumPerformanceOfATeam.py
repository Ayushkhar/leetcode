# Last updated: 7/10/2026, 8:00:18 PM
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        heap_speed = []
        eng = []
        
        for j in range(len(efficiency)):
            eng.append([efficiency[j],speed[j]])
        eng.sort(reverse = True)
        # return eng 
        def insert_min_heap_speed(val):
            nonlocal heap_speed
            heap_speed.append(val)
            curr_ind = len(heap_speed) - 1
            while curr_ind > 0:
                parent = (curr_ind-1) // 2
                if(heap_speed[curr_ind]<heap_speed[parent]):
                    temp = heap_speed[curr_ind]
                    heap_speed[curr_ind] = heap_speed[parent]
                    heap_speed[parent] = temp

                    curr_ind = parent
                else:
                    break
        def delete_min_heap_speed():
            minimum = heap_speed[0]
            heap_speed[0] = heap_speed[-1]
            heap_speed.pop()

            curr_ind = 0
            while True:
                left = (2*curr_ind) + 1
                right = (2*curr_ind) + 2
                smaller = curr_ind

                if(left < len(heap_speed) and heap_speed[left] < heap_speed[smaller]):
                    smaller = left

                if(right < len(heap_speed) and heap_speed[right] < heap_speed[smaller]):
                    smaller = right

                if smaller == curr_ind:
                    break

                temp = heap_speed[curr_ind]
                heap_speed[curr_ind] = heap_speed[smaller]
                heap_speed[smaller] = temp

                curr_ind = smaller
            return minimum

        speed_sum = 0
        ans = 0
        for eff,sp in eng:
            insert_min_heap_speed(sp)
            speed_sum += sp

            if len(heap_speed) > k:
                speed_sum = speed_sum - delete_min_heap_speed()

            ans =  max(ans, speed_sum * eff)

        return ans % (pow(10,9) + 7)

            





      

            




        