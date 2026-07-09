# Last updated: 7/9/2026, 10:24:50 PM
1class Solution:    
2    def findKthLargest(self, nums: List[int], k: int) -> int: 
3        heap = []
4        def insert(value):
5            nonlocal heap
6            heap.append(value)
7            curr_ind = len(heap) - 1
8
9            while curr_ind > 0:
10                parent = (curr_ind - 1)// 2
11                if heap[parent] < heap[curr_ind]:
12                    temp = heap[parent]
13                    heap[parent] =heap[curr_ind]
14                    heap[curr_ind] =temp
15
16                    curr_ind = parent
17                    
18                else:
19                    break 
20
21        for x in nums:
22            insert(x)
23        def delete(heap):
24            if len(heap) ==1:
25                return heap.pop()
26            maxi = heap[0]
27            heap[0] = heap[-1]
28            heap.pop()
29
30            curr = 0
31            while True:
32                left = (2*curr) + 1
33                right = (2*curr) + 2
34
35                larger = curr
36                if(left < len(heap) and heap[left] > heap[larger]):
37                    larger = left
38
39                if(right < len(heap) and heap[right] > heap[larger]):
40                    larger = right
41
42                if larger == curr:
43                        break
44                    
45                temp = heap[curr]
46                heap[curr] = heap[larger]
47                heap[larger] = temp
48
49                curr = larger 
50            return maxi
51        for _ in range(k-1):
52            delete(heap)
53        return heap[0]
54
55
56        
57
58
59
60            
61
62        