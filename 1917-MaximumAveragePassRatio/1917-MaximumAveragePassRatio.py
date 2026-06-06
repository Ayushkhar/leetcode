# Last updated: 6/6/2026, 10:24:38 PM
from heapq import heappush, heappop
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Helper function to calculate the gain in average pass ratio
        def gain(pass_students, total_students):
            return (pass_students + 1) / (total_students + 1) - pass_students / total_students

        # Max-heap to store classrooms by the most gain
        heap = []
        for pass_students, total_students in classes:
            heappush(heap, (-gain(pass_students, total_students), pass_students, total_students))
        
        # Allocate extra students
        for _ in range(extraStudents):
            g, pass_students, total_students = heappop(heap)
            pass_students += 1
            total_students += 1
            heappush(heap, (-gain(pass_students, total_students), pass_students, total_students))
        
        # Calculate the final average ratio
        total_avg = sum(pass_students / total_students for _, pass_students, total_students in heap) / len(classes)
        return total_avg
